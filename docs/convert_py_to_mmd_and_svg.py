# -*- coding: utf-8 -*-
import ast
import astor
import re
import subprocess
import os

def clean_label(label):
    """Remove caracteres problemáticos e espaços extras."""
    label = re.sub(r"[{}\"\\\[\]<>]", "", label)
    label = re.sub(r"\s+", " ", label)
    return label.strip()

def extract_mermaid_from_python_code(code_str):
    """
    Gera fluxograma Mermaid com setas 'Sim' e 'Não' para decisões e loops.
    """
    tree = ast.parse(code_str)
    mermaid = ["graph TD"]
    node_counter = 0

    def new_node(label, shape="rect"):
        nonlocal node_counter
        label = clean_label(label)
        node_id = f"N{node_counter}"
        node_counter += 1
        if shape == "diamond":
            mermaid.append(f'{node_id}{{"{label}"}}')
        else:
            mermaid.append(f'{node_id}["{label}"]')
        return node_id

    def walk(node, parent=None):
        if isinstance(node, ast.FunctionDef):
            curr = new_node(f"Func: {node.name}()")
            if parent:
                mermaid.append(f"{parent} --> {curr}")
            for stmt in node.body:
                walk(stmt, curr)
            return curr

        elif isinstance(node, ast.If):
            cond = new_node(f"If: {astor.to_source(node.test).strip()}", "diamond")
            if parent:
                mermaid.append(f"{parent} --> {cond}")
            # Caminho "Sim"
            last_true = cond
            for stmt in node.body:
                true_node = walk(stmt, last_true)
                mermaid.append(f"{cond} -->|Sim| {true_node}")
            # Caminho "Não"
            if node.orelse:
                for stmt in node.orelse:
                    false_node = walk(stmt, cond)
                    mermaid.append(f"{cond} -->|Não| {false_node}")
            return cond

        elif isinstance(node, ast.While):
            cond = new_node(f"While: {astor.to_source(node.test).strip()}", "diamond")
            if parent:
                mermaid.append(f"{parent} --> {cond}")
            for stmt in node.body:
                loop_node = walk(stmt, cond)
                mermaid.append(f"{cond} -->|Sim| {loop_node}")
            mermaid.append(f"{cond} -->|Não| {cond}_end")
            mermaid.append(f'{cond}_end["Fim While"]')
            return cond

        elif isinstance(node, ast.For):
            cond = new_node(f"For: {astor.to_source(node.target).strip()} in {astor.to_source(node.iter).strip()}", "diamond")
            if parent:
                mermaid.append(f"{parent} --> {cond}")
            for stmt in node.body:
                loop_node = walk(stmt, cond)
                mermaid.append(f"{cond} -->|Sim| {loop_node}")
            mermaid.append(f"{cond} -->|Não| {cond}_end")
            mermaid.append(f'{cond}_end["Fim For"]')
            return cond

        elif isinstance(node, ast.Expr):
            expr = new_node(astor.to_source(node).strip())
            if parent:
                mermaid.append(f"{parent} --> {expr}")
            return expr

        elif isinstance(node, ast.Assign):
            assign = new_node(astor.to_source(node).strip())
            if parent:
                mermaid.append(f"{parent} --> {assign}")
            return assign

        return parent

    for n in tree.body:
        walk(n)

    return "\n".join(mermaid)

def process_all_py_files():
    """Busca todos os arquivos .py e gera .mmd e .svg."""
    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.py'):
                full_path = os.path.join(dirpath, filename)
                with open(full_path, 'r', encoding='utf-8') as f:
                    try:
                        code = f.read()
                        mermaid_code = extract_mermaid_from_python_code(code)
                    except Exception as e:
                        print(f"❌ Erro ao processar {full_path}: {e}")
                        continue

                mmd_path = os.path.join(dirpath, f"{os.path.splitext(filename)[0]}.mmd")
                svg_path = os.path.join(dirpath, f"{os.path.splitext(filename)[0]}.svg")

                with open(mmd_path, 'w', encoding='utf-8') as f:
                    f.write(mermaid_code)
                print(f"✔️ {mmd_path} gerado.")

                try:
                    subprocess.run(["mmdc", "-i", mmd_path, "-o", svg_path], check=True)
                    print(f"✅ SVG salvo: {svg_path}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Falha ao gerar SVG para {mmd_path}: {e}")

if __name__ == '__main__':
    process_all_py_files()
