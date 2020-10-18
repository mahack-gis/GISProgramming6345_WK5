
#file = open('testWords.txt', 'r')
#f = file.readlines()

fin = open('words.txt')
fin.readline()
line = fin.readline()
word = line.strip()

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True







