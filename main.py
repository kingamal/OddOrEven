print('What number are you thinking?')
number = int(input())
while number:
    if number >=1 and number <= 1000:
        if number % 2 != 0:
            print("That's an odd number! Have another?")
            number = int(input())
        elif number % 2 == 0:
            print("That's an even number! Have another?")
            number = int(input())
        else:
            print("Thanks for playing")
    else:
        print("That's a wrong number! Try it again")