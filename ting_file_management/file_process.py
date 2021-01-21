from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance:
        if item["nome_do_arquivo"] == path_file:
            return
    result = txt_importer(path_file)
    returned_object = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(result),
        "linhas_do_arquivo": result,
    }
    instance.enqueue(returned_object)
    print(returned_object)


def remove(instance):
    try:
        item = instance.dequeue()
        print(f"Arquivo {item['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        print(item)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
