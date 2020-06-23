##list of time slots

TimeSlots = ['6:00 - 6:15', '6:15 - 6:30', '6:30 - 6:45', '6:45 - 7:00']

#for i in TimeSlots:
 #   displayCounter = i + 1
  #  print(i)

length = len(TimeSlots)
i = 0 
while i < length:
    displayCounter = i + 1
    print (str(displayCounter)+ "). " + TimeSlots[i])
    i +=1
#displayCounter = i + 1
 #   print (TimeSlots[i]) 
