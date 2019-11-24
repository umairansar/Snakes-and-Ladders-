#@15112
#Muhammad Umair Ansar   #mansar@andrew.cmu.edu
#Final Project          #First CheckPoint


#___________________MY CODE____________________________________________
from tkinter import *
from PIL import ImageTk, Image
import time
import random


class board():

    def __init__(self,root, player, secondP, Xbox, Ybox):
        self.canvas = root
        self.player = player
        self.secondP = secondP
        #self.thirdP = thirdP
        #self.fourthP = fourthP
        self.Xbox = Xbox
        self.Ybox = Ybox
        self.canvas.bind("<Button-1>", self.mouseClick)
        self.mycanvas = self.printToken()

    def mouseClick(self, e):
        print (e.x, e.y)

    def findBox(self, i): #Getting pixels for numbers/blocks
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

    #Print token on top of board
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

        #In case of 2 players
        if NumOfPlayers == 2:
            #Import token
            imgpath2 = self.player.getToken()
            img2 = Image.open(imgpath2)
            photo2 = ImageTk.PhotoImage(img2)

            X, Y = self.findBox(self.player.getPosition())
            token = self.canvas.create_image(X-c, Y-c, image=photo2, anchor='center')

            #Import token 2
            imgpath3 = self.secondP.getToken()
            img3 = Image.open(imgpath3)
            photo3 = ImageTk.PhotoImage(img3)

            X, Y = self.findBox(self.secondP.getPosition())
            token2 = self.canvas.create_image(X-c, Y-c, image=photo3, anchor='center')

        #In case of 3 players
        if NumOfPlayers == 3:
            #Import token
            imgpath2 = self.player.getToken()
            img2 = Image.open(imgpath2)
            photo2 = ImageTk.PhotoImage(img2)

            X, Y = self.findBox(self.player.getPosition())
            token = self.canvas.create_image(X-c, Y-c, image=photo2, anchor='center')

            #Import token 2
            imgpath3 = self.secondP.getToken()
            img3 = Image.open(imgpath3)
            photo3 = ImageTk.PhotoImage(img3)

            X, Y = self.findBox(self.secondP.getPosition())
            token2 = self.canvas.create_image(X-c, Y-c, image=photo3, anchor='center')

            #Import token 3
            imgpath4 = self.thirdP.getToken()
            img4 = Image.open(imgpath4)
            photo4 = ImageTk.PhotoImage(img4)

            X, Y = self.findBox(self.secondP.getPosition())
            token3 = self.canvas.create_image(X-c, Y-c, image=photo4, anchor='center')

        #In case of 4 players
        if NumOfPlayers == 4:
            #Import token
            imgpath2 = self.player.getToken()
            img2 = Image.open(imgpath2)
            photo2 = ImageTk.PhotoImage(img2)

            X, Y = self.findBox(self.player.getPosition())
            token = self.canvas.create_image(X-c, Y-c, image=photo2, anchor='center')

            #Import token 2
            imgpath3 = self.secondP.getToken()
            img3 = Image.open(imgpath3)
            photo3 = ImageTk.PhotoImage(img3)

            X, Y = self.findBox(self.secondP.getPosition())
            token2 = self.canvas.create_image(X-c, Y-c, image=photo3, anchor='center')

            #Import token 3
            imgpath4 = self.thirdP.getToken()
            img4 = Image.open(imgpath4)
            photo4 = ImageTk.PhotoImage(img4)

            X, Y = self.findBox(self.secondP.getPosition())
            token3 = self.canvas.create_image(X-c, Y-c, image=photo4, anchor='center')

            #Import token 4
            imgpath5 = self.fourthP.getToken()
            img5 = Image.open(imgpath5)
            photo5 = ImageTk.PhotoImage(img5)

            X, Y = self.findBox(self.secondP.getPosition())
            token4 = self.canvas.create_image(X-c, Y-c, image=photo5, anchor='center')
        

        self.canvas.update()
        
        time.sleep(1)
        print("check running ok!!")
        canvas = self.canvas
        
        return canvas

    def returnCanvas(self):
        return self.mycanvas
        

#_________________________________________________________________________    
class Game():
    def __init__(self, players, myDataFrame):
        #Snakes and Ladders dictionary
        self.salDict1 = dict()
        self.players = players
        self.point = IntVar()
        self.diceNum = 0
        self.diceBut = 0
        self.frame = myDataFrame

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

        #Calling Functions
        self.salDictionary()
        self.createScoreBoard()
        #self.gameMaster(self.players)

    def createScoreBoard(self):
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
                      text = "X",
                      fg = "red",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")

        #Score Player 2
        self.score1N = Label(self.frame,
                       text = "X",
                       fg = "orange",
                       width = 10,
                       height = 2,
                       font = "Helvetica 10 bold")

        #Score Player 3
        self.score2N = Label(self.frame,
                      text = "X",
                      fg = "blue",
                      width = 10,
                      height = 2,
                      font = "Helvetica 10 bold")

        #Score Player 4
        self.score3N = Label(self.frame,
                       text = "X",
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
                      text = "Player 1",
                      fg = "black",
                      width = 9,
                      height = 1,
                      font = "Helvetica 14 bold")
        self.diceNum.grid(row=14, column=0, columnspan=2)

        #Dice Button
        self.diceBut = Button(self.frame,
                         text="ROLL DICE",
                         relief="groove",
                         bg="white",
                         font="Helvetica 12 bold",
                         command=self.gameMaster(self.players))
        self.diceBut.config(anchor="w")
        self.diceBut.grid(row=15, column=0, columnspan=2)

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
        
    #Function to handle player turn
    def gameMaster(self, myPlayer):
        global winner
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

        #run dice rolls and movements
        if winner == False:
            totalPoints = 0
            print("\n----Player %i Hit enter to roll----" % myPlayer.getPlayerNum())
            self.info.insert(END,"\n----Player %i Hit enter to roll----" % myPlayer.getPlayerNum())
            #self.diceBut.wait_variable(self.point)
            point = self.throDice()
            totalPoints = point
            print("You rolled: %i" % point)
            self.info.insert(END,"You rolled: %i" % point)
            self.moveToken(myPlayer, point)
            if point == 6:
                #self.diceBut.wait_variable(self.point)
                point = self.throDice()
                totalPoints = totalPoints + point
                print("Bonus Turn: You rolled: %i" % point)
                self.info.insert(END, "You rolled: %i" % point)
                self.moveToken(myPlayer, point)
                if point == 6:
                    #self.diceBut.wait_variable(self.point)
                    point = self.throDice()
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
            else:
                self.checkPosition(myPlayer)

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
                winner = True
        self.updateScore()

    def rollDice(self):
        self.point = random.randint(1,6)
        self.diceNum["text"] = self.point
        print(self.point)

    def throDice(self):
        self.rollDice()    #to run uncomment this and comment wait ones
        #self.updateScore()
        return self.point

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

    def moveToken(self, myPlayer, points):
        possiblePosition = myPlayer.getPosition() + points
        if possiblePosition <= 100:
            myPlayer.updatePosition(possiblePosition)
            print("You are at the spot %i" % possiblePosition)
            self.info.insert(END, "You are at the spot %i" % possiblePosition)
        else:
            print("Your points are over the required limit.")
            self.info.insert(END,"Your points are over the required limit.")

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


        
#__________________________________________________________________________
class Player():
    def __init__(self, playerNum, token, color):
        self.token = token
        self.playerNum = playerNum
        self.playerPos = 0
        self.color = color

    def updatePosition(self, pos):
        self.playerPos = pos

    def getPosition(self):
        return self.playerPos

    def getPlayerNum(self):
        return self.playerNum

    def getToken(self):
        return self.token

    def getColor(self):
        return self.color
#_________________________________________________________________________

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
        self.canvas = Canvas(self.frame1, width=567, height=567)
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
        

        
#_________________________________________________________________________    
if __name__ == '__main__':

    #Create Window
    root = Tk()
    root.title("Snakes and Laders 2019")
    root.geometry("750x525")

    global NumOfPlayers
    NumOfPlayers = int(input("Please enter number of total players (=2)"))
    extension = "C:\\Users\\umair\\Desktop\\CS 112\\Project\\Boards\\"
    players = []
    tokens = [extension+"token.jpg", extension+"token2.jpg",
              extension+"token3.jpg", extension+"token5.jpg"]
    color = ["red", "yellow","blue", "green"]


    #Create Board
    create = createBoard(root)
    canvas = create.returnCanvasRN()

    #Get Block Dimensions
    Xbox, Ybox = create.returnDimensions()

    #Get Right Frame (to be populated)
    myDataFrame = create.returnFrame2()

    #Concat player objects into list
    for i in range(NumOfPlayers):
        players.append(Player(i+1, tokens[i], color[i])) #where i+1 denotes player number
    
    global winner
    global count
    count = 0
    winner = False                   

    while winner == False:
        for i in range(len(players)):
            if winner == False:
                count+=1
                start = Game(players[i], myDataFrame) #Start Game
                put = board(canvas, players[i], players[abs(i-1)], Xbox, Ybox) #Put it on board
                #temp = i
                #i = 
                #print(put.returnCanvas())

    

#____________________________END (2)______________________________________

