# -*- coding: utf-8 -*-

import os
import ast
import re
import astor
from pathlib import Path


def clean_identifier(text):
    """
    Remove ou substitui caracteres especiais para compatibilidade com Mermaid.
    """
    text = re.sub(r"[^\w]", "_", text)  # Mantém apenas letras, números e _
    return text


def parse_python_file(filepath):
    """Analisa um arquivo Python e retorna seu AST"""
    with open(filepath, "r", encoding="utf-8") as file:
        return ast.parse(file.read())


def get_function_and_class_defs(tree):
    """Extrai funções e classes do AST"""
    elements = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            elements.append(("function", node.name))
        elif isinstance(node, ast.ClassDef):
            elements.append(("class", node.name))

    return elements


def generate_mermaid_code(elements, filename):
    """Gera código Mermaid a partir das definições encontradas"""
    clean_name = clean_identifier(filename)
    lines = [f"classDiagram", f"class {clean_name} {{"]

    for element_type, name in elements:
        name = clean_identifier(name)
        prefix = "+" if element_type == "function" else "#"
        lines.append(f"    {prefix}{name}()")

    lines.append("}")
    return "\n".join(lines)


def write_mermaid_file(mermaid_code, output_path):
    """Escreve o arquivo .mmd"""
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(mermaid_code)


def convert_to_svg(mmd_path, svg_path):
    """Chama o mermaid-cli para converter .mmd em .svg"""
    os.system(f"mmdc -i \"{mmd_path}\" -o \"{svg_path}\" --quiet")


def process_python_file(file_path):
    print(f"📄 Processando: {file_path}")
    try:
        tree = parse_python_file(file_path)
        elements = get_function_and_class_defs(tree)
        if not elements:
            print(f"⚠️ Nenhum elemento detectado em {file_path}, pulando.")
            return

        filename = Path(file_path).stem
        mermaid_code = generate_mermaid_code(elements, filename)

        mmd_path = f"{file_path}.mmd"
        svg_path = f"{file_path}.svg"

        write_mermaid_file(mermaid_code, mmd_path)
        print("Generating single mermaid chart")
        convert_to_svg(mmd_path, svg_path)
        print(f"✅ SVG gerado: {svg_path}")
    except Exception as e:
        print(f"❌ Erro ao processar {file_path}: {e}")


def find_python_files(root="."):
    """Busca todos os arquivos .py recursivamente"""
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
