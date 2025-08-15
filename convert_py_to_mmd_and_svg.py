# -*- coding: utf-8 -*-
import ast
import astor
import re
import os
from pathlib import Path
import subprocess

def clean_label(label):
    """
    Remove caracteres especiais e simplifica labels.
    """
    label = re.sub(r"[^\w\s:=><\-\+\*/]", "", label)
    label = re.sub(r"\s+", " ", label)
    return label.strip()

def generate_mermaid_from_ast(code_str):
    """
    Gera código Mermaid flowchart a partir de código Python.
    """
    tree = ast.parse(code_str)
    lines = ["flowchart TD"]
    node_counter = 0

    def new_node(label, shape="rect"):
        nonlocal node_counter
        node_id = f"n{node_counter}"
        label = clean_label(label)
        if shape == "diamond":
            lines.append(f'{node_id}{{"{label}"}}')
        elif shape == "parallelogram":
            lines.append(f'{node_id}[/"{label}"/]')
        else:
            lines.append(f'{node_id}["{label}"]')
        node_counter += 1
        return node_id

    def walk(node, parent=None):
        if isinstance(node, ast.FunctionDef):
            current = new_node(f"Func: {node.name}()", "rect")
            if parent:
                lines.append(f"{parent} --> {current}")
            last = current
            for stmt in node.body:
                last = walk(stmt, last)
            return current

        elif isinstance(node, ast.If):
            cond = new_node(f"If: {astor.to_source(node.test).strip()}", "diamond")
            if parent:
                lines.append(f"{parent} --> {cond}")
            last_true = cond
            for stmt in node.body:
                last_true = walk(stmt, cond)
            last_false = cond
            for stmt in node.orelse:
                last_false = walk(stmt, cond)
            return cond

        elif isinstance(node, ast.While):
            cond = new_node(f"While: {astor.to_source(node.test).strip()}", "diamond")
            if parent:
                lines.append(f"{parent} --> {cond}")
            for stmt in node.body:
                walk(stmt, cond)
            return cond

        elif isinstance(node, ast.For):
            label = f"For: {astor.to_source(node.target).strip()} in {astor.to_source(node.iter).strip()}"
            loop = new_node(label, "diamond")
            if parent:
                lines.append(f"{parent} --> {loop}")
            for stmt in node.body:
                walk(stmt, loop)
            return loop

        elif isinstance(node, ast.Assign):
            assign = new_node(astor.to_source(node).strip(), "rect")
            if parent:
                lines.append(f"{parent} --> {assign}")
            return assign

        elif isinstance(node, ast.Expr):
            expr = new_node(astor.to_source(node).strip(), "rect")
            if parent:
                lines.append(f"{parent} --> {expr}")
            return expr

        return parent

    for n in tree.body:
        walk(n)

    return "\n".join(lines)


def process_python_file(file_path):
    print(f"📄 Processando: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        mermaid_code = generate_mermaid_from_ast(code)

        if mermaid_code.strip() == "flowchart TD":
            print(f"⚠️ Nenhum elemento detectado em {file_path}, pulando.")
            return

        mmd_path = f"{file_path}.mmd"
        svg_path = f"{file_path}.svg"

        with open(mmd_path, "w", encoding="utf-8") as f:
            f.write(mermaid_code)

        print("Generating single mermaid chart")
        subprocess.run(["mmdc", "-i", mmd_path, "-o", svg_path, "--quiet"], check=True)
        print(f"✅ SVG gerado: {svg_path}")
    except Exception as e:
        print(f"❌ Erro ao processar {file_path}: {e}")


def find_python_files(root="."):
    py_files = []
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.endswith(".py"):
                py_files.append(os.path.join(dirpath, file))
    return py_files


if __name__ == "__main__":
    print("🔍 Procurando arquivos .py...")
    py_files = find_python_files()
    for py_file in py_files:
        process_python_file(py_file)
