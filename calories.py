calorieCount = {"Apple" : 105 , "Apricots" : 101 , "Bananas" : 105} #Creating dictionary
calories = 0 #initialise calories to 0
ch = ""
while(ch != "na"): #Run till value entered is na
    fruit = input("Please Enter the fruit name : ") #Take user input
    if(fruit == "na"):
        # for fruits in calorieCount.keys():
                # if(fruit == fruits):
                    # calorieCount[fruit] += calories * number
        break #break the loop is value is na
    number = int(input("Please enter the number of times you ate " + fruit + " : "))
    for fruits in calorieCount.keys():
            if(fruit == fruits):
                calories += calorieCount[fruit] * number #add the calorie values with the Fruit
print("Calories are : " + str(calories)) #print the total calories
