# -*- coding: utf-8 -*-
import ast
import astor
import re
import subprocess
import os

def clean_label(label):
    """
    Remove ou substitui caracteres especiais para compatibilidade com Mermaid.
    """
    label = re.sub(r"[{}\"\\\[\]<>]", "", label)  # Remove caracteres problemáticos
    label = re.sub(r"\s+", " ", label)            # Colapsa espaços múltiplos
    return label.strip()

def extract_mermaid_from_python_code(code_str):
    """
    Gera um fluxograma Mermaid simples a partir de um código Python.
    """
    tree = ast.parse(code_str)
    mermaid = ["graph TD"]
    node_counter = 0

    def new_node(label):
        nonlocal node_counter
        label = clean_label(label)
        node_id = f"N{node_counter}"
        node_counter += 1
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
            cond = new_node(f"If: {astor.to_source(node.test).strip()}")
            if parent:
                mermaid.append(f"{parent} --> {cond}")
            for stmt in node.body:
                walk(stmt, cond)
            for stmt in node.orelse:
                walk(stmt, cond)
            return cond

        elif isinstance(node, ast.For):
            target = astor.to_source(node.target).strip()
            it = astor.to_source(node.iter).strip()
            loop = new_node(f"For: {target} in {it}")
            if parent:
                mermaid.append(f"{parent} --> {loop}")
            for stmt in node.body:
                walk(stmt, loop)
            return loop

        elif isinstance(node, ast.While):
            test = astor.to_source(node.test).strip()
            loop = new_node(f"While: {test}")
            if parent:
                mermaid.append(f"{parent} --> {loop}")
            for stmt in node.body:
                walk(stmt, loop)
            return loop

        elif isinstance(node, ast.Expr):
            label = astor.to_source(node).strip()
            expr = new_node(label)
            if parent:
                mermaid.append(f"{parent} --> {expr}")
            return expr

        elif isinstance(node, ast.Assign):
            label = astor.to_source(node).strip()
            assign = new_node(label)
            if parent:
                mermaid.append(f"{parent} --> {assign}")
            return assign

        return parent

    for n in tree.body:
        walk(n)

    return "\n".join(mermaid)

def process_all_py_files():
    """
    Busca todos os arquivos .py a partir da raiz e gera um .mmd e .svg para cada um.
    """
    for dirpath, _, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.py'):
                full_path = os.path.join(dirpath, filename)

                # Lê o código-fonte
                with open(full_path, 'r', encoding='utf-8') as f:
                    try:
                        code = f.read()
                        mermaid_code = extract_mermaid_from_python_code(code)
                    except Exception as e:
                        print(f"❌ Erro ao processar {full_path}: {e}")
                        continue

                base_name = os.path.splitext(filename)[0]
                mmd_path = os.path.join(dirpath, f"{base_name}.mmd")
                svg_path = os.path.join(dirpath, f"{base_name}.svg")

                # Escreve o arquivo .mmd
                with open(mmd_path, 'w', encoding='utf-8') as f:
                    f.write(mermaid_code)
                print(f"✔️ {mmd_path} gerado.")

                # Tenta gerar o .svg com o mmdc
                try:
                    subprocess.run(
                        ["mmdc", "-i", mmd_path, "-o", svg_path],
                        check=True
                    )
                    print(f"✅ SVG salvo: {svg_path}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Falha ao gerar SVG para {mmd_path}: {e}")

if __name__ == '__main__':
    process_all_py_files()
