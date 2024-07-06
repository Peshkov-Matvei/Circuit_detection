def match_elements(recognized_elements, database):
    matches = []
    for element in recognized_elements:
        match = database.get(element['name'], None)
        if match:
            matches.append(match)
    return matches


if __name__ == "__main__":
    recognized_elements = [{"name1": "Авт. выкл. 3P 16А"}, {"name2": "Авт. выкл. 3P 63А"}]
    database = { "Авт. выкл. 3P 16А": 1, "Авт. выкл. 3P 63А": 2 }
    matches = match_elements(recognized_elements, database)
    print(matches)
