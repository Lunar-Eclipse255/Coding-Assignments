#The instructions were unclear nad because of this I made code that has the user input 2 words and then compare their length




word= input("Enter a word " )

x=len(word)
for X in range(x):
    print(word[X])
print("Your word is ",x,"letters long")
word2= input("Enter another word " )
x = int(x)
y=len(word2)
for Y in range(y):
    print(word2[Y])
print("Your word is ",y,"letters long")
y = int(y)

better=x-y
if better>=0:
    print("Your first word is ",better, " character longer than your second word")
else:
    print("Your second word is ",better*-1, " character longer than your first word")
x = str(x)
letter = word[1]
text="Give a number less than or equal to " + str(x) + " "
letter=input(text)

x = int(x)
letter = int(letter)
if letter>x:
    print("That number is too high")

else :
    w=word[letter-1]
    print(w)
