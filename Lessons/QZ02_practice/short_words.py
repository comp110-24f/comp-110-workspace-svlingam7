def short_words(input: list[str]) -> list[str]:
    """returns list of words that are shorter than 5 characters"""
    index: int = 0
    short_list: list[str] = []

    while index < len(input):
        if len(input[index]) < 5:
            short_list.append(input[index])
        else:
            print(f"{input[index]} is too long!")
        index += 1
    return short_list


weather: list[str] = ["sun", "cloud", "sky"]

print(short_words(weather))
