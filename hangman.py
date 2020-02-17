from os import system
import random
import re
from pyfiglet import Figlet

allowed_chars = 'abcdefghkijklmnoprstuvz'
words_pool = []
template = ''
count = 0
tries = 5
used_letters = ''

# must have this file in root that contains words
inputfile = open('words.txt')
for line in inputfile:
    # remove newline char and add to list
    words_pool.append(line.rstrip())
inputfile.close()

f = Figlet(font='standard')

# picks a random wors from list at the begining of game
word = words_pool[random.randint(0, len(words_pool) - 1)]

# print out word with ________
for letter in range(0, len(word)):
    template += '_'

# lets put words 1st and last letter in template
temp = list(template)
temp[0] = word[0]
temp[-1] = word[-1]
template = ''.join(temp)

def game_title():
    system('cls')
    print(f.renderText('Vjesala'))

game_title()
print(f"Pokusaj pogoditi trazenu rijec\nZa svako krivo slovo gubis 1 bod\nKreces sa {tries} bodova!")
print("Utipkati exit za izlaz iz igre!")
print("\n")

print(f"Trazimo rijec od {len(word)} slova")
while tries > 0:
    print(f"Iskoristena slova: {used_letters}")
    print(template)
    print("\n")
    if tries == 0:
        game_title()
        print(f"GAME OVER\nNisi uspio!\nRijec koju smo trazili je bila: {word}")
        break
    if list(template).count('_') == 0:
        game_title()
        print(f"CONGRATZ!!\nPobijedio si!\nRijec koju si pogodio je bila: {word}")
        if tries == 3:
            print("!!!Savrseni rezultat!!!")
        else:
            print(f"trebalo ti je {count} pokusaja!")
            print(f"Preostalo ti je {tries} bodova")
        break
    guess = input("Utipkaj slovo: ")
    if guess == 'exit':
        game_title()
        print("Bye bye!")
        break
    elif len(guess) == 1:
        if guess in allowed_chars:
            count += 1
            used_letters += guess + ','
            if guess in word:
                for m in re.finditer(guess, word):
                    pos = m.start()
                    ltemp = list(template)
                    ltemp[pos] = guess
                    template = ''.join(ltemp)
                    game_title()
                    print("Bravo! pogodio si slovo")
                    print(f"Broj bodova: {tries}")
            else:
                game_title()
                tries -= 1
                print(f"Nema '{guess}', zalim gubis bod!")
                print(f"Broj bodova: {tries}")
                print("\n")
        else:
            game_title()
            print("Znak nije podrzan!")
    else:
        game_title()
        print('Samo jedno slovo dozvoljeno!')