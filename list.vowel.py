vowels=['a','e','i','o','u']
word=input("enter any string:")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("the no.of diffrnt vowels present in",word,"is",len(found))
