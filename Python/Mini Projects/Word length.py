word= input("Enter a word " )
x=len(word)
print("Your word is ",x,"letters long")

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
