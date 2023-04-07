def filter(words, letter):
    return [word for word in words if word.startswith(letter)]

words = ["дурка", "бгк", "бийск", "собака", "обь", "дурдом", "дота2", "дарья"]
letter = "д"
result = filter(words, letter)
print("Список слов, которые начинаются на букву Д:", result)  