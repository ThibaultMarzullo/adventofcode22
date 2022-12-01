# Count how many calories worth of food each Elf is carrying

def snacks(calorylist:str):
    noblanks = calorylist.split('\n\n')
    strlists = [sublist.split('\n') for sublist in noblanks]
    intlists = [[int(item) for item in sublist] for sublist in strlists]
    sums = [sum(intlist) for intlist in intlists]
    calories = max(sums)
    whogotit = sums.index(calories)
    print(f"\x1B[3mAnd they all looked upon Elf {whogotit} with hunger...\x1B[0m")
    return calories