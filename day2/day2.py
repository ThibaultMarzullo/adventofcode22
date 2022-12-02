
import sys

def cheat(papernote):
    with open(papernote, 'r') as forbiddenknowledge:
        datruth = forbiddenknowledge.readlines()
    return datruth

def play(moves):
    theothermove, yourmove = moves.strip().split(' ', 1)
    decrypt = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'
    }
    therulesbutyoucheat = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }
    if decrypt[yourmove] == decrypt[theothermove]:
        return decrypt[yourmove], 'Draw'
    elif decrypt[theothermove] == therulesbutyoucheat[decrypt[yourmove]]:
        return decrypt[yourmove], 'Win'
    else:
        return decrypt[yourmove], 'Lose'

def playagain(moves):
    theothermove, theoutcome = moves.strip().split(' ', 1)
    decrypt = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Lose',
        'Y': 'Draw',
        'Z': 'Win'
    }
    tolose = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }
    towin = {
        'Rock': 'Paper',
        'Paper': 'Scissors',
        'Scissors': 'Rock'
    }
    if decrypt[theoutcome] == 'Win':
        return towin[decrypt[theothermove]], 'Win'
    elif decrypt[theoutcome] == 'Draw':
        return decrypt[theothermove], 'Draw'
    else:
        return tolose[decrypt[theothermove]], 'Lose'

def score(move, outcome):
    scoring = {
        'Rock': 1,
        'Paper': 2,
        'Scissors': 3,
        'Lose': 0,
        'Draw': 3,
        'Win': 6
    }
    return scoring[move] + scoring[outcome]

def main(encryptednote):
    
    print("\x1B[3mEveryone sat down, and they started to wonder... Would the best spot not be closer to the snacks?\x1B[0m")
    print("\033[1;3mAnd suddenly, from afar, the drums of battle started chanting.\nFor there was going to be a Rock, Paper Scissors tournament!\033[0m")
    print("\n\nYou feel someone slipping a note in your pocket...")

    dafuture = cheat(encryptednote)

    print(f"...\n...\n...\nThe note gives all of your opponents' {len(dafuture)} moves for the RPS tournament!")
    print("You realize the immense power of this note. You look at it thoughtfully.")
    corruption = None
    while corruption != 'y' and corruption != 'n':
        corruption = input("Do you keep it? [y/n]")
    if corruption == 'y':
        print(f"\x1B[3m'Heh, isn't that, isn't that odd though?' you thought, 'Yet, after all why not? Why shouldn't I keep it?'\x1B[0m")
        finalscorebutyoucheat = 0
        for thisround in dafuture:
            move, outcome = play(thisround)
            finalscorebutyoucheat += score(move, outcome)
        print(f"\x1B[3mIf I played these moves, I would get...\x1B[0m")
        print(f"{finalscorebutyoucheat} points!")

        print(f"\x1B[3mAs you count your points, a voice whispers in your ear. 'That is not what the note says, I mean, can you not read encrypted messages properly?'\x1B[0m")
        print(f"\x1B[3mYou read the note again. 'Ah, of course!'\x1B[0m")

        finalscorebutyoucheatagain = 0
        for thisround in dafuture:
            move, outcome = playagain(thisround)
            finalscorebutyoucheatagain += score(move, outcome)
        print(f"\x1B[3mIf I played these moves, I would get...\x1B[0m")
        print(f"{finalscorebutyoucheatagain} points!")
        
        print("And so, you played the game, knowing very well that you were breaking the trust that the Elves had in you. Could you live with yourself after you rigged this Rock, Paper, Scissors tournament? What will the consequences be?")
    else:
        print("Your soul is pure! However, you really suck at Rock Paper Scissors. You lose all rounds and end up in the tent furthest from the snacks.\nYou die of starvation.")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an input file./nUsage:/n\tpython3 day2.py path/to/your/input")
    main(sys.argv[1])