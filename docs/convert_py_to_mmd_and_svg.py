# -*- coding: utf-8 -*-
import ast
import astor
import re
import subprocess

def clean_label(label):
    """
    Remove ou substitui caracteres especiais para compatibilidade com Mermaid.
    """
    label = re.sub(r"[{}\"\[\]<>]", "", label)   # remove chaves, colchetes, aspas, etc
    label = re.sub(r"\s+", " ", label)           # colapsa múltiplos espaços
    label = label.replace("\\", "")              # remove barras invertidas
    label = label.strip()
    return label

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

        else:
            return parent

    for n in tree.body:
        walk(n)

    return "\n".join(mermaid)

if __name__ == '__main__':
    input_py = "copy_files_to_non_empty_dirs.py"
    output_mmd = "copy_files_to_non_empty_dirs.mmd"
    output_svg = "copy_files_to_non_empty_dirs.svg"

    with open(input_py, "r") as file:
        codigo = file.read()

    mermaid_code = extract_mermaid_from_python_code(codigo)

    with open(output_mmd, "w") as f:
        f.write(mermaid_code)

    print(f"✔️ Arquivo Mermaid salvo como: {output_mmd}")

    # Executa o mmdc para gerar o SVG
    try:
        subprocess.run(["mmdc", "-i", output_mmd, "-o", output_svg], check=True)
        print(f"✅ Fluxograma gerado em: {output_svg}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao gerar SVG com mmdc: {e}")
