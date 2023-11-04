name = ['']
verb = ['Stole', 'Robbed', 'Fought', 'Peed']
noun = ['Sweets', 'Bank', 'Truck', 'Stove']
from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words -1)
    word_picked = words[num_picked]
    return word_picked
print(pick(name), pick(verb), 'a', pick(noun), end='.\n')
while True:
    print(pick(name), pick(verb), 'a', pick(noun), end='.')
    input()
