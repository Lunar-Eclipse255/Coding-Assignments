#Make a function to convert Celsius to Fahrenheit:
    #Do the math
    #return the answer
#Make a function to convert Fahrenheit to Celsius:
    #Do the math
    #return the answer
#Have an if and elif statement to ask if they want to convert from ºC to ºF or from ºF to ºC
#For each side of the conversion:
    #Ask for the number of the temperature they want converted
    #Take the number from the function
    #Have it print out their solution
conversion = int(input("What do you want to convert\n1.) From Celsius to Fahrenheit\n2.) From Fahrenheit to Celsius "))

def conversionCelsiusMath(numCelsius):
    answerCelsius= (numCelsius*(9/5))+32
    return(answerCelsius)

def conversionFahrenheitMath(numFahrenheit):
    answerFahrenheit= (numFahrenheit-32)/9*5
    return(answerFahrenheit)

if conversion ==1:
    numCelsius=float(input("What is the temperature? "))
    answerCelsius=conversionCelsiusMath(numCelsius)
    print(numCelsius,"ºC is",answerCelsius,"ºF")


elif conversion ==2:
    numFahrenheit=float(input("What is the temperature? "))
    answerFahrenheit=conversionFahrenheitMath(numFahrenheit)
    print(numFahrenheit,"ºF is",answerFahrenheit,"ºC")
