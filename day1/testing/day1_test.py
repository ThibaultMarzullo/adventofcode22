import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import day1
import numpy as np

print("Generating a random list")
bearersoffood = np.random.randint(1, 100)
pocketdepth = [np.random.randint(1, 20) for i in range(bearersoffood)]
calorylist = [[str(np.random.randint(1, 100000)) for i in range(pocketdepth[j])] for j in range(bearersoffood)]
backpacks = [''.join([f"{line}\n" for line in block]) for block in calorylist]
handwritten = ''.join([f"{block}\n" for block in backpacks])[:-2]
print("Done.\n\n")
result, _ = day1.snacks(handwritten)
assert(isinstance(result, int))
print(f"\x1B[3mFor he had... {result} calories!\x1B[0m")