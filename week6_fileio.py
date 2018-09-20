file_pointer = open("speech.txt", "r", encoding="utf8")

#text_list = file_pointer.readlines()
print(file_pointer.readline())
print(file_pointer.readline())
file_pointer.close()