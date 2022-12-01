import sys
# Count how many calories worth of food each Elf is carrying

def snacks(calorylist:str, onetime=True):
    noblanks = calorylist.split('\n\n')
    strlists = [sublist.split('\n') for sublist in noblanks]
    intlists = [[int(item) for item in sublist] for sublist in strlists]
    sums = [sum(intlist) for intlist in intlists]
    calories = max(sums)
    whogotit = sums.index(calories)
    if onetime:
        print(f"\x1B[3mAnd they all looked upon Elf {whogotit} with hunger...\x1B[0m")
    return calories, sums

def topsnackers(calorylist:str, howmany=3):
    calories, sums = snacks(calorylist, onetime=False)
    targets = []
    for i in range(howmany):
        print(f"\033[1;3m{'So the leader' if i==0 else '...and then he'} asked who was the most loaded Elf {i+1} time{'' if i==0 else 's'}...\033[0m")
        targets.append(max(sums))
        print(f"\x1B[3mIt was Elf {sums.index(max(sums))}...\x1B[0m")
        sums.pop(sums.index(max(sums)))
    
    print(f"\x1B[3mThey had a total of {sum(targets)} calories!\x1B[0m")
    return sum(targets)

def main(wheresthelist='input.txt', num=3):

    print(f"\033[1;3mThey eventually became hungry.\nThe leader wondered which Elf was carrying the most snacks. \033[0m")

    with open(wheresthelist, 'r') as heresthelist:
        snacklist = heresthelist.read()
    cals, _ = snacks(snacklist)
    print(f"\x1B[3mFor he had... {cals} calories!\x1B[0m")

    print(f"\033[1;3m'But...' one voice said, 'should we not ask for the top {num} carriers instead?\nThey all agreed.\033[0m")
    topsnackers(snacklist)

    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(wheresthelist=sys.argv[1])
    else:
        main()