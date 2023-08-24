#Stealing my old code that counts the number of letter in a sentence and stores them
# add ha as a variable
#add a counter that takes the last word and the last word-1
#have it print it
word= input("Enter a word " )
x=len(word)

y=x-1
x2=(word[x:x+1])
y2=(word[y])
z=(word[0:x-1])
print(y2+x2+z+'ha')
