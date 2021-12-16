'''
lines = []
folds = []
maxY = 0
maxX = 0
problem1 = True
graph1 = {}
graph2 = {}

origString = []
pairDict = {}
for line in  open('input.txt', 'r'):
  line = line.strip().split('->')

  if len(line) == 1:
    origString.append(line)
    origString = origString[0]
  else:
    pairDict[line[0].strip()] = line[1].strip()
print(pairDict)



steps = 0
print(origString)
'''
'''
while steps < 40:
  newString = ""

  for i in range(0, len(origString)-1):

    if origString[i:i+2] in pairDict:
      newString += origString[i]
      newString += pairDict[origString[i:i+2]]
    if i == len(origString)-2:
      newString += origString[i+1]

  steps += 1
  origString = newString
'''


print(origString)
from collections import Counter
freqCounter =  Counter(origString)
print(max(freqCounter.values())-min(freqCounter.values()))




S, rules = open("input.txt").read().split('\n\n')

R = {}
for line in rules.strip().split('\n'):
    start,end = line.strip().split(' -> ')
    R[start] = end

# Keep track of *counts* of each pair of letters
# C1 = {pair of characters: count of that pair}
C1 = Counter()
for i in range(len(S)-1):
    C1[S[i]+S[i+1]] += 1

for t in range(41):
    if t in [10,40]:
        CF = Counter()
        for k in C1:
            CF[k[0]] += C1[k]
        CF[S[-1]] += 1
        print(max(CF.values())-min(CF.values()))

    # If AB->R, then AB becomes (AR, RB)
    C2 = Counter()
    for k in C1:
        C2[k[0]+R[k]] += C1[k]
        C2[R[k]+k[1]] += C1[k]
    C1 = C2
