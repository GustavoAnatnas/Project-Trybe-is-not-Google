import sys
import os
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for file in instance.get_queue():
        if file['nome_do_arquivo'] == path_file:
            print(f"Arquivo {path_file} já processado.")
            return False

    lines = txt_importer(path_file)
    metadata = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(metadata)
    print(metadata)


def remove(instance: Queue):
    if not instance:
        print("Não há elementos")
        return

    file_path = instance.dequeue()['nome_do_arquivo']
    try:
        os.remove(file_path)
        print(f"Arquivo {file_path} removido com sucesso")
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado")


def file_metadata(instance: Queue, position):
    try:
        metadata = instance.search(position)
        print(metadata, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
