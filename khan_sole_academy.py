import random
# this line is to generate anything random.
x=random.randint(10,99)
y=random.randint(10,99)
a=x+y
#this is to assign the random numbers to the variables and also the sum of those random numbers.
count=1
# this line is to assign a variable to one
while count<=3:
# this shows the condition of the number of times there should repitition
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    a = x + y
#this is to assign the random numbers to the variables and also the sum of those random numbers.
    q = print("What is", x, "+", y, "?")
    #this is to ask the user the addition question
    u = int(input("Answer: "))
    # this is allow the user answer the question
    if u==a:
        print("Correct!! You've gotten",count, "times in a row")
        count +=1
    else:
        count=1
        print("Incorrect. The expected number was",a)
print('congrats, you mastered Addition')
# the above is to specify the conditions for the input and also display the information associated with each condition
