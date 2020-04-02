def opt(list_of_words):
    result = 0
    for word in list_of_words:
        result += len(word)**2
    return result

def f(text):
    list_of_words = []
    with open("words.txt") as words:
        for line in words:
            line = line[:-1]
            if line in text:
                if line != "":
                    list_of_words.append(line)
    length_of_longest = len(max(list_of_words, key=lambda s:(len(s), s)))
    possibilities = []

    def rec(rec_text):
        if rec_text == "":
            return ""
        for i in range(1, min(length_of_longest, len(rec_text))):
            if rec_text[0:i] in list_of_words:
                poss_of_rest = rec_text[0:i] + " " +  rec(rec_text[i:])
                possibilities.append(poss_of_rest)
        return rec_text      
    rec(text)
    print(possibilities)

f("tamatematykapustkinieznosi")