import os.path
import sys


def check_comparison(item, item_to_check, exception_message):
    if item != item_to_check:
        raise ValueError(exception_message)


def txt_importer(path_file):
    try:
        with open(path_file, "r") as file:
            extension = os.path.splitext(path_file)[1]
            check_comparison(extension, ".txt", "Formato inválido")
            content = file.read().split(sep="\n")
            return content

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    except ValueError as exc_ext:
        print(exc_ext, file=sys.stderr)

    else:
        print("Importação realizada com sucesso", file=sys.stdout)
