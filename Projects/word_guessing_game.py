import random
import math
name=input("Enter Your Name")

print("Ok!That's Nice {} !! All The Best".format(name))

def inputInt(text):  #Function for the numbers..
    while True:
        try:
            num=int(input(text))
            return num
        except ValueError as e:
            print("Please Enter Valid input")



lower_bound=inputInt("Enter Your Lower Bound")
upper_bound=inputInt("Enter Your Upper Bound")
guess=round(math.log2(upper_bound-(lower_bound+1)))
random_number=random.randint(lower_bound,upper_bound)
print(f'The Random Number {lower_bound} and {upper_bound} has been generated')
print(f"you have {guess} No of chances to guesss the number!All The Best")

count=0

print(f"checking test case {random_number}")
while guess>count:
    num=inputInt("Enter Number To Guess")
    if num<lower_bound or num>upper_bound :
        print("You Have Entered Wrong Number ")
        continue
    elif num<random_number :
        print("Your Number is Less Than The Guessing Number")
    elif num>random_number :
        print("your number is greater than the Guessing number")
    elif(num==random_number):
        print("You Guessed Right Number")
        break
    count=count+1

    val=guess-count
    print(f"you left the  {val}  guess the number!!")
    if count>=guess :
        print(f"the original number is {random_number}")
        print("Better Luck Next Time")

