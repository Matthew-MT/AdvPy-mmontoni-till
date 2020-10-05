import re, random, math

art = [
    "  __________",
    "  |/       |",
    "  O        |",
    " /|\       |",
    "  |        |",
    " / \       |",
    "__________/|",
    "| | | | | \|"
]

words = open("./words.txt").read().split("\n")

score = 0

guessed = []

class scoreboard:
    wins = 0
    losses = 0

totalScore = scoreboard()

cont = True

endChallenge = False

guess = ""

word = ""

spacer = "\n\n\n"

def printHangman(s):
    if s > 0:
        for line in art[0:s]:
            print(line)
        print("")

while cont:
    word = words[math.floor(random.random() * len(words))]
    guessed = ["_"] * len(word)
    score = 0
    endChallenge = False
    while not endChallenge:
        print(spacer)
        print("Hangman! Guess the word by inputting guesses as to what letters it contains.\n")
        printHangman(score)
        for c in guessed:
            print(c, end = " ")
        print("\n")
        guess = ""
        while len(guess) != 1 or re.search("[^a-zA-Z]", guess):
            guess = input("Input a one-letter guess: ")
        if guess in word and guess not in guessed:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            if "_" not in guessed:
                print(f"\nYou did it!\nThe word is {word}, and you didn't get hanged!")
                totalScore.wins += 1
                endChallenge = True
        else:
            if score < len(art) - 1:
                if guess not in guessed:
                    print("\nGood try! But wrong, unfortunately. Try again!")
                else:
                    print("\nYou already guessed that! I have to take points away for that.")
                score += 1
            else:
                print("\nYou lose! You ran out of guesses. I can't show you the word, that would be cheating.")
                printHangman(score + 1)
                totalScore.losses += 1
                endChallenge = True
    print(spacer)
    print(f"Current score:\n    Games won: {totalScore.wins}\n    Games lost: {totalScore.losses}"
        + f"\n    Percent of games won: {(totalScore.wins / (totalScore.wins + totalScore.losses)) * 100}%")
    print(spacer)
    cont = (input("Type \"y\" to keep playing or anything else to exit: ") == "y")