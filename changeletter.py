def move(word):
    num_2=""
    for i in word:
        num_2+=chr(ord(i)+1)
    return num_2
print(move("bye"))


