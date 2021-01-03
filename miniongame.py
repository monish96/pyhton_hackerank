from collections import Counter

def minion_game(string):
    # your code goes here
    # result = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
    # counts = Counter(result)
    vowels = 0
    consonants = 0
    the_vowel = ["A", "E", "I", "O", "U"]
    for i in range(len(string)):
        print((len(string) ,  i))
        if string[i] in the_vowel:
            print('>>>>', (len(string), i))
            vowels += (len(string)-i)
        else:
            consonants += (len(string)-i)
    if vowels == consonants:
        print('Draw')
    elif vowels > consonants:
        print('Kevin {0}'.format(vowels))
    elif vowels < consonants:
        print('Stuart {0}'.format(consonants))

if __name__ == '__main__':
    s = input()
    minion_game(s)
