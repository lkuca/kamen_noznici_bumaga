
#mäng
import random
start = input('Olete käivitanud mängu "Kivi, paber, käärid". Kas sa tahad mängida? (Sisestage + või -): ')
if start == '+':
    print("Alustan...")
    print("lõppetan")
    print("et vaadata skoor sissesta c")
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Kivi, käärid või paber? (Sisestage kv, k või p): ")
        list_play = ['kv', 'k', 'p']
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'kv'and user == 'k':
              rand_ball += 1
            if rand == 'k' and user == 'kv':
               user_ball += 1
            if rand == 'k' and user == 'p':
               rand_ball += 1
            if rand == 'p' and user == 'kv':
               rand_ball += 1
            if rand == 'p' and user == 'k':
               user_ball += 1
            if rand == 'kv' and user == 'p':
               user_ball += 1
            if rand== 'kv' and user == 'kv':
               user_ball +=0
            if rand== 'p' and user == 'p':
               user_ball +=0
            if rand == 'k' and user == 'k':
               user_ball +=0
        elif user == 'с':
            print('Teie punktid - ', user_ball, '. Sinu vastase punktid - ', rand_ball, ".")
        elif user == '-':
            print('Teie punktid - ', user_ball, '. Sinu vastase punktid - ', rand_ball, ".")
            print('Mängu lõpp! Tule jälle!')
            break
        else:
            print('Sisestage kv, k või p')


           