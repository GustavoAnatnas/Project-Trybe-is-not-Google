import os
import sys


def txt_importer(path_file):
    file_extension = os.path.splitext(path_file)[1]

    if file_extension != '.txt':
        print("Formato inválido", file=sys.stderr)
        return []

    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    with open(path_file, 'r') as file:
        lines = [line.strip() for line in file]
        return lines
