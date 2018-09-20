# file_pointer = open("speech.txt", "r", encoding="utf8")
#
# #text_list = file_pointer.readlines()
# #print(file_pointer.readline())
# print(file_pointer.readlines()) # read the files into a list of str

import csv # csv library that provides wrapper for csv file
with open("songs.csv", "r", encoding="utf8") as fp:
    csv_pointer = csv.reader(fp)
    print(csv_pointer)
    count = 0
    songs = []
    for song in csv_pointer:
        if count > 0: # if not header, append to new list with the right data type
            songs.append([song[0], song[1], int(song[2]), song[3], int(song[4])])
        count += 1
        #print(song)

    print("The total number of songs is: {}".format(count-1))

    print("The first ten songs are:")
    for i in range(10):
        print(songs[i]) # print out the first song details

    from operator import itemgetter # this is a library that can sort by any cols
    # sort the song according to song name, in the reverse manner.
    songs_sorted = sorted(songs, key=itemgetter(4), reverse=True)
    # default sorting for numeric starts from the smallest.
    print("The sorted first 10 songs:")
    for i in range(10):
        print(songs_sorted[i])

    # print the top ten songs into a file
    topTen = open("topTen.txt", "w", encoding="utf")
    for each in songs_sorted:
        topTen.write(str(each)+"\n")
    topTen.close()

