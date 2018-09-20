file_pointer = open("speech.txt", "r", encoding="utf8")
print(file_pointer.read())
file_pointer.close()