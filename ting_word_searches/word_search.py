def exists_word(word, instance):
    found_lines_by_file = []
    for file_processed in instance:
        find_by_file = {
            "palavra": word,
            "arquivo": file_processed["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, line in enumerate(
                    file_processed["linhas_do_arquivo"]
                )
                if word.lower() in line.lower()
            ],
        }
        if len(find_by_file["ocorrencias"]):
            found_lines_by_file.append(find_by_file)
    return found_lines_by_file


def search_by_word(word, instance):
    found_lines_by_file = []
    for file_processed in instance:
        find_by_file = {
            "palavra": word,
            "arquivo": file_processed["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1, "conteudo": line}
                for index, line in enumerate(
                    file_processed["linhas_do_arquivo"]
                )
                if word.lower() in line.lower()
            ],
        }
        if len(find_by_file["ocorrencias"]):
            found_lines_by_file.append(find_by_file)
    return found_lines_by_file
