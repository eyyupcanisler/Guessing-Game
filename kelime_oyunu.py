def PrintGameIntro():
    print("****WELCOME TO THE GUESSING GAME****")
    print('''
    The goal of this game to find the computer generated random number in several guesses.
    The user first should determine the range for generating the random number.
    Lower limit should be higher than or equal to 0.
    Upper limit should be lower than or equal to 100.
    For any entry outside the 0-100, the program should keep asking users for valid values.  
    After the limits are defined, the random number should be generated within these limits.
    For example, if the user enters 5 and 15 as the limits, the random number to be guessed would be between 5-15 (including 5 and 15).

    Depending on the range, the number of guesses that user can make will change, as shown below:
    \trange < 0-9: 2 guesses,
    \trange btw 10-19\t: 4 guesses,
    \trange btw 20-39\t: 6 guesses,
    \trange btw 40-100\t: 8 guesses,

    If the guess is too far (that is, the difference is bigger than or equal to 10), 
    the program should print 'Go up a lot' or 'Go down a lot'.

    If the guess is close (that is, the difference is less than 10), 
    the program should print 'Go up a bit' or 'Go down a bit'.

    At each guess, the number of remaining guesses should be displayed.

    If the user guesses the number correctly, the program should print a success message and terminate.

    If the user consumes all guesses and cannot get it correctly, the program should print a failure message and terminate.

    ''')
def GetTheLimits(count):
    high_err = False;
    low_err = False;
    if (count == 0):
        low = int(input('Lower limit: '))
        high = int(input('Higher limit: '))
    else:
        if (high_err):
            high = int(input('Higher limit: '))
        if (low_err):
            low = int(input('Lower limit: '))
    if (high > 100):
        print("Error! Upper limit should be equal to or less than 100\n")
        high_err = True
        GetTheLimits(count)
    if (low < 0):
        print("Error! Upper limit should be equal to or bigger than 0.\n")
        low_err = True
        GetTheLimits(count)

    if (low >= high):
        print("Error! Upper limit should be higher than lower limit.\n")
        low_err = True
        high_err = True
        GetTheLimits(count)

    count += 1
    return low, high
import random

def outPut(lowerLimit, higherLimit):
    answer = random.randint(lowerLimit, higherLimit)
    return answer

def RangeGuessNumber(lo, hi):
    if (hi-lo >= 0 and hi-lo <= 9):
        MaxNumber = 2
    if (hi-lo >= 10 and hi-lo <= 19):
        MaxNumber = 4
    if (hi-lo >= 20 and hi-lo <= 39):
        MaxNumber = 6
    if (hi-lo >= 40 and hi-lo <= 100):
        MaxNumber = 8
    return MaxNumber

def guess(CorrectAns, MaxRangeNumber, gnumber):
    if (gnumber < MaxRangeNumber):
        user_guess = int(input("Write a value: "))
        if (user_guess - CorrectAns == 0):
            print("Your Answer is True!")
        else:
            if (user_guess - CorrectAns <= -10):
                print("Go up a lot.")
                gnumber += 1
                RemainingGuess = MaxRangeNumber - gnumber
                print("Remaining guess: ", RemainingGuess)
                guess(CorrectAns, MaxRangeNumber, gnumber)
            if user_guess - CorrectAns >= 10:
                print("Go down a lot.")
                gnumber += 1
                RemainingGuess = MaxRangeNumber - gnumber
                print("Remaining guess: ", RemainingGuess)
                guess(CorrectAns, MaxRangeNumber, gnumber)
            if user_guess - CorrectAns < 0 and user_guess - CorrectAns > -10:
                print("Go up a bit.")
                gnumber += 1
                RemainingGuess = MaxRangeNumber - gnumber
                print("Remaining guess: ", RemainingGuess)
                guess(CorrectAns, MaxRangeNumber, gnumber)
            if user_guess - CorrectAns > 0 and user_guess - CorrectAns < 10:
                print("Go down a bit.")
                gnumber += 1
                RemainingGuess = MaxRangeNumber - gnumber
                print("Remaining guess: ", RemainingGuess)
                guess(CorrectAns, MaxRangeNumber, gnumber)
    else:
        RemainingGuess = 0
        print("You have reached your maximum guess. Game is over!")

        return gnumber


PrintGameIntro()
lowLim, highLim = GetTheLimits(0)
CompAnswer = outPut(lowLim, highLim)
MaximumRangeNumber = RangeGuessNumber(lowLim, highLim)
RangeGuess = guess(CompAnswer, MaximumRangeNumber,0)