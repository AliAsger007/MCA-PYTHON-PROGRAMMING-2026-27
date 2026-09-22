number = 50

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct")
        break
    elif guess > number:
        print("Too High")
    else:
        print("Too Low")
