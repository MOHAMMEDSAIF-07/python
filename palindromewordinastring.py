string = "hi bro my level is high"
temp=string.split()
for word in temp:
    if word == word[::-1]:
        print(word)