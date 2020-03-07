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
    longest_word = max(list_of_words, key=len)

    def recu(string):
        counter = 0
        for i in range(min(len(string), len(longest_word))):
            if string[:i+1] in list_of_words:
                counter += 1
        if counter == 0:
            return ""
        for i in range(min(len(longest_word), len(string))):
            if string[:i] in list_of_words:
                return (string[:i+1] + recu(string[i+1:]))
        
    lista = recu(text)
    print(lista)
    



print(f("tamatematykapustkinieznosi"))