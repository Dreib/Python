#file = open("books.txt", "w")
file = open("books.txt", "r")

#your code goes here
#file.write("Harry Potter")
#file.write("Game of Thrones")

txt = ""
cont = file.readlines()
for line in cont:
    words = line.split()
    for word in words:
        txt += word[0]
    print(txt)
    txt = ""

file.close()
