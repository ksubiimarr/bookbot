def get_books_text(filepath):
    with open(filepath) as x:
        return x.read()

def num_of_words(text):
    count = 0
    list_of_words = text.split()
    for i in list_of_words:
        count += 1
    return count

def count_chars(text):
    dict = {}
    lower = text.lower()
    for i in lower:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def helper(dic):
    return dic["num"]

def sort(dick):
    listt = []
    for i in dick:
        listt.append({"char": i, "num": dick[i]})
    listt.sort(reverse=True, key=helper)
    return listt

