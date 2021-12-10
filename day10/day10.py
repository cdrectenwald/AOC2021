with open('input.txt', 'r') as file:
  lines = file.readlines()
  lines = [line.rstrip() for line in lines]


SCORES = []
cost = 0
paren = {
  '(' : 1,
  '[': 1,
  '{' : 1,
  '<': 1 }
for line in lines:
    goodLine = True
    stack = []
    for c in line:
        if c in paren:
            stack.append(c)
        elif c==')':
            if S[-1] != '(':
                cost += 3
                goodLine = False
                break
            else:
                stack.pop()
        elif c==']':
            if S[-1] != '[':
                cost += 57
                goodLine = False
                break
            else:
                stack.pop()
        elif c=='}':
            if S[-1] != '{':
                cost += 1197
                goodLine = False
                break
            else:
                stack.pop()
        elif c=='>':
            if S[-1] != '<':
                cost += 25137
                goodLine = False
                break
            else:
                stack.pop()
    if goodLine:
      score = 0
      P = {'(': 1, '[': 2, '{': 3, '<': 4}
      for c in range(len(S)-1, -1, -1):
          score = score*5 + P[S[c]]
      SCORES.append(score)

SCORES.sort()
print(SCORES[len(SCORES)//2])
