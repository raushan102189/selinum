with open("file.txt","r") as f:
    lists = f.readlines()
rog = []
for c in lists:
    word = c.splitlines()
    # print(word[0])
    rog.append(word[0])
print(rog)



