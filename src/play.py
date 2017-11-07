#Database For Players 
def offset():

    #used to find the last line
    player= open("src/plist.txt","r+")
    offset = 0
    for line in player:
        offset += len(line)
    player.close()
    return(offset)

def offsetline():

    #used to find all new lines
    player= open("src/plist.txt","r+")
    #This algorithm finds the last line of the txt file
    offsetline=[]
    offset = 0
    player.seek(0)
    for line in player:
        offsetline.append(offset)
        offset += len(line)
    player.close()
    return(offsetline)

def pseek():

    #used to go to last line of file
    player= open("src/plist.txt","r+")
    ofset=offset()
    if (ofset>1):
        player.seek(ofset)
        pseek=player.seek(ofset)
    else:
        player.seek(1)
        pseek=player.seek(1)
    player.close()
    return(pseek)


def player_init(name):
    
    #print(player.read()) === read all users
    #Used to initialise a new unexisting player
    player= open("src/plist.txt","r+")
    player.seek(0)
    for i in offsetline():
        player.seek(i)
        if(player.readline()==(name+"\n")):
            player.close()
            return False
    toseek= pseek()
    player.seek(toseek)
    player.write(("\n\n%s\n500.00\n") % name) #this format organizes names
    player.seek(0)
    player.close()
def player_cont(name):
    name=str(name)
    #Returns data for an existing player
    player= open("src/plist.txt","r")
    for i in offsetline():
        if player.readline()==(name+"\n"):
            money= float(next(player))
            money= money+0.00
            player.close()
            return(money)
    player.close()    

    return False

def pbal_update(name,win):
    name=str(name)
    player= open("src/plist.txt","r+")
    lnum=0
    for i in offsetline():
        if player.readline()==(name+"\n"):
            money= float(next(player))
            money=money+win
            
            offsee=offsetline()
            player.seek(offsee[lnum+1])

            player.write(str(money)+"\n")
            player.close()
            break
        lnum=lnum+1
    return(player_cont(name))
def testing():
    return True
