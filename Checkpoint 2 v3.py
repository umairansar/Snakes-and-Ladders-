#@15112
#Muhammad Umair Ansar   #mansar@andrew.cmu.edu
#Final Project          #Final CheckPoint

#______________________________________________________Instructions_______________________________________________________

'''
To test the online gameplay, make a copy of this code with the following changes
and run on either same computer or another.

1. Replace "mansar", "mansar" in line 1212 to "mumar", "mumar" or any other of my friends.
2. Replace "mumar" in line 663 and line 665 with "mansar" (that is my username).
3. Switch conditions in line 483 and 495 (i.e. compare whichplayer
   with 2 where is 1 and vice versa)

Just in case, I have already made the above changes to the duplicate attached
to this repository.
'''

#______________________________________________________MY CODE____________________________________________________________

from tkinter import *
from PIL import ImageTk, Image
import time
import random
import socket
import threading

#_________________________________________________________________________________________________________________________

class board():

    def __init__(self, root, player, secondP, thirdP, fourthP, Xbox, Ybox, NumOfPlayers):
        self.canvas = root
        self.player = player
        self.secondP = secondP
        self.thirdP = thirdP
        self.fourthP = fourthP
        self.Xbox = Xbox
        self.Ybox = Ybox
        self.NumOfPlayers = NumOfPlayers
        self.canvas.bind("<Button-1>", self.mouseClick)
        self.printToken()
        

    def mouseClick(self, e):
        print (e.x, e.y)

    def findBox(self, i): #Getting pixels for numbers/blocks______________________________________
        '''
        Let n be the block number
        then row = n
        row = row - 10 as long as row = +ve for i iterations
        then i * 50 gives me height of block from below in board
        then vertical height - calculated height = actual height from above
        for col = row as it has been reduced below 10
        check if odd row, observe backward trend
        width - col * 50
        check if even row, then observe forward trend
        col * 50
        '''
        n = i
        row = n
        count = 0
        while row > 0:
            count = count + 1
            row = row - 10
        row = row + 10 
        count = count - 1   # I am considering lower left corner to depict a block, later 25
        y = count * self.Ybox    # added to x and y to be in center approx
        y = 525 - y
        col = row
        if count % 2 == 0:
            x = col * self.Xbox
        else:
            x = col * self.Xbox
            x = 525 - x + self.Xbox

        # Now I have (x, y) corresponding to n-numbered block on board
        print("x=", x, " y=", y)
        return x, y

    #Print token on top of board__________________________________________________________________
    def printToken(self):

        #Localize different tokens differently
        if self.player.getColor() == "red":
            c = 15
        elif self.player.getColor() == "yellow":
            c = 20
        elif self.player.getColor() == "blue":
            c = 10
        elif self.player.getColor() == "green":
            c = 25

        #.........................................................................................
        if count == 1:
            global TOKEN, photo, TOKEN2, photo2, TOKEN3, photo3, TOKEN4, photo4
            if self.NumOfPlayers == 2:
                #Import token
                #global TOKEN, photo
                imgpath = self.player.getToken()
                img = Image.open(imgpath)
                photo = ImageTk.PhotoImage(img)
                X, Y = 0, 525
                TOKEN = self.canvas.create_image(X, Y, image=photo, anchor='center')
                self.canvas.update()

                #Import token
                #global TOKEN2, photo2
                imgpath2 = self.secondP.getToken()
                img2 = Image.open(imgpath2)
                photo2 = ImageTk.PhotoImage(img2)
                X, Y = 0, 510
                TOKEN2 = self.canvas.create_image(X, Y, image=photo2, anchor='center')
                self.canvas.update()

        #.........................................................................................
            elif self.NumOfPlayers == 3:
                #Import token
                #global TOKEN, photo
                imgpath = self.player.getToken()
                img = Image.open(imgpath)
                photo = ImageTk.PhotoImage(img)
                X, Y = 0, 525
                TOKEN = self.canvas.create_image(X, Y, image=photo, anchor='center')
                self.canvas.update()

                #Import token
                #global TOKEN2, photo2
                imgpath2 = self.secondP.getToken()
                img2 = Image.open(imgpath2)
                photo2 = ImageTk.PhotoImage(img2)
                X, Y = 0, 500
                TOKEN2 = self.canvas.create_image(X, Y, image=photo2, anchor='center')
                self.canvas.update()
                
                #Import token
                #global TOKEN3, photo3
                imgpath3 = self.thirdP.getToken()
                img3 = Image.open(imgpath3)
                photo3 = ImageTk.PhotoImage(img3)
                X, Y = 0, 480
                TOKEN3 = self.canvas.create_image(X, Y, image=photo3, anchor='center')
                self.canvas.update()

        #.........................................................................................
            elif self.NumOfPlayers == 4:
                #Import token
                #global TOKEN, photo
                imgpath = self.player.getToken()
                img = Image.open(imgpath)
                photo = ImageTk.PhotoImage(img)
                X, Y = 0, 525
                TOKEN = self.canvas.create_image(X, Y, image=photo, anchor='center')
                self.canvas.update()

                #Import token
                #global TOKEN2, photo2
                imgpath2 = self.secondP.getToken()
                img2 = Image.open(imgpath2)
                photo2 = ImageTk.PhotoImage(img2)
                X, Y = 0, 510
                TOKEN2 = self.canvas.create_image(X, Y, image=photo2, anchor='center')
                self.canvas.update()
                
                #Import token
                #global TOKEN3, photo3
                imgpath3 = self.thirdP.getToken()
                img3 = Image.open(imgpath3)
                photo3 = ImageTk.PhotoImage(img3)
                X, Y = 0, 510
                TOKEN3 = self.canvas.create_image(X, Y, image=photo3, anchor='center')
                self.canvas.update()

                #Import token
                #global TOKEN4, photo4
                imgpath4 = self.fourthP.getToken()
                img4 = Image.open(imgpath4)
                photo4 = ImageTk.PhotoImage(img4)
                X, Y = 0, 510
                TOKEN4 = self.canvas.create_image(X, Y, image=photo4, anchor='center')
                self.canvas.update()

        #.........................................................................................
            
        #In case of 2 players
        if self.NumOfPlayers == 2:
            if count%2 == 1:
                X, Y = self.findBox(self.player.getPosition())
                self.canvas.delete(TOKEN)
                self.canvas.update()
                TOKEN = self.canvas.create_image(X-c, Y-c, image=photo, anchor='center')
                self.canvas.update()
                time.sleep(0.5)
            elif count%2 == 0:
                X, Y = self.findBox(self.player.getPosition())
                self.canvas.delete(TOKEN2)
                self.canvas.update()
                TOKEN2 = self.canvas.create_image(X-c, Y-c, image=photo2, anchor='center')
                self.canvas.update()
                time.sleep(0.5)

        #.........................................................................................

        #In case of 3 players
        if self.NumOfPlayers == 3:
            if whichPlayer == 1:
                X, Y = self.findBox(self.player.getPosition())
                print("X chla, ", X, "Y chla, ", Y)
                self.canvas.delete(TOKEN)
                self.canvas.update()
                TOKEN = self.canvas.create_image(X-c, Y-c, image=photo, anchor='center')
                self.canvas.update()
                time.sleep(0.5)
            elif whichPlayer == 2:
                X, Y = self.findBox(self.player.getPosition())
                print("X chla 2, ", X, "Y chla 2, ", Y)
                self.canvas.delete(TOKEN2)
                self.canvas.update()
                TOKEN2 = self.canvas.create_image(X-c, Y-c, image=photo2, anchor='center')
                self.canvas.update()
                time.sleep(0.5)
            elif whichPlayer == 3:
                X, Y = self.findBox(self.player.getPosition())
                print("X chla 3, ", X, "Y chla 3, ", Y)
                self.canvas.delete(TOKEN3)
                self.canvas.update()
                TOKEN3 = self.canvas.create_image(X-c, Y-c, image=photo3, anchor='center')
                self.canvas.update()
                time.sleep(0.5)

        #.........................................................................................

        #In case of 4 players
        if self.NumOfPlayers == 4:
            if whichPlayer == 1:
                X, Y = self.findBox(self.player.getPosition())
                self.canvas.delete(TOKEN)
                self.canvas.update()
                TOKEN = self.canvas.create_image(X-c, Y-c, image=photo, anchor='center')
                self.canvas.update()
                time.sleep(0.5)
            elif whichPlayer == 2:
                X, Y = self.findBox(self.player.getPosition())
                self.canvas.delete(TOKEN2)
                self.canvas.update()
                TOKEN2 = self.canvas.create_image(X-c, Y-c, image=photo2, anchor='center')
                self.canvas.update()
                time.sleep(0.5)
            elif whichPlayer == 3:
                X, Y = self.findBox(self.player.getPosition())
                self.canvas.delete(TOKEN3)
                self.canvas.update()
                TOKEN3 = self.canvas.create_image(X-c, Y-c, image=photo3, anchor='center')
                self.canvas.update()
                time.sleep(0.5)
            elif whichPlayer == 4:
                X, Y = self.findBox(self.player.getPosition())
                self.canvas.delete(TOKEN4)
                self.canvas.update()
                TOKEN4 = self.canvas.create_image(X-c, Y-c, image=photo4, anchor='center')
                self.canvas.update()
                time.sleep(0.5)

        
        self.canvas.update()
        canvas = self.canvas
        time.sleep(1)
        print("check running ok!!")

    

#_________________________________________________________________________________________________________________________
class Game():
    def __init__(self, players, fst, snd, trd, ft, temp, myDataFrame, NumOfPlayers, mySocket):
        #Snakes and Ladders dictionary
        self.salDict1 = dict()
        self.players = players
        self.point = IntVar()
        self.diceNum = 0
        self.diceBut = 0
        self.temp = temp
        self.frame = myDataFrame
        self.fst = fst
        self.snd = snd
        self.trd = trd
        self.ft = ft
        self.NumOfPlayers = NumOfPlayers
        self.mySocket = mySocket

        self.info = 0
        self.score = 0
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.scoreN = 0
        self.score1N = 0
        self.score2N = 0
        self.score3N = 0
        self.Score = 0
        self.board = 0
        self.change = IntVar()

        #.........................................................................................

        #Calling Functions
        self.salDictionary()
        if count!=1:
            self.createScoreBoard()
            self.updateScoreBoard()
        elif count == 1:
            self.createScoreBoard()

        #.........................................................................................

        #Calling Next Class
        if NumOfPlayers == 2 and self.mySocket != None:
            if whichPlayer == 1:
                put = board(canvas, players, snd, None, None, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer == 2:
                put = board(canvas, players, fst, None, None, Xbox, Ybox, NumOfPlayers) #Put it on board

        elif NumOfPlayers == 2:
            if whichPlayer == 1:
                put = board(canvas, players, snd, None, None, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer == 2:
                put = board(canvas, players, fst, None, None, Xbox, Ybox, NumOfPlayers) #Put it on board

        #.........................................................................................

        if NumOfPlayers == 3:
            if whichPlayer==1:
                put = board(canvas, players, snd, trd, None, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer==2:
                put = board(canvas, players, trd, fst, None, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer==3:
                put = board(canvas, players, fst, snd, None, Xbox, Ybox, NumOfPlayers) #Put it on board

        #.........................................................................................

        if NumOfPlayers == 4:
            if whichPlayer==1:
                put = board(canvas, players, snd, trd, ft, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer==2:
                put = board(canvas, players, trd, ft, fst, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer==3:
                put = board(canvas, players, ft, fst, snd, Xbox, Ybox, NumOfPlayers) #Put it on board
            elif whichPlayer==4:
                put = board(canvas, players, fst, snd, trd, Xbox, Ybox, NumOfPlayers) #Put it on board

    def createScoreBoard(self): #Used to create scoreboard______________________________________
        #First Half of ScoreBoard
        self.Score = Label(self.frame,
                    text="Score",
                    fg="light green",
                    bg = "dark green",
                    borderwidth=2,
                    font = "Helvetica 22 bold",
                    relief="flat")
        self.Score.config(anchor=E)
        self.Score.grid(row=0, column=0)

        #Second Half of ScoreBoard
        self.board = Label(self.frame,
                    text="Board",
                    fg="light green",
                    bg = "dark green",
                    borderwidth=2,
                    font = "Helvetica 22 bold",
                    relief="flat")
        self.board.config(anchor=W)
        self.board.grid(row=0, column=1)

        #Label Player 1
        self.score = Label(self.frame,
                      text = "Player 1",
                      fg = "red",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")

        #Label Player 2
        self.score1 = Label(self.frame,
                       text = "Player 2",
                       fg = "orange",
                       width = 10,
                       height = 2,
                       font = "Helvetica 10 bold")

        #Label Player 3
        self.score2 = Label(self.frame,
                      text = "Player 3",
                      fg = "blue",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")

        #Label Player 4
        self.score3 = Label(self.frame,
                       text = "Player 4",
                       fg = "green",
                       width = 10,
                       height = 2,
                       font = "Helvetica 10 bold")


        #Score Player 1
        self.scoreN = Label(self.frame,
                      text = "__",
                      fg = "red",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")

        #Score Player 2
        self.score1N = Label(self.frame,
                       text = "__",
                       fg = "orange",
                       width = 10,
                       height = 2,
                       font = "Helvetica 10 bold")

        #Score Player 3
        self.score2N = Label(self.frame,
                      text = "__",
                      fg = "blue",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")

        #Score Player 4
        self.score3N = Label(self.frame,
                       text = "__",
                       fg = "green",
                       width = 10,
                       height = 2,
                       font = "Helvetica 10 bold")

        
        self.score.grid(row=1, column=0)
        self.score1.grid(row=1, column=1)
        self.score2.grid(row=3, column=0)
        self.score3.grid(row=3, column=1)

        self.scoreN.grid(row=2, column=0)
        self.score1N.grid(row=2, column=1)
        self.score2N.grid(row=4, column=0)
        self.score3N.grid(row=4, column=1)

        #Info Box 
        self.info = Listbox(self.frame, relief="flat", width=27, height=10)
        self.info.grid(row=12, column=0, columnspan=2)

        #Label for space
        self.invisible = Label(self.frame,
                      text = "",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")
        self.invisible.grid(row=13, column=0, columnspan=2)

        #Dice Number
        self.diceNum = Label(self.frame,
                      text = "-/-|-\-",
                      fg = "black",
                      width = 9,
                      height = 1,
                      font = "Helvetica 14 bold")
        self.diceNum.grid(row=14, column=0, columnspan=2)
        

        if self.temp == 0:
            if whichPlayer == 1:
                #Dice Button
                self.diceBut = Button(self.frame,
                                 text="ROLL DICE",
                                 relief="groove",
                                 bg="white",
                                 font="Helvetica 12 bold",
                                 command= lambda : self.gameMaster(self.players, None))
                self.diceBut.config(anchor="w")
                self.diceBut.grid(row=15, column=0, columnspan=2)
                self.diceBut.wait_variable(self.change)
                
            elif whichPlayer == 2:
                #Dice Button (Computer's Turn)
                self.diceBut = Button(self.frame,
                                 text="ROLL DICE",
                                 relief="groove",
                                 bg="white",
                                 font="Helvetica 12 bold",
                                 command= self.gameMaster(self.players, None))
                self.diceBut.config(anchor="w")
                self.diceBut.grid(row=15, column=0, columnspan=2)

        #When socket connection..............................................................
        elif self.mySocket:
            if whichPlayer == 1:
                #Dice Button
                self.diceBut = Button(self.frame,
                                 text="ROLL DICE",
                                 relief="groove",
                                 bg="white",
                                 font="Helvetica 12 bold",
                                 command= lambda : self.gameMaster(self.players, None))
                self.diceBut.config(anchor="w")
                self.diceBut.grid(row=15, column=0, columnspan=2)
                self.diceBut.wait_variable(self.change)
                
            elif whichPlayer == 2:
                #Dice Button (Friends Turn)
                self.diceBut = Button(self.frame,
                                 text="ROLL DICE",
                                 relief="groove",
                                 bg="white",
                                 font="Helvetica 12 bold",
                                 command= self.gameMaster(self.players, self.mySocket))
                self.diceBut.config(anchor="w")
                self.diceBut.grid(row=15, column=0, columnspan=2)

        else:
            #Dice Button
            self.diceBut = Button(self.frame,
                             text="ROLL DICE",
                             relief="groove",
                             bg="white",
                             font="Helvetica 12 bold",
                             command= lambda : self.gameMaster(self.players, None))
            self.diceBut.config(anchor="w")
            self.diceBut.grid(row=15, column=0, columnspan=2)
            self.diceBut.wait_variable(self.change)

    #___________________________________________________________________________________________________

    def updateScoreBoard(self):
        if self.NumOfPlayers >= 2:
            self.scoreN["text"] = str(self.fst.getPosition())
            self.score1N["text"] = str(self.snd.getPosition())
            if self.NumOfPlayers >= 3:
                self.score2N["text"] = str(self.trd.getPosition())
                if self.NumOfPlayers == 4:
                    self.score3N["text"] = str(self.ft.getPosition())
                
    #___________________________________________________________________________________________________

    def salDictionary(self):
        self.salDict1 = {5: 35,
                        13: 24,
                        18: 39,
                        30: 53,
                        33: 57,
                        59: 83,
                        51: 87,
                        67: 73,
                        86: 38,
                        97: 61,
                        70: 89,   
                        }
    #___________________________________________________________________________________________________

    def SaveScoreBoard(self):
        print("inside save score board")
        file = open("Score Record.txt", 'w')
        file.write("Score Board")
        file.write("\n")
        file.write(str(self.NumOfPlayers))
        file.write("\n")
        if self.NumOfPlayers >= 2:
            file.write("Player "+ str(self.fst.getPlayerNum()) + ": " + str(self.fst.getPosition()))
            file.write("\n")
            file.write("Player "+ str(self.snd.getPlayerNum()) + ": " + str(self.snd.getPosition()))
            file.write("\n")
            if self.NumOfPlayers >= 3:
                file.write("Player "+ str(self.trd.getPlayerNum()) + ": " + str(self.trd.getPosition()))
                file.write("\n")
                if self.NumOfPlayers == 4:
                    file.write("Player "+ str(self.ft.getPlayerNum()) + ": " + str(self.ft.getPosition()))
                    file.write("\n")
    #___________________________________________________________________________________________________

    #Function to handle player turn
    def gameMaster(self, myPlayer, sock):
        global winner
        self.change.set(self.change.get())  #GAME CHANGER___________

        #check for game winner
        if myPlayer.getPosition() == 100:
            print("Player %i is the Winner!" % myPlayer.getPlayerNum())
            root = Toplevel()
            msg = Label(root, text="Player %i is the Winner!" % myPlayer.getPlayerNum(),
                    fg="light green",
                    bg = "dark green",
                    borderwidth=2,
                    font = "Helvetica 22 bold",
                    relief="flat")
            msg.config(anchor=CENTER)
            msg.pack()
            winner = True

        #.........................................................................................

        #run dice rolls and movements
        if winner == False:

        #.........................................................................................

            #if message received from friend
            if sock != None:
                msg = TheMsg(sock)
                while msg == None:
                    msg = TheMsg(sock)
                    try:
                        msg = int(msg)
                        myPlayer.setPlayerNum(2)
                        self.moveToken(myPlayer, msg)
                        self.checkPosition(myPlayer)

                        #Check if reached 100
                        if myPlayer.getPosition() == 100:
                            root = Toplevel()
                            msg = Label(root, text="Player %i is the Winner!" % myPlayer.getPlayerNum(),
                                fg="light green",
                                bg = "dark green",
                                borderwidth=2,
                                font = "Helvetica 22 bold",
                                relief="flat")
                            msg.config(anchor=CENTER)
                            msg.pack()

                            #Save Score Board for Current Game
                            print("about to execute savescoreboard")
                            self.SaveScoreBoard()

                            #Update Winner
                            winner = True

                    except:
                        print("No number received from the Friend")

        #.........................................................................................

            #for normal offline play                        
            else:
                totalPoints = 0
                print("\n----Player %i Hit enter to roll----" % myPlayer.getPlayerNum())
                self.info.insert(END,"\n----Player %i Hit enter to roll----" % myPlayer.getPlayerNum())
                point = self.throDice()
                self.updatePlayerLabel()
                totalPoints = point
                print("You rolled: %i" % point)
                self.info.insert(END,"You rolled: %i" % point)
                self.moveToken(myPlayer, point)
                if point == 6:
                    point = self.throDice()
                    self.updatePlayerLabel()
                    totalPoints = totalPoints + point
                    print("Bonus Turn: You rolled: %i" % point)
                    self.info.insert(END, "You rolled: %i" % point)
                    self.moveToken(myPlayer, point)
                    if point == 6:
                        point = self.throDice()
                        self.updatePlayerLabel()
                        totalPoints = totalPoints + point
                        print("Bonus Turn: You rolled: %i" % point)
                        self.info.insert(END, "You rolled: %i" % point)
                        self.moveToken(myPlayer, point)
                        self.checkPosition(myPlayer)
                        if totalPoints == 18:
                            print("Bad Luck: You rolled 3 sixes.")
                            self.info.insert(END, "Bad Luck: You rolled 3 sixes.")
                            self.moveToken(myPlayer, -18)
                            self.checkPosition(myPlayer)
                    else:
                        self.checkPosition(myPlayer)
                        #send msg to peer
                else:
                    self.checkPosition(myPlayer)
                    #send msg to peee

        #.........................................................................................

                if self.mySocket != None:
                    if totalPoints == 18:
                        totalPoints = 0
                        sendMessage(self.mySocket, "mumar", str(totalPoints))
                    else:
                        sendMessage(self.mySocket, "mumar", str(totalPoints))

        #.........................................................................................

                            #if message received from friend
                if sock != None:
                    msg = TheMsg(sock)
                    while msg == None:
                        msg = TheMsg(sock)
                        try:
                            msg = int(msg)
                            myPlayer.setPlayerNum(2)
                            self.moveToken(myPlayer, msg)

                            #Check if reached 100
                            if myPlayer.getPosition() == 100:
                                root = Toplevel()
                                msg = Label(root, text="Player %i is the Winner!" % myPlayer.getPlayerNum(),
                                    fg="light green",
                                    bg = "dark green",
                                    borderwidth=2,
                                    font = "Helvetica 22 bold",
                                    relief="flat")
                                msg.config(anchor=CENTER)
                                msg.pack()

                                #Save Score Board for Current Game
                                print("about to execute savescoreboard")
                                self.SaveScoreBoard()

                                #Update Winner
                                winner = True

                        except:
                            print("No number received from the Friend")

        #.........................................................................................

                if myPlayer.getPosition() == 100:
                    root = Toplevel()
                    msg = Label(root, text="Player %i is the Winner!" % myPlayer.getPlayerNum(),
                        fg="light green",
                        bg = "dark green",
                        borderwidth=2,
                        font = "Helvetica 22 bold",
                        relief="flat")
                    msg.config(anchor=CENTER)
                    msg.pack()
                    #Save Score Board for Current Game
                    print("about to execute savescoreboard")
                    self.SaveScoreBoard()

                    #Update Winner
                    winner = True
        self.updateScore()

    #.........................................................................................

    def rollDice(self):
        self.point = random.randint(1,6)
        self.diceNum["text"] = self.point
        print(self.point)

    #.........................................................................................

    def throDice(self):
        self.rollDice()    #to run uncomment this and comment wait ones
        #self.updateScore()
        return self.point

    #.........................................................................................

    def updateScore(self):
        print("updating scores in colored labels.....................", self.players.getPlayerNum())
        if self.players.getPlayerNum() == 1:
            self.scoreN["text"] = str(self.players.getPosition())
        if self.players.getPlayerNum() == 2:
            self.score1N["text"] = str(self.players.getPosition())
        if self.players.getPlayerNum() == 3:
            self.score2N["text"] = str(self.players.getPosition())
        if self.players.getPlayerNum() == 4:
            self.score3N["text"] = str(self.players.getPosition())

    #.........................................................................................

    def updatePlayerLabel(self):
        self.diceNum["text"] = "Player " + str(self.players.getPlayerNum()) + ": " + str(self.point)

    #.........................................................................................

    def moveToken(self, myPlayer, points):
        possiblePosition = myPlayer.getPosition() + points
        if possiblePosition <= 100:
            myPlayer.updatePosition(possiblePosition)
            print("You are at the spot %i" % possiblePosition)
            self.info.insert(END, "You are at the spot %i" % possiblePosition)
        else:
            print("Your points are over the required limit.")
            self.info.insert(END,"Your points are over the required limit.")

    #.........................................................................................

    def checkPosition(self, myplayer):
        for pos in self.salDict1:
            if pos == myplayer.getPosition():
                if pos < self.salDict1[pos]:
                    print("You climbed a ladder to spot %i" % self.salDict1[pos])
                    self.info.insert(END, "You climbed a ladder to spot %i" % self.salDict1[pos])
                else:
                    print("You rode a snake to spot %i" % self.salDict1[pos])
                    self.info.insert(END,"You rode a snake to spot %i" % self.salDict1[pos])
                myplayer.updatePosition(self.salDict1[pos])


        
#_________________________________________________________________________________________________________________________
class Player():
    def __init__(self, playerNum, token, color):
        self.token = token
        self.playerNum = playerNum
        self.playerPos = 0
        self.color = color

    def updatePosition(self, pos):
        self.playerPos = pos

    def setPlayerNum(self, num):
        self.playerNum = num

    def getPosition(self):
        return self.playerPos

    def getPlayerNum(self):
        return self.playerNum

    def getToken(self):
        return self.token

    def getColor(self):
        return self.color
#_________________________________________________________________________________________________________________________

class createBoard():
    def __init__(self, root):
        self.root = root
        
        #Create Frame
        self.frame1 = Frame(self.root)
        self.frame1.pack(side='left')
        self.frame2 = Frame(self.root)
        self.frame2.pack(side='right')

        #Box dimensions
        self.Xbox = 0
        self.Ybox = 0

        #Import Board
        self.imgpath = "Board 2 v2.jpg"
        self.img = Image.open(self.imgpath)
        self.photo = ImageTk.PhotoImage(self.img)

        #Import 2nd Board
        self.imgpathS = "Board 4 v4.jpg"
        self.imgS = Image.open(self.imgpathS)
        self.photoS = ImageTk.PhotoImage(self.imgS)

        #Initiate Dimensions
        self.Xbox = 0
        self.Ybox = 0
        self.diceBut = 0
        self.diceNum = 0
        self.invisible = 0

        #Calling Functions
        self.boxDimensions()

        choice = random.randint(1,2)
        if choice == 1:
            print("choice")
            self.PHOTO = self.photo
        else:
            self.PHOTO = self.photoS


        #Create Canvas and Bind Event
        self.canvas = Canvas(self.frame1, width=528, height=525)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.PHOTO, anchor='nw')
        self.canvas.update()


    def boxDimensions(self):    #Calculate Box Dims
        width, height = self.img.size
        print(width, height)
        self.Xbox = width/10
        self.Ybox = height/10
        print("Xbox = ", self.Xbox, " Ybox = ", self.Ybox)

    def returnCanvasRN(self):
        return self.canvas

    def returnDimensions(self):
        print("Xbox: ", self.Xbox, self.Ybox)
        return self.Xbox, self.Ybox

    def returnFrame2(self):
        return self.frame2

#_________________________________________________________________________________________________________________________
def closeWindow():
    print("file created!")
    file = open("pastScore.txt", 'w')
    file.write(str(wp))
    file.write("\n")
    file.write(str(np))
    file.write("\n")
    for x in range(np):
        file.write(str(p[x].getPosition()))
        file.write("\n")
    file.close()
    root.destroy()

#_________________________________________________________________________________________________________________________

def call(NumOfPlayers, temp, myDataFrame, mySocket):
    if temp == 0:
        if whichPlayer == 1:
            start = Game(players[0], players[0], players[1], None, None, temp, myDataFrame, NumOfPlayers, None) #Start Game
        elif whichPlayer == 2:
            start = Game(players[1], players[0], players[1], None, None, temp, myDataFrame, NumOfPlayers, None) #Start Game
                             
    elif mySocket!= None:
        if whichPlayer == 1:
            start = Game(players[0], players[0], players[1], None, None, temp, myDataFrame, 2, mySocket) #Start Game
        elif whichPlayer == 2:
            start = Game(players[1], players[0], players[1], None, None, temp, myDataFrame, 2, mySocket) #Start Game

    elif NumOfPlayers == 2:
        if whichPlayer == 1:
            start = Game(players[0], players[0], players[1], None, None, temp, myDataFrame, NumOfPlayers, None) #Start Game
        elif whichPlayer == 2:
            start = Game(players[1], players[0], players[1], None, None, temp, myDataFrame, NumOfPlayers, None) #Start Game
                    
    elif NumOfPlayers == 3:
        if whichPlayer==1:
            start = Game(players[0], players[0], players[1], players[2], None, temp, myDataFrame, NumOfPlayers, None) #Start Game    
        elif whichPlayer==2:
            start = Game(players[1], players[0], players[1], players[2], None, temp,  myDataFrame, NumOfPlayers, None) #Start Game   
        elif whichPlayer==3:
            start = Game(players[2], players[0], players[1], players[2], None, temp, myDataFrame, NumOfPlayers, None) #Start Game
    
    elif NumOfPlayers == 4:
        if whichPlayer==1:
            start = Game(players[0], players[0], players[1], players[2], players[3], temp, myDataFrame, NumOfPlayers, None) #Start Game    
        elif whichPlayer==2:
            start = Game(players[1], players[0], players[1], players[2], players[3], temp, myDataFrame, NumOfPlayers, None) #Start Game    
        elif whichPlayer==3:
            start = Game(players[2], players[0], players[1], players[2], players[3], temp, myDataFrame, NumOfPlayers, None) #Start Game    
        elif whichPlayer==4:
            start = Game(players[3], players[0], players[1], players[2], players[3], temp, myDataFrame, NumOfPlayers, None) #Start Game

        
#_________________________________________________________________________________________________________________________
def core(NumOfPlayers, temp, main_root, wp_resume, Resume, mySocket):

    #Change Window Content
    global root
    root = main_root
    root.title("Snakes and Laders 2019")
    root.geometry("707x525")
        
    extension = "C:\\Users\\umair\\Desktop\\CS 112\\Project\\Boards\\"
    global players
    players = []

    #Make list of token addresses
    tokens = [extension+"tokenv1.jpg",
              extension+"tokenv2.jpg",
              extension+"tokenv3.jpg",
              extension+"tokenv4.jpg"]
    color = ["red", "yellow","blue", "green"]

    #Create Board
    create = createBoard(root)
    
    global canvas, winner, count, whichPlayer
    canvas = create.returnCanvasRN()

    #Get Block Dimensions
    global Xbox, Ybox
    Xbox, Ybox = create.returnDimensions()

    #Get Right Frame (to be populated)
    global myDataFrame
    myDataFrame = create.returnFrame2()

    #Concat player objects into list
    for i in range(NumOfPlayers):
        players.append(Player(i+1, tokens[i], color[i])) #where i+1 denotes player number

    #Initialize Variables
    count = 0
    winner = False
    whichPlayer = 1

    
    global np, p, wp
    np = NumOfPlayers
    p = players
    wp = whichPlayer

    while winner == False:
        #Track Closing Action (Save Score)
        root.protocol("WM_DELETE_WINDOW", closeWindow)
    
        whichPlayer = 1 #used to reset positions of player calls in board function

        if Resume == True and count == 0:
            for j in range(np):
                players[j].updatePosition(scores[j])
                print("Player Number ", players[j].getPlayerNum(), " is on position ", scores[j])
            whichPlayer = wp_resume
            print("whichPlayer dummy : ", whichPlayer)
            Resume = False

            #Run the Game Classes/Functions
            for i in range(whichPlayer-1, len(players)):
                if winner == False:
                    count += 1
                    call(NumOfPlayers, temp, myDataFrame, mySocket) #Resume Call
                    whichPlayer += 1    #updated player turn
                    wp = whichPlayer    #updated to safe in resume file
                    
  
        else:
            #Run the Game Classes/Functions
            for i in range(len(players)): #calling main if-else calls for game
                if winner == False:
                    count+=1
                    call(NumOfPlayers, temp, myDataFrame, mySocket)
                    whichPlayer += 1    #updated player turn
                    wp = whichPlayer    #updated to safe in resume file
                
                    
    

    

#_________________________________________________________________________________________________________________________
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def leftrotate (x, c):
    return (x << c)&0xFFFFFFFF | (x >> (32-c)&0x7FFFFFFF>>(32-c))

def StartConnection (IPAddress, PortNumber):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("86.36.46.10", 15112))
    return s

def login (sock, username, password):

    command = "LOGIN " + username + "\n"
    command = str.encode(command)
    sock.send(command)
    msg = sock.recv(512)
    msg = str(msg, 'utf-8')

    #Extracting Challenge from the message using negative indeces
    space = msg.rfind(" ")
    space = -1 * (len(msg) - space)
    chal = msg[space+1:]

    message = password + chal
    block = ""
    check = False #used to get inside loop just after appending message
    lenght = str(len(message))
    

    #Creating block of lenght 509
    for i in range(0,509-(int(lenght)-1)):

        if i == 0:
            block = block + message
            check = True

        elif check == True:
            check = False
            block = block + "1"
    
        else:
            block = block + "0"

    
    #Appending to block the size of message
    if int(lenght) < 100:
        block = block + "0" + lenght[0] + lenght[1]
    elif int(lenght) < 999:
        block = block + lenght[0] + lenght[1] + lenght[2]

    #Thus, a block string of total lenght 512 is created now.

    #Dividing block in sets of 32
    M = [block[i:i+32] for i in range(0, len(block), 32)]

    #Replacing string in M with sum of ASCIIs
    for i in range(len(M)):
        asc = 0
        for j in range(len(M[i])):
            asc = asc + ord(M[i][j])
        M[i] = asc
    
    #Given Code
    s = []
    K = []
    
    s[0:16] = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22]
    s[16:32] = [5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20]
    s[32:48] = [4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23]
    s[48:64] = [6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

    K[0:4] = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee]
    K[4:8] = [0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501]
    K[8:12] = [0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be]
    K[12:16] = [0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821]
    K[16:20] = [0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa]
    K[20:24] = [0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8]
    K[24:28] = [0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed]
    K[28:32] = [0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a]
    K[32:36] = [0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c]
    K[36:40] = [0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70]
    K[40:44] = [0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05]
    K[44:48] = [0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665]
    K[48:52] = [0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039]
    K[52:56] = [0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1]
    K[56:60] = [0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1]
    K[60:64] = [0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

    #Initialize variables
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    A = a0
    B = b0
    C = c0
    D = d0

    for i in range(0, 64):
        if 0 <= i <= 15:
            F = (B & C) | ((~B) & D)
            F = F & 0xFFFFFFFF

            g = i
        elif 16 <= i <= 31:
            F = (D & B) | ((~D) & C)
            F = F & 0xFFFFFFFF
            g = (5*i + 1) % 16
        elif 32 <= i <= 47:
            F = B ^ C ^ D
            F = F & 0xFFFFFFFF
            g = (3*i + 5) % 16
        elif 48 <= i <= 63:
            F = C ^ (B | (~D))
            F = F & 0xFFFFFFFF
            g = (7*i) % 16
        dtemp = D
        D = C
        C = B
        B = B + leftrotate((A + F + K[i] + M[g]), s[i])
        B = B & 0xFFFFFFFF
        A = dtemp

    #And this chunk's hash to result so far
    a0 = (a0 + A) & 0xFFFFFFFF
    b0 = (b0 + B) & 0xFFFFFFFF
    c0 = (c0 + C) & 0xFFFFFFFF
    d0 = (d0 + D) & 0xFFFFFFFF


    result = str(a0) + str(b0) + str(c0) + str(d0)
    messageDigest = result
    
    command = "LOGIN " + username + " " + messageDigest + "\n"
    command = str.encode(command)

    sock.send(command)

    msg = sock.recv(512)
    msg = str(msg, 'utf-8')

    if msg[0:16] == "Login Successful":
        return True
    
    return False


def getFriends(sock):

    #Sending Request
    sock.send(b"@friends\n")
    msg = sock.recv(10000)
    msg = str(msg, 'utf-8')
    msg = msg.split('@')
    return msg[4:]

def ShowFriends(select, socket):
    Friends = getFriends(socket)
    if Friends != []:
        for f in Friends:
            select.insert(END,f)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#_________________________________________________________________________________________________________________________
def resumeEvent():
    try:
        file = open("pastScore.txt", 'r')
        print("file exists")
        whichPlayer = file.readline()
        TotalPlayers = file.readline()
        global scores
        scores = []
        for i in range(int(TotalPlayers)):
            scores.append(int(file.readline()))
        global Resume
        Resume = True
        temp = 1000
        print("main_root in resumeEvent(): ", main_root)

        #Delete the items
        main_canvas.destroy()
        main_frame.destroy()

        #Call for newer itms to be placed on same root
        core(int(TotalPlayers), temp, main_root, int(whichPlayer), Resume, None)
        
    except IOError:
        print("File not accessible")
#_________________________________________________________________________________________________________________________
def newgameEvent():
    main_canvas.delete(resume)
    main_canvas.delete(start)
    main_canvas.delete(online)
    main_canvas.delete(score)
    main_canvas.delete(rules)

    global comp, p2, p3, p4, back

    comp = Button(main_canvas, text="Human V Computer", width=20, bg = "#E2EBEF", font="Helvetica 22", command=compEvent)
    comp = main_canvas.create_window(715, 251, window=comp)

    p2 = Button(main_canvas, text="Two Player", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=p2Event)
    p2 = main_canvas.create_window(715, 309, window=p2)

    p3 = Button(main_canvas, text="Three Player", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=p3Event)
    p3 = main_canvas.create_window(715, 367, window=p3)

    p4 = Button(main_canvas, text="Four Player", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=p4Event)
    p4 = main_canvas.create_window(715, 425, window=p4)

    back = Button(main_canvas, text="<", width=20, bg = "#E2EBEF",  font="Helvetica 15", command=clearNewGame)
    back = main_canvas.create_window(715, 490, window=back)
#_________________________________________________________________________________________________________________________

def comeOnline():
    socket = StartConnection("86.36.46.10", 15112)
    In = login (socket, "mansar", "mansar")
    if In == True:
        print("Login was successful.")
    
    main_canvas.delete(resume)
    main_canvas.delete(start)
    main_canvas.delete(online)
    main_canvas.delete(score)
    main_canvas.delete(rules)

    #Select Friend
    select = Listbox(main_canvas, selectmode=BROWSE, width=60, height=10, exportselection=0)
    ShowFriends(select, socket)
    selectR = main_canvas.create_window(450, 300, window=select)

    #Send Invite
    invite = Button(main_canvas, text="Send Request", width=20, font="Helvetica 16", command=lambda: sendMsg(select, socket))
    inviteR = main_canvas.create_window(450, 410, window=invite)

    #Accept Invite
    accept = Button(main_canvas, text="Accept", width=20, font="Helvetica 16", command=lambda: openGame(socket))
    acceptR = main_canvas.create_window(450, 452, window=accept)

    #Accept Invite
    reply = Button(main_canvas, text="Check Reply", width=20, font="Helvetica 16", command=lambda: openGamefromReply(socket))
    replyR = main_canvas.create_window(450, 494, window=reply)

    #Back to Home
    home = Button(main_canvas, text="<", width=17, font="Helvetica 16", command=lambda: clearOnline(selectR, inviteR, acceptR, replyR, homeR))
    homeR = main_canvas.create_window(450, 546, window=home)

    checkReply(socket)

def checkReply(socket):
    time.sleep(2)
    if ShowMessages(socket):
        if TheMsg(socket) == "okay":
            #Call 2 by 2 function
            #Window Open from okay reply
            global net
            net = socket
            p2OnlineEvent() 
                        
def sendMsg(select, socket):
    person = select.get(select.curselection())
    message = "Play?"
    if sendMessage(socket, person, message):
        print("Game Request Sent to ", person)

def sendMessage(sock, friend, message):

    #Trimming size ti be 5 digit
    command = "@@sendmsg@" + friend + "@" + message
    size = len(command)
    size = size + len(str(size))

    #Finding size
    if len(str(size)) != 5:
        less = 5 - len(str(size))
        size = less * "0" + str(size + less)

    command = "@" + str(size) + command[1:]
    
    command = str.encode(command)

    sock.send(command)
    msg = sock.recv(10000)
    msg = str(msg, 'utf-8')

    if "@ok" in msg:
        return True

    return False

def openGame(socket):
    person = ShowMessages(socket)
    if person:
        if sendMessage(socket, person, "okay"):
            print("reply sent to the original invitee")
            print(TheMsg(socket))
            print(person)
            #Call 2 by 2 function
            global net
            net = socket
            p2OnlineEvent()

def openGamefromReply(socket):
    person = ShowMessages(socket)
    if person:
        print(person)
        #Call 2 by 2 function
        global net
        net = socket
        p2OnlineEvent()
        
def TheMsg(socket):
    (Messages, Files) = getMail(socket)
    if Messages != []:
        for (u, m) in Messages:
            friend = u  #use most recent invite 
        return m
    return None

def ShowMessages(socket):
    (Messages, Files) = getMail(socket)
    if Messages != []:
        for (u, m) in Messages:
            friend = u  #use most recent invite 
        return friend
    return None

def getMail(sock):

    #Sending Request
    sock.send(b"@rxmsg\n")
    msg = sock.recv(10000)
    msg = str(msg, 'utf-8')
    
    msg = msg.split('@')

    msg = msg[3:]
    messageT = []   #username + message
    messageFPrint = []  #username + filename
    messageFSave = []   #filename + content

    #Appending to the list for returning
    for i in range(len(msg)):
        if msg[i] == "msg":
            messageT.append((msg[i+1], msg[i+2]))
            i = i + 3
        elif msg[i] == "file":
            messageFPrint.append((msg[i+1], msg[i+2]))
            messageFSave.append([msg[i+2], msg[i+3]])
            i = i + 4

    
    #Saving files with file name
    for i in range(len(messageFSave)):
        file = open(messageFSave[i][0], "w")
        file.write(messageFSave[i][1])
        file.close()
            
    return (messageT,messageFPrint)

#_________________________________________________________________________________________________________________________

def viewOldScores():
    main_canvas.delete(resume)
    main_canvas.delete(start)
    main_canvas.delete(online)
    main_canvas.delete(score)
    main_canvas.delete(rules)

    try:
        file = open("Score Record.txt", 'r')
        print("Score Record file exists")
        heading = file.readline()
        TotalPlayers = int(file.readline())
        scores = []
        for i in range(int(TotalPlayers)):
            data = file.readline()
            data = data[:len(data)-1]
            scores.append(data)

        global board1, board2, board3, board4, Score, but

        #First Half of ScoreBoard
        Score = Label(main_canvas,text="Score Board",borderwidth=2,font = "Helvetica 28 bold",relief="groove")
        Score = main_canvas.create_window(450, 200, window=Score)

        #Second Half of ScoreBoard
        jump = 0
        if TotalPlayers >= 2:
            board1 = Label(main_canvas,text=scores[0],borderwidth=2, bg = "#E2EBEF",width = 30,font = "Helvetica 22 ",relief="flat")
            board1 = main_canvas.create_window(450, 300+jump, window=board1)
            jump += 50
            board2 = Label(main_canvas,text=scores[1],borderwidth=2,bg = "#E2EBEF",width = 30,font = "Helvetica 22 ",relief="flat")
            board2 = main_canvas.create_window(450, 300+jump, window=board2)
            jump += 50
            if TotalPlayers >= 3:
                board3 = Label(main_canvas,text=scores[2],borderwidth=2,bg = "#E2EBEF",width = 30,font = "Helvetica 22 ",relief="flat")
                board3 = main_canvas.create_window(450, 300+jump, window=board3)
                jump += 50
                if TotalPlayers == 4:
                    board4 = Label(main_canvas,text=scores[3],borderwidth=2,bg = "#E2EBEF",width = 30,font = "Helvetica 22 ",relief="flat")
                    board4 = main_canvas.create_window(450, 300+jump, window=board4)
                    jump += 50

        but = Button(main_canvas,text="<",borderwidth=2,font = "Helvetica 16 ",bg = "#E2EBEF", width=20, command= lambda : clearScoreBoard(TotalPlayers))                   
        but = main_canvas.create_window(450, 300+jump, window=but)

        jump += 50
        
    except IOError:
        print("File not accessible")

#_________________________________________________________________________________________________________________________

def viewRules():
    main_canvas.delete(resume)
    main_canvas.delete(start)
    main_canvas.delete(online)
    main_canvas.delete(score)
    main_canvas.delete(rules)

    text0 = "The rules are as follows: \n\n"
    text1 = "1. Each player gets to roll a dice ranging from 1 to 6. \n\n"
    text2 = "2. If a person gets a 6, they get a bonus turn. \n\n"
    text3 = "3. Three consecutive sixes, and all the points are cancelled. \n\n"
    text4 = "4. Whichever player reaches the 100th block first wins. \n\n"
    text = text0+text1+text2+text3+text4

    global guideR, BackR
    guide = Label(main_canvas,text=text,borderwidth=2,font = "Helvetica 18 bold",relief="groove")
    guideR = main_canvas.create_window(450, 300, window=guide)

    Back = Button(main_canvas,text="<",borderwidth=2,font = "Helvetica 16 ",bg = "#E2EBEF", width=20, command= lambda : clearRules())                   
    BackR = main_canvas.create_window(450, 500, window=Back)

def clearRules():
    main_canvas.delete(guideR)
    main_canvas.delete(BackR)

    #Calling Functions
    initializeButtons()    

#_________________________________________________________________________________________________________________________

def compEvent():
    global NumOfPlayers, temp
    NumOfPlayers = 2
    temp = 0
    main_canvas.destroy()
    main_frame.destroy()
    core(NumOfPlayers, temp, main_root, None, None, None)
    main_root.withdraw()
def p2OnlineEvent():
    global NumOfPlayers, temp
    NumOfPlayers = 2
    temp = 1000
    main_canvas.destroy()
    main_frame.destroy()
    core(NumOfPlayers, temp, main_root, None, None, net)
    main_root.withdraw()
def p2Event():
    global NumOfPlayers, temp
    NumOfPlayers = 2
    temp = 1000
    main_canvas.destroy()
    main_frame.destroy()
    core(NumOfPlayers, temp, main_root, None, None, None)
    main_root.withdraw()
def p3Event():
    global NumOfPlayers, temp
    NumOfPlayers = 3
    temp = 1000
    main_canvas.destroy()
    main_frame.destroy()
    core(NumOfPlayers, temp, main_root, None, None, None)
    main_root.withdraw()
def p4Event():
    global NumOfPlayers, temp
    NumOfPlayers = 4
    temp = 1000
    main_canvas.destroy()
    main_frame.destroy()
    core(NumOfPlayers, temp, main_root, None, None, None)
    main_root.withdraw()

#_________________________________________________________________________________________________________________________
def clearNewGame():
    main_canvas.delete(comp)
    main_canvas.delete(p2)
    main_canvas.delete(p3)
    main_canvas.delete(p4)
    main_canvas.delete(back)

    #Calling Functions
    initializeButtons()

#_________________________________________________________________________________________________________________________
def clearScoreBoard(TotalPlayers):
    main_canvas.delete(but)
    main_canvas.delete(Score)
    main_canvas.delete(board1)
    main_canvas.delete(board2)
    if TotalPlayers>=3:
        main_canvas.delete(board3)
        if TotalPlayers==4:
            main_canvas.delete(board4)

    #Calling Functions
    initializeButtons()

#_________________________________________________________________________________________________________________________
def clearOnline(select, accept, invite, reply, home):
    main_canvas.delete(select)
    main_canvas.delete(accept)
    main_canvas.delete(online)
    main_canvas.delete(invite)
    main_canvas.delete(reply)
    main_canvas.delete(home)
    
    
    #Calling Functions
    initializeButtons()
        
#_________________________________________________________________________________________________________________________

def initializeButtons():
    global resume, start, online, score, rules
    resume = Button(main_canvas, text="Resume", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=resumeEvent)
    resume = main_canvas.create_window(715, 251, window=resume)

    start = Button(main_canvas, text="New Game", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=newgameEvent)
    start = main_canvas.create_window(715, 309, window=start)

    online = Button(main_canvas, text="Online", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=comeOnline)
    online = main_canvas.create_window(715, 367, window=online)

    score = Button(main_canvas, text="Score Board", width=20, bg = "#E2EBEF", font="Helvetica 22", command=viewOldScores)
    score = main_canvas.create_window(715, 425, window=score)

    rules = Button(main_canvas, text="Rules", width=20, bg = "#E2EBEF",  font="Helvetica 22", command=viewRules)
    rules = main_canvas.create_window(715, 483, window=rules)

def mouseClick(e):
    print (e.x, e.y)

#_________________________________________________________________________________________________________________________
if __name__ == '__main__':

    global main_root, main_frame    
    main_root = Tk()
    main_frame = Frame(main_root)
    main_frame.pack()
    global main_canvas
    main_canvas = Canvas(main_frame, width=900, height=597)
    main_canvas.pack()

    #Import Image
    imgpath = "Welcome Page final.jpg"
    img = Image.open(imgpath)
    PHOTO = ImageTk.PhotoImage(img)

    #Create Canvas
    main_canvas.create_image(0, 0, image=PHOTO, anchor='nw')
    main_canvas.bind("<Button-1>", mouseClick)
    main_canvas.update()

    #Calling Functions
    initializeButtons()
        


