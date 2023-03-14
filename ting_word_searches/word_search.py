def exists_word(word, instance):
    occurrences = []
    for item in instance.get_queue():
        found_occurrences = []
        for line_number, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                found_occurrences.append({"linha": line_number})

        if found_occurrences:
            occurrences.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": found_occurrences
            })

    return occurrences


def search_by_word(word, instance):
    occurrences = []
    for item in instance.get_queue():
        found_occurrences = []
        for j, line in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                found_occurrences.append({"linha": j, "conteudo": line})

        if found_occurrences:
            occurrences.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": found_occurrences
            })

    return occurrences
