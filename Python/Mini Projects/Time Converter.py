#Assignment 2
firstTime=int(input("Convert seconds to minutes and hours "))
hourTime=firstTime/3600
hourTimeExtra=hourTime%1
realHourTime=int(hourTime-hourTimeExtra)
minuteTime=hourTimeExtra*60
minuteTimeExtra=minuteTime%1
realMinuteTime=int(minuteTime-minuteTimeExtra)

secondTime=minuteTimeExtra*60
secondTimeExtra=secondTime%1
realSecondTime=int(secondTime-secondTimeExtra)
print("That will be ",realHourTime, "hours,", realMinuteTime, "minutes and approximately ", realSecondTime, "seconds.")
