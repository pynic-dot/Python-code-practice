import random
import math

rnd_num = random.randint(1, 100)
num_guess = []


def outofgame():
    y = input("if you want to quit then press y , if not the n").upper()
    if y == 'Y':
        print(f'list of guesses {num_guess} and total number guesses  is {len(num_guess)} and the answer is {rnd_num}')
        return exit()

    else:
        pass


while True:
    num_gussed = int(input("Please Enter your guess: "))
    if num_gussed not in range(1, 100):
        print('Out of Bounds')
        outofgame()
        continue

    elif num_guess[::] == [] and math.isclose(rnd_num, num_gussed, abs_tol=10):
        print("Warm!")
        num_guess.append(num_gussed)
        outofgame()
        continue

    elif num_guess[::] == [] and math.fabs(rnd_num - num_gussed) not in range(1, 10):
        print("Cold!")
        num_guess.append(num_gussed)
        outofgame()
        continue

    elif math.isclose(rnd_num, num_gussed, abs_tol=10):
        print("Warmer!")
        num_guess.append(num_gussed)
        outofgame()
        continue

    elif math.fabs(rnd_num - num_gussed) not in range(1, 10):
        print("Colder!")
        num_guess.append(num_gussed)
        outofgame()
        continue
    elif rnd_num == num_gussed:
        print("Guessed Correct!")
        break

