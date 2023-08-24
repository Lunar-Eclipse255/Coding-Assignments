#Imports random generator and OS:
import random
import os

#Opens file with the words:
file = open("Python/Wordle/Wordle.txt","r")

#Defines the variables and Lists:
fileList=list()
counter=0
counter2=0
randWord=list()
solutionList=[]
solutionList2=['-','-','-','-','-']
alphabetList=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Functions:
#Makes a function to get a random word
def y():
    import random
    num=random.randint(0,5756)
    return(num)

#Code:
#Turns the file given to us into a list called fileList
for x in (file):
    fileList.append(x.rstrip().upper())
file.close()
#Prints and says instructions
print("Enter a 5 letter word \n","If the letter is capitalized it is in the correct place\n","If a letter is lower case in the alphabet list that letter is in the generated word but in the wrong place \n If the letter is dashed out in the alphabet it is not in the word")
os.system("say Enter a 5 letter word. If the letter it is in the correct place. If a letter is lower case in the alphabet list that letter is in the generated word but in the wrong place. If the letter is dashed out in the alphabet it is not in the word")
#Pulls the random word from the function setting it equal to a variable
randWordNum=y()
randWord=fileList[randWordNum]
#Has a while loop that goes through all five letters in the words
while counter2<5:
    #Gets a user input
    userWord=input("Enter a word ").upper()
    #Goes through the letters in the user word
    for a in userWord:

        #If its there adds the letter capitalized to the dashed list
        if randWord[counter]==userWord[counter]:
            solutionList.append(a)
            counter2=counter2+1

        #If its in the word but not in the right place adds a lower case version to the alphabet list
        elif userWord[counter] in randWord:
            solutionList.append('-')
            for d in range(len(alphabetList)):
                if a == alphabetList[d]:
                    alphabetList[d]=alphabetList[d].lower()
        #If its not there adds a dash to the alphabet list
        elif userWord[counter] != randWord :
            solutionList.append('-')
            for c in range(len(alphabetList)):

                if a == alphabetList[c]:
                    alphabetList[c]='-'




        counter=counter+1
#Resests counter 2 to zero if its not equal to five so the code doesn't break
    if counter2!=5:
        counter2=0
#Prints the dashed list and alphabet list
    print(solutionList)
    print(alphabetList)
    solutionList=[]
    counter=0


#If you get all the letters prints and says You win
print("You Win")
os.system("say You Win")
