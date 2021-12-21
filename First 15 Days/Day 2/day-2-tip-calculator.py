#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

billTotal = float(input("What was the bill total? $"))
tipPercent = int(input("What % tip would you like to give? 12, 15, 18? "))
splitBetween = int(input("How many people to split the bill? "))
tipAmount = (tipPercent / 100) * billTotal

personalAmount = (billTotal + tipAmount) / splitBetween

print(f"Each person should pay: ${personalAmount:.2f}")