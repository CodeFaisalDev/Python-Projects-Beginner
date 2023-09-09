import random;

lower = int(input("Enter lower Bound"))
upper = int(input("Enter upper Bound"))

x = random.randint(lower, upper)
print("You have only have 10 chances");

count = 0

while(count < 10):
    count+1

    guess = int(input("Guess The Number"))

    if(guess == x):
        print("Hurray! You have guessed the Number")
        break;
    elif(guess < x):
        print("You have guessed to low. Try again!")

    elif(guess > x):
        print("You have guessed to high. Try again!")

if(count >= 10):
    print("You Loose")
    print("The number is: "% x)
