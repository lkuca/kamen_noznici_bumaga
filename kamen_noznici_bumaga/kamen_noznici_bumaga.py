from pickle import APPEND
import random

r="rock" 
p="papper" 
s="scissors"
player1="player1"
player2="player2"
list=[r,p,s]

r>s 
p>r 
s>p 
results=[]
player1_ball = 0
player2_ball = 0
while True:
    random.shuffle(list)
    print(f"{player1},{list[0]}")
    res1 = list[0]
    random.shuffle(list)
    print(f"{player2},{list[0]}")
    res2 = list[0]


    if res1==r and res2==s:
        print("player1 won 1 point")
        player1_ball += 1
        results.append(player1)
    elif res1==s and res2==r:
        print("player2 won 1 point")
        player2_ball += 1
        results.append(player2)
    elif res1==r and res2==r:
        print("nobody recive point")
    elif res1==s and res2==s:
        print("nobody recive point")
    elif res1==p and res2==p:
        print("nobody recive point")
    elif res1==r and res2==p:
        print("player2 won 1 point")
        player2_ball += 1
        results.append(player2)
    elif res1==p and res2==r:
        print("player1 won 1 point")
        player1_ball += 1
        results.append(player1)
    elif res1==s and res2==p:
        print("player1 won 1 point")
        player1_ball += 1
        results.append(player1)
    elif res1==p and res2==s:
        print("player2 won 1 point")
        player2_ball += 1
        results.append(player2)
    show=input("show: ")    
    if show=="show":
        print(f"player1 points {player1_ball},player2 points {player2_ball},")
        

