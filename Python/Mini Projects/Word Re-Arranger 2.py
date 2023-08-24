#Stealing my old code that counts the number of letter in a sentence and stores them
#All words should be made uppercase
#Find all the places where vowel is by:
#adding a while loop which adds a counter
#have a if statement looking for values
# do word maniplation with code such as finding it, assigning it to the number it is in the string by adding to the counter than taking that number value than replacing it with e
# look if the last later is an s
#if so take away the s and replace it with a y by taking ou tthe last letter if it is an s then in that lst number spot replace it with a y.
# take my code from the previous project on ho wto take the last word and bring it to the front

answer= input("Enter a word " )


x=len(answer)
for X in range (x):

    if answer[X] == 'a':

        where = X
        part1=answer[0:where]
        part2=answer[where+1:x]
        part1=str(part1)
        part2=str(part2)
        answer=part1 + "e" + part2
        print(answer)

    elif answer[X] == 'i':

        where = X
        part1=answer[0:where]
        part2=answer[where+1:x]
        part1=str(part1)
        part2=str(part2)

        answer=part1 + "e" + part2
        print(answer)
    elif answer[X] == 'o':

        where = X
        part1=answer[0:where]
        part2=answer[where+1:x]
        part1=str(part1)
        part2=str(part2)

        answer=part1 + "e" + part2
        print(answer)
    elif answer[X] == 'u':

        where = X
        part1=answer[0:where]
        part2=answer[where+1:x]
        part1=str(part1)
        part2=str(part2)

        answer=part1 + "e" + part2
        print(answer)
    elif answer[X] == 'y':

        where = X
        part1=answer[0:where]
        part2=answer[where+1:x]
        part1=str(part1)
        part2=str(part2)

        answer=part1 + "e" + part2
        print(answer)

if answer[x-1] =='s':
    part3=answer[0:x-1]
    part4=answer[x:x+1]
    answer= part3 + "y" + part4

print(answer)
part5=answer[0:1]
part6=answer[1:]
answer = part6 + part5
print(answer)
answer=answer.upper()
print(answer)
