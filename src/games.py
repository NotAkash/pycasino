#Menu Option:

#Load Files
import time
import random
import sys

#Import Local Files
while True:                         # This is used in case games.py is ran locally
    try:                            #and not ran from casino.py
        from src.play import *
        from src.gamesplayed import *
        from src.start import start_game
    except ModuleNotFoundError:
        from play import *
        from gamesplayed import *
        from start import start_game
        break
    else:
        break

#Find Balance

def balance(user):
    return player_cont(user)


#Slot Machine


def slots(bet):
    ngame("slots")
    print("Welcome To The Slot Machines")
    print("Here, We Have A Varied Level Of Dificulties And Winnings")
    #Get time for pseudorandom variables
    print("     Win By Getting 3 Of The Same Number")
    print("     Tie By Getting 2 Of The Same Number")
    print("1= 02.50  X Gamble ||| 25% Chance Of Winning")
    print("2= 04.00  X Gamble ||| 23% Chance Of Winning")
    print("3= 05.00  X Gamble ||| 14% Chance Of Winning")
    print("4= 07.50  X Gamble ||| 10% Chance Of Winning")
    print("5= 10.00  X Gamble ||| 06% Chance Of Winning")
    print("--------  -------- ||| 34% Chance Of Losings")
    print("-- 01.00  X Gamble ||| 66% Chance Of Neither")
    #winning vars:
    print("")
    input("")
    rnum=[]
    vnum=[]                 
    num= random.randint(1,60)
    rnum.append(num)                              #Get 3 Random Ints from 1,60
    num= random.randint(1,60)                     #Append Them To List
    rnum.append(num)
    num= random.randint(1,60)
    rnum.append(num)

    d_game1= random.randint(5,7)
    d_game2= random.randint(11,14)
    d_game3= random.randint(19,23)
    for i in rnum:
        if gplayed("slots")%d_game1==0 and gplayed("slots")%d_game2!=0 and gplayed("slots")%d_game3!=0:
            vnum.append(random.randint(1,2))
        elif gplayed("slots")%d_game2==0 and gplayed("slots")%d_game3!=0:
            vnum.append(random.randint(2,4))
        elif gplayed("slots")%d_game3==0:
            vnum.append(random.randint(4,5))
        else:
            
            if i%2==0 and i%4!=0 and i%6!=0 and i%10!=0 and i%12!=0 and i%20!=0:
                vnum.append(1)
            elif i%3==0 and i%6!=0 and i%12!=0 and i%15!=0:
                vnum.append(1)
            elif i%4==0 and i%12!=0 and i%20!=0:
                vnum.append(1)
            elif i%5==0 and i%10!=0 and i%15!=0 and i%20!=0:
                vnum.append(3)
            elif i%6==0 and i%12!=0:
                vnum.append(4)
            elif i%10==0 and i%20!=0:
                vnum.append(5)
            elif i%12==0:
                vnum.append(4)
            elif i%15==0:
                vnum.append(5)
            else:
                vnum.append(2)
    Tielose=True
    if vnum[0]==vnum[1] or vnum[0]==vnum[2] or vnum[1]==vnum[2]:

        ngame("SlotsTie")
        if gplayed("SlotsTie")%3==0 and gplayed("SlotsTie")%5!=0:
            vnum[1]=vnum[0]
            vnum[2]=vnum[0]
        elif gplayed("SlotsTie")%5==0:
            Tielose= True
            bnu= random.randint(2,4)
            vnum[0]= bnu
            vnum[1]=bnu+1
            vnum[2]=bnu-1
            print("Slot Rolled At: ")
            print(vnum)
        else:
            Tielose=False
            print("Slot Rolled At: ")
            print(vnum)
            win=0
            print("Your Bet Will Be Returned")

    if vnum[0]==vnum[1] and vnum[1]==vnum[2]:
            Tielose= False
            if vnum[0]==1:
               win=2.5*bet
            elif vnum[0]==2:
                win=4.0*bet
            elif vnum[0]==3:
                win=5*bet
            elif vnum[0]==4:
                win=7.5*bet
            elif vnum[0]==5:
                win=10*bet
            print("Slot Rolled At: ")
            print(vnum)                
            print("You Won", win)

    else:
        if Tielose == True:
            print("Slot Rolled At: ")
            print(vnum)
            print("Sorry, You Lost",bet)
            win=-bet
            
    print("Updating, Player Balance By: ")
    
    return(win)


def roulette(choice,gamble):
    choice = str(choice)
    choice= choice.capitalize()
    ngame("roulette")
    red = [1,4,7,10,13,16,19,22]                        #All Possible Pools
    black = [2,5,8,11,14,17,20,23]
    green = [3,6,9,12,15,18,21,24]
    even = [2,4,6,8,10,12,14,16,18,20,22,24]
    odd = [1,3,5,7,9,11,13,15,17,19,21,23]

    won=False                                            #Win Or Lose Boolean, if any condition is of win, don't play lose condition.
    d_game1= random.randint(4,7)
    d_game2= random.randint(9,11)                       #Donation game, if this random number within range is a factor of the number of games played, give a free win to the user
    d_game3= random.randint(17,19)
    roll=0
    if gplayed('roulette')%d_game1==0 and gplayed('roulette')%d_game2!=0 and gplayed('roulette')%d_game3!=0:    #If number of times game is played is a factor for d_game
                                                                                                                #and not of a bigger d_game then give a free win
        if choice.capitalize() =='Red' and random.randint(1,6)==1:              #make life a little harder, after the 1/3 * n times played is true, there's a 1/6 chance of winning
            roll=random.choice(red)                                     #roll will
            
        if choice.capitalize() =='Black' and random.randint(1,6)==1:
            roll=random.choice(black)
            
        if choice.capitalize() =='Green' and random.randint(1,6)==1:
            roll=random.choice(green)
            
        if choice.capitalize() =='Odd' and random.randint(1,6)==1:
            roll=random.choice(odd)
            
        if choice.capitalize() =='Even' and random.randint(1,6)==1:
            roll=random.choice(even)
            
    elif gplayed('roulette')%d_game2==0 and gplayed('roulette')%d_game3!=0:
        if choice.capitalize() =='Red' and random.randint(1,5)==1:
            roll=random.choice(red)
            
        if choice.capitalize() =='Black' and random.randint(1,5)==1:
            roll=random.choice(black)
            
        if choice.capitalize() =='Green' and random.randint(1,5)==1:
            roll=random.choice(green)
            
        if choice.capitalize() =='Odd' and random.randint(1,5)==1:
            roll=random.choice(odd)
            
        if choice.capitalize() =='Even' and random.randint(1,5)==1:
            roll=random.choice(even)
            
    elif gplayed('roulette')%d_game3==0:
        if choice.capitalize() =='Red' and random.randint(1,4)==1:                      #for bigger factors, chance becomes 1/4
            roll=random.choice(red)
            
        if choice.capitalize() =='Black' and random.randint(1,4)==1:
            roll=random.choice(black)
            
        if choice.capitalize() =='Green' and random.randint(1,4)==1:
            roll=random.choice(green)
            
        if choice.capitalize() =='Odd' and random.randint(1,4)==1:
            roll=random.choice(odd)
            
        if choice.capitalize() =='Even' and random.randint(1,4)==1:
            roll=random.choice(even)
    else:
        roll = random.randint(1,24)                         #otherwise get a random number from any pool
        
    
    print("Your Call Was On",choice.capitalize())
    print("Roulette, Called On",roll)
    
    if choice.capitalize() == 'Red':                                                    #For each pool if choice is in the pool win game
        for i in red:
            if i==roll:
                
                print("Your Choice Pool Was Correct!")
                win= 3*gamble
                won=True
                
    elif choice.capitalize() == 'Black':
        for i in black:
            if i==roll:
                print("Your Choice Pool Was Correct!")
                win=3*gamble
                won=True
    elif choice.capitalize() == 'Green':
        for i in green:
            if i==roll:
                print("Your Choice Pool Was Correct!")
                win=3*gamble
                won=True
    elif choice.capitalize() == 'Even':
        for i in even:
            if i==roll:
                print("Your Choice Pool Was Correct!")
                win=2*gamble
                won=True
    elif choice.capitalize() == 'Odd':
        for i in odd:
            if i==roll:
                print("Your Choice Pool Was Correct!")
                win=2*gamble
                won=True
    if(won==False):
        win=-gamble
        print(roll,"is not in",choice)
        print("Sorry, You Lost:",win)

    if win>0:
        print("You Won",win,"!")
    return win


# BlackJack discontinued, too similar to other games.

def blackjack(base_gamble):

    print("Under Construction")
    return(base_gamble)
    print("Welcome To Blackjack")
    time.sleep(1)
    print("Ace is 1")
    print("Jack[J], Joker[T], Queen[Q], King[K] are 10")
    print("Rest Of The Deck Represents A Score Of Its Own Value\n")
    time.sleep(4)

    print("Get Closest To '21' To Win, Play Against Dealer")
    print("Hit == Take Another Card From Deck")
    print("Stand == End Game, See If Cards Amount To A Score Closer To 21 Than The Dealer")
    print("Double Down == Double Gamble If Confident In Chances Of Winning\n")
    x = player_init("s")


"""
    outcome = "Hit, Stand Or Double Down"
    # Initialise Score
    player_score = 0
    dealer_score = 0
    win = 0

    # define globals for cards
    RANKS = ['10','10','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
    VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}
    CARDS = ['A','2','3','4','5','6','7','8','9','Q','K','J','T',]
    # Start Game

    error_message = "Invalid Entry, Try One Of:", outcome
    while player_score<=21:

        # Options
        while True:
            try:
                print("So Far Your Cards Are Valued At", player_score)
                print("If You Are Confident In Your Value, Stand. Else: Hit / Double Down\n")
                choice = input("%s?: "%outcome)
            except ValueError:
                print(error_message)
                continue
            if choice.lower() != "hit" and choice.lower() != "stand" and choice.lower() != "double down":
                print(error_message)
                continue
            else:
                if choice.lower()=="stand" and player_score==0:
                    print("Cant stand while card score is just %i, forcing option: 'Hit'"%player_score)
                    choice = "Hit"

                break

        #Give Semi Random Score To Dealer
        dealer_score += int(random.choice(list(RANKS)))
        #        TODO | deal with tie| add content to diffrent choices

        #Continue a round, based on user choice
    
        if choice.lower() == "hit":
            random_card = random.choice(CARDS)
            player_score += VALUES[random_card]
            time.sleep(1)
            print("You Chose To Pick Up Another Card With A Current Score Of %i, You Receive The Card, %s" % (int(player_score), str(random_card)))

            break
            #Hit Player

        if choice.lower() == "stand":
            #TODO compare values of bot/user and then tell user who won, change win vars and return that

            break
            #Stand Player

        if choice.lower() == "double down":

            break
            #Double Down Player

    return(win)

  """


def usr():
    name = start_game()
    return(name)


def doexit():
    raise SystemExit
