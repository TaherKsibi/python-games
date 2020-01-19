#Yash Raja, Taher Ksibi, Aizaz Kayani
#January 18, 2017
#PocketPlay.py
#This program opens a main menu that allows the user to pick and click what game they want to play(either connect 4 or tic-tac-toe) and a player mode
#(Player V Player or Player V Ai). Next the program opens to the desired game and player mode. After the game window is opened the user has the option to press the
#back button to go back to the main menu.
#Once the a player or the Ai wins, a box in the middle of the window that givve the user(s) an option to play again.
#In the main menu there is an extra box for exiting the game. If the box/text is clicked is pressed all windows close and the program ends. 
#Test Cases: check Test Cases file in folder

from graphics import *
import time
import random

#PocketPlayMenu is a function that when called creates a Main Menu for Pocket Play
#It allows user to select what game they want to play and if they want to play
#against AI or against another player. The user can change the game by clicking a
#different game, the game starts when they click Play, the game closes when Exit is clicked
def PocketPlayMenu():
    #Creates Main Menu with boxes for each game and how many players
    try:
        main = GraphWin("Main Menu- PocketPlay", 1024, 700)
        main.setCoords(0,0,1024,700)
        background= Image(Point(512,350),"image3.png")
        background.draw(main)
        ptTitleM = Point(462, 615)
        ptBoardM1 = Point(250, 350)
        ptBoardM2 = Point(700,500)
        ptBoardM11 = Point(245,345)
        ptBoardM22 = Point(705, 505)
        ptLine1M = Point(470, 500)
        ptLine2M = Point(470, 350)
        boardM2 = Rectangle(ptBoardM11, ptBoardM22)
        boardM2.setFill('black')
        boardM2.draw(main)
        ptBoardM3 = Point(250,100)
        ptBoardM4 = Point(705,300)
        ptBoardM33= Point(245,90)
        ptBoardM44 = Point(710,310)
        boardM3 = Rectangle(ptBoardM33, ptBoardM44)
        boardM3.setFill('black')
        boardM3.draw(main)
        ptLine11M = Point(470, 300)
        ptLine22M = Point(470, 100)
        #Main Title
        titleM = Text(ptTitleM, "Pocket Play")
        titleM.setSize(36)
        titleM.setTextColor('orange')
        titleM.draw(main)
        boardM = Rectangle(ptBoardM1, ptLine1M)
        boardM2 = Rectangle(ptLine2M, ptBoardM2)
        boardM.setFill('blue')
        boardM.draw(main)
        boardM2.setFill('blue')
        boardM2.draw(main)
        boardM4 = Rectangle(ptBoardM3, ptLine11M)
        boardM5 = Rectangle(ptLine22M, ptBoardM4)
        boardM4.setFill('blue')
        boardM4.draw(main)
        boardM5.setFill('blue')
        boardM5.draw(main)
        ptGame1M = Point(350, 425)
        #Boxes to decide for type of game
        game1M = Text(ptGame1M, "Connect 4")
        game1M.setSize(25)
        game1M.setTextColor('yellow')
        game1M.draw(main)
        ptGame2M = Point(595, 425)
        game2M = Text(ptGame2M, "Tic-Tac-Toe")
        game2M.setSize(25)
        game2M.setTextColor('orange')
        game2M.draw(main)

        
        pt1PlayerM = Point(350, 200)
        #Boxes to select type of how many real players(1 or 2)
        player1M = Text(pt1PlayerM, "Player V AI")
        player1M.setSize(25)
        player1M.setTextColor('red')
        player1M.draw(main)
        pt2PlayerM = Point(590, 200)
        player2M = Text(pt2PlayerM, "Player V Player")
        player2M.setSize(25)
        player2M.setTextColor('red')
        player2M.draw(main)
        #Box and text to allow the player to exit the game
        ptExitBox1 = Point(250, 80)
        ptExitBox2 = Point(700, 25)
        exitBox = Rectangle(ptExitBox1, ptExitBox2)
        exitBox.setFill('yellow')
        exitBox.draw(main)
        ptExit = Point(465, 50)
        exitB = Text(ptExit, "Exit")
        exitB.setSize(25)
        exitB.setTextColor('red')
        exitB.draw(main)
        #Box and text to allow the player to start the game after selecting game and player mode
        ptPlayBox1 = Point(750, 400)
        ptPlayBox2 = Point(1000, 500)
        playBox = Rectangle(ptPlayBox1, ptPlayBox2)
        playBox.setFill('light green')
        playBox.draw(main)
        ptPlay= Point(875, 450)
        play = Text(ptPlay, "Play")
        play.setSize(35)
        play.setTextColor('white')
        play.draw(main)
        p = 0
        g = "no"
        play = False
        exitgame = False
        #Checking if user clicks play and doesnt exit,also reads what game user wants to play
        while not(play) and not(exitgame) and p != "no" and g != 0:
            mClick = main.getMouse()
            mClickX = mClick.getX()
            mClickY = mClick.getY()
            if mClickX >= 250 and mClickX < 470 and mClickY >= 350 and mClickY <= 500:
                g = "Connect4"
                game1M.undraw()
                game2M.undraw()
                boardM.undraw()
                boardM2.undraw()
                boardM.setFill('dark blue')
                boardM2.setFill('blue')
                boardM.draw(main)
                boardM2.draw(main)
                game1M.draw(main)
                game2M.draw(main)
            elif mClickX >= 470 and mClickX < 700 and mClickY >= 350 and mClickY <= 500:
                g = "TicTacToe"
                game1M.undraw()
                game2M.undraw()
                boardM.undraw()
                boardM2.undraw()
                boardM.setFill('blue')
                boardM2.setFill('dark blue')
                boardM.draw(main)
                boardM2.draw(main)
                game1M.draw(main)
                game2M.draw(main)
            elif mClickX >= 250 and mClickX < 470 and mClickY >= 100 and mClickY <= 300:
                p = 1
                player1M.undraw()
                player2M.undraw()
                boardM4.undraw()
                boardM5.undraw()
                boardM5.setFill('blue')
                boardM4.setFill('dark blue')
                boardM4.draw(main)
                boardM5.draw(main)
                player1M.draw(main)
                player2M.draw(main)
            elif mClickX >= 470 and mClickX < 700 and mClickY >= 100 and mClickY <= 300:
                p = 2
                player1M.undraw()
                player2M.undraw()
                boardM4.undraw()
                boardM5.undraw()
                boardM4.setFill('blue')
                boardM5.setFill('dark blue')
                boardM4.draw(main)
                boardM5.draw(main)
                player1M.draw(main)
                player2M.draw(main)
            elif mClickX >= 750 and mClickX < 1000 and mClickY >= 400 and mClickY <= 500:
                #If user clicks play without choosing game and players, it tells user to pick game and players
                if g != "no" and p != 0:
                    play = True
                else:
                    ptWarningBox = Point(499, 350)
                    ptGameAndPlayer1 = Point(308, 250)
                    ptGameAndPlayer2 = Point(680,430)
                    warningRect2 = Rectangle(ptGameAndPlayer1, ptGameAndPlayer2)
                    warningRect2.setFill("black")
                    warningRect2.draw(main)
                    if g == "no" and p == 0:
                        warning2 = Text(ptWarningBox,"Please select a game and a player mode")
                        warning2.setSize(14)
                        warning2.setTextColor("red")
                        warning2.draw(main)
                        time.sleep(1)
                        warning2.undraw()
                        warningRect2.undraw()
                    #If the user clicks a game but not a player mode, the program tells the user to pick a player mode
                    elif p == 0:
                        warning2 = Text(ptWarningBox,"Please select a player mode")
                        warning2.setSize(14)
                        warning2.setTextColor("red")
                        warning2.draw(main)
                        time.sleep(1)
                        warning2.undraw()
                        warningRect2.undraw()
                    #If the user clicks a player mode but not a game, the program tells the user to pick a game     
                    elif g == "no":
                        warning2 = Text(ptWarningBox,"Please select a game")
                        warning2.setSize(14)
                        warning2.setTextColor("red")
                        warning2.draw(main)
                        time.sleep(1)
                        warning2.undraw()
                        warningRect2.undraw()
            elif mClickX >= 250 and mClickX <= 700 and mClickY >= 25 and mClickY <= 80:
                p = 0
                g = "no"
                exitgame = True
        main.close()
        return g, p, exitgame
    except:
        exitgame = True
        return g, p, exitgame
#Warning - Creates a warning box in connect4 if they click of the connect4 board and not on back
def warning():
    ptWarning = Point(399,270)
    ptWarning1 = Point(228,180)
    ptWarning2 = Point(570,360)
    warningRect = Rectangle(ptWarning1,ptWarning2)
    warningRect.setFill("brown")
    warningRect.draw(con)
    warning = Text(ptWarning,"Please click on board")
    warning.setSize(24)
    warning.setTextColor("orange")
    warning.draw(con)
    time.sleep(1.5)
    warning.undraw()
    warningRect.undraw()
#Hor is a function that creates a list from the same index of all rows, showing the pieces from bottom to top
def hor(num):
    horizontal = []
    horizontal.append(row1[num])
    horizontal.append(row2[num])
    horizontal.append(row3[num])
    horizontal.append(row4[num])
    horizontal.append(row5[num])
    horizontal.append(row6[num])
    return horizontal
#Row is a function that is given a value which represents which row should be sent back
def row(p):
    if p == 1:
        row = list(row1)
    if p == 2:
        row = list(row2)
    if p == 3:
        row = list(row3)
    if p == 4:
        row = list(row4)
    if p == 5:
        row = list(row5)
    if p == 6:
        row = list(row6)
    return row
#Point of diagonal 1 lr 
def dPt1(aList, aRow, anIndex):
    list1 = [57 + 114*(anIndex), 45+90*(aRow-1)]
    aList.append(list1)
    return aList
#Point of diagonal 2 rl
def dPt2(aList, aRow, anIndex):
    list1 = [57 + 114*((anIndex)), 45+90*(aRow-1)]
    aList.append(list1)
    return aList
#A function that makes lists diagonally in connect 4 left to right
def dialr(w):
    dia = []
    if w == 1:
        dia.append(row(6)[0])
    if w == 2:
        dia.append(row(5)[0])
        dia.append(row(6)[1])
    if w == 3:
        dia.append(row(4)[0])
        dia.append(row(5)[1])
        dia.append(row(6)[2])
    if w == 4:
        dia.append(row(3)[0])
        dia.append(row(4)[1])
        dia.append(row(5)[2])
        dia.append(row(6)[3])
    if w == 5:
        dia.append(row(2)[0])
        dia.append(row(3)[1])
        dia.append(row(4)[2])
        dia.append(row(5)[3])
        dia.append(row(6)[4])
    if w == 6:
        dia.append(row(1)[0])
        dia.append(row(2)[1])
        dia.append(row(3)[2])
        dia.append(row(4)[3])
        dia.append(row(5)[4])
        dia.append(row(6)[5])
    if w == 7:
        dia.append(row(1)[1])
        dia.append(row(2)[2])
        dia.append(row(3)[3])
        dia.append(row(4)[4])
        dia.append(row(5)[5])
        dia.append(row(6)[6])
    if w == 8:
        dia.append(row(1)[2])
        dia.append(row(2)[3])
        dia.append(row(3)[4])
        dia.append(row(4)[5])
        dia.append(row(5)[6])
    if w == 9:
        dia.append(row(1)[3])
        dia.append(row(2)[4])
        dia.append(row(3)[5])
        dia.append(row(4)[6])
    if w == 10:
        dia.append(row(1)[4])
        dia.append(row(2)[5])
        dia.append(row(3)[6])
    if w == 11:
        dia.append(row(1)[5])
        dia.append(row(2)[6])
    if w == 12:
        dia.append(row(1)[5])
    return dia
#If the user gets 4 in a row diagonally left to right, this function will create a line crossing it out
def dialrPt(w):
    diaPt = []
    if w == 4:
        diaPt = dPt1(diaPt, 3, 0)
        diaPt = dPt1(diaPt, 4, 1)
        diaPt = dPt1(diaPt, 5, 2)
        diaPt = dPt1(diaPt, 6, 3)
    if w == 5:
        diaPt = dPt1(diaPt, 2, 0)
        diaPt = dPt1(diaPt, 3, 1)
        diaPt = dPt1(diaPt, 4, 2)
        diaPt = dPt1(diaPt, 5, 3)
        diaPt = dPt1(diaPt, 6, 4)
    if w == 6:
        diaPt = dPt1(diaPt, 1, 0)
        diaPt = dPt1(diaPt, 2, 1)
        diaPt = dPt1(diaPt, 3, 2)
        diaPt = dPt1(diaPt, 4, 3)
        diaPt = dPt1(diaPt, 5, 4)
        diaPt = dPt1(diaPt, 6, 5)
    if w == 7:
        diaPt = dPt1(diaPt, 1, 1)
        diaPt = dPt1(diaPt, 2, 2)
        diaPt = dPt1(diaPt, 3, 3)
        diaPt = dPt1(diaPt, 4, 4)
        diaPt = dPt1(diaPt, 5, 5)
        diaPt = dPt1(diaPt, 6, 6)
    if w == 8:
        diaPt = dPt1(diaPt, 1, 2)
        diaPt = dPt1(diaPt, 2, 3)
        diaPt = dPt1(diaPt, 3, 4)
        diaPt = dPt1(diaPt, 4, 5)
        diaPt = dPt1(diaPt, 5, 6)
    if w == 9:
        diaPt = dPt1(diaPt, 1, 3)
        diaPt = dPt1(diaPt, 2, 4)
        diaPt = dPt1(diaPt, 3, 5)
        diaPt = dPt1(diaPt, 4, 6)
    return diaPt
#This function creates lists in connect 4 from right to left
def diarl(w):
    dia = []
    if w == 1:
        dia.append(row(6)[6])
    if w == 2:
        dia.append(row(5)[6])
        dia.append(row(6)[5])
    if w == 3:
        dia.append(row(4)[6])
        dia.append(row(5)[5])
        dia.append(row(6)[4])
    if w == 4:
        dia.append(row(3)[6])
        dia.append(row(4)[5])
        dia.append(row(5)[4])
        dia.append(row(6)[3])
    if w == 5:
        dia.append(row(2)[6])
        dia.append(row(3)[5])
        dia.append(row(4)[4])
        dia.append(row(5)[3])
        dia.append(row(6)[2])
    if w == 6:
        dia.append(row(1)[6])
        dia.append(row(2)[5])
        dia.append(row(3)[4])
        dia.append(row(4)[3])
        dia.append(row(5)[2])
        dia.append(row(6)[1])
    if w == 7:
        dia.append(row(1)[5])
        dia.append(row(2)[4])
        dia.append(row(3)[3])
        dia.append(row(4)[2])
        dia.append(row(5)[1])
        dia.append(row(6)[0])
    if w == 8:
        dia.append(row(1)[4])
        dia.append(row(2)[3])
        dia.append(row(3)[2])
        dia.append(row(4)[1])
        dia.append(row(5)[0])
    if w == 9:
        dia.append(row(1)[3])
        dia.append(row(2)[2])
        dia.append(row(3)[1])
        dia.append(row(4)[0])
    if w == 10:
        dia.append(row(1)[2])
        dia.append(row(2)[1])
        dia.append(row(3)[0])
    if w == 11:
        dia.append(row(1)[1])
        dia.append(row(2)[0])
    if w == 12:
        dia.append(row(1)[0])
    return dia
#If the user gets 4 in a row diagonally right to left, this function will create a line crossing it out
def diarlPt(w):
    diaPt = []
    if w == 4:
        diaPt = dPt2(diaPt, 3, 6)
        diaPt = dPt2(diaPt, 4, 5)
        diaPt = dPt2(diaPt, 5, 4)
        diaPt = dPt2(diaPt, 6, 3)
    if w == 5:
        diaPt = dPt2(diaPt, 2, 6)
        diaPt = dPt2(diaPt, 3, 5)
        diaPt = dPt2(diaPt, 4, 4)
        diaPt = dPt2(diaPt, 5, 3)
        diaPt = dPt2(diaPt, 6, 2)
    if w == 6:
        diaPt = dPt2(diaPt, 1, 6)
        diaPt = dPt2(diaPt, 2, 5)
        diaPt = dPt2(diaPt, 3, 4)
        diaPt = dPt2(diaPt, 4, 3)
        diaPt = dPt2(diaPt, 5, 2)
        diaPt = dPt2(diaPt, 6, 1)
    if w == 7:
        diaPt = dPt2(diaPt, 1, 5)
        diaPt = dPt2(diaPt, 2, 4)
        diaPt = dPt2(diaPt, 3, 3)
        diaPt = dPt2(diaPt, 4, 2)
        diaPt = dPt2(diaPt, 5, 1)
        diaPt = dPt2(diaPt, 6, 0)
    if w == 8:
        diaPt = dPt2(diaPt, 1, 4)
        diaPt = dPt2(diaPt, 2, 3)
        diaPt = dPt2(diaPt, 3, 2)
        diaPt = dPt2(diaPt, 4, 1)
        diaPt = dPt2(diaPt, 5, 0)
    if w == 9:
        diaPt = dPt2(diaPt, 1, 3)
        diaPt = dPt2(diaPt, 2, 2)
        diaPt = dPt2(diaPt, 3, 1)
        diaPt = dPt2(diaPt, 4, 0)
    return diaPt
#TTTBoard is a fucntion that creates the window for tic tac toe, it is a graphics only function
#it helps the user to see what is happening and creates a 3*3 board for the to play on
def tttboard():
    #This is the background image, calling to it from the pocket play folder
    background= Image(Point(512,350),"image2.png")
    background.draw(ttt)
    #Makes board and title for Tic Tac Toe window
    ptBoard1 = Point(0,0)
    ptBoard2 = Point(798,540)
    ptTitle = Point(462,615)
    title = Text(ptTitle, "Tic Tac Toe")
    title.setSize(36)
    title.setTextColor('yellow')
    title.draw(ttt)
    board = Rectangle(ptBoard1, ptBoard2)
    board.draw(ttt)
    pthor1 = Point(324,525)
    pthor2 = Point(474,525)
    pthor1e = Point(324,75)
    pthor2e = Point(474,75)
    pthor1l = Line(pthor1,pthor1e)
    pthor2l = Line(pthor2, pthor2e)
    pthor1l.draw(ttt)
    pthor2l.draw(ttt)
    ptver1 = Point(174,225)
    ptver2 = Point(174,375)
    ptver1e = Point(624,225)
    ptver2e = Point(624,375)
    ptver1l = Line(ptver1, ptver1e)
    ptver2l = Line(ptver2, ptver2e)
    ptver1l.draw(ttt)
    ptver2l.draw(ttt)
    row1 = ["","",""]
    row2 = ["","",""]
    row3 = ["","",""]
    #This is drawing the backing button box and text, including point,size, and color. This is drawn in the tic tac toe window
    ptBackButton1 = Point(830, 670)
    ptBackButton2 = Point(970, 580)
    backButtonBox = Rectangle(ptBackButton1, ptBackButton2)
    backButtonBox.setFill('pink')
    backButtonBox.draw(ttt)
    ptBackButton = Point(900, 625)
    backButton = Text(ptBackButton, "Back")
    backButton.setSize(25)
    backButton.setTextColor('red')
    backButton.draw(ttt)
    #This is where the legend is mae for the tic tac toe board
    ptLegend1 = Point(798,0)
    ptLegend2 = Point(1023,540)
    legend = Rectangle(ptLegend1, ptLegend2)
    legend.setOutline('green')
    legend.draw(ttt)
    ptLegend = Point(900, 500)
    legend = Text(ptLegend, "Legend")
    legend.setSize(30)
    legend.setTextColor('black')
    legend.draw(ttt)

    #This is the circle inside the legend labeling player 2 or Ai
    ptCircleW = Point(850,350)
    circleW = Circle(ptCircleW, 30)
    circleW.setWidth(2)
    circleW.draw(ttt)
    #This is the "X" inside the legend labeling player 1
    Xf2 = Line(Point(825, 200),Point(875,150))
    Xs2 = Line(Point(875,200),Point(825,150))
    Xf2.setWidth(2)
    Xs2.setWidth(2)
    Xf2.draw(ttt)
    Xs2.draw(ttt)
    #This creates the "=" inside the legend
    for n in range(175,525,175):
        ptEqual2 = Point(900, n)
        equal2 = Text(ptEqual2, "=")
        equal2.setSize(36)
        equal2.setTextColor('black')
        equal2.draw(ttt)
    #Text to label the circle inside the legend(Ai, player2)
    ptP2 = Point(970, 350)
    if player == 1:
        p2 = Text(ptP2, "AI")
    if player == 2:
        p2 = Text(ptP2, "Player 2")
    p2.setSize(20)
    p2.setTextColor('blue')
    p2.draw(ttt)
    ptP2 = Point(970, 350)
    #Text to label the "X" inside the legend(player 1)
    ptP1 = Point(970, 175)
    p1 = Text(ptP1, "Player 1")
    p1.setSize(20)
    p1.setTextColor('red')
    p1.draw(ttt)
    return row1,row2,row3
#Thor is a horizontal function that is used for tic tac toe
#it makes a list of horizontal values using the same index and different rows
def thor(num):
    horizontal = []
    horizontal.append(trow1[num])
    horizontal.append(trow2[num])
    horizontal.append(trow3[num])
    return horizontal
#Trow is a function that represents the rows in tic tac toe
def trow(p):
    if p == 1:
        trow = list(trow1)
    if p == 2:
        trow = list(trow2)
    if p == 3:
        trow = list(trow3)
    return trow
#Warningt is a function that creates a warning box telling user to click on board and not outside
def warningt():
    ptWarning = Point(399,270)
    ptWarning1 = Point(228,180)
    ptWarning2 = Point(570,360)
    warningRect = Rectangle(ptWarning1,ptWarning2)
    warningRect.setFill("brown")
    warningRect.draw(ttt)
    warning = Text(ptWarning,"Please click on board")
    warning.setSize(24)
    warning.setTextColor("orange")
    warning.draw(ttt)
    time.sleep(1.5)
    warning.undraw()
    warningRect.undraw()
#Main Program
#Intialize variables
rematch = True
leave = False
yes = False
while rematch and not(leave): #Loops the game until user closes program or clicks exit
    #Sees if player wants rematch
    if not(yes):
        #Opens main menu and checks what game and player mode, and checks if the user wants to leave
        game, player, leave = PocketPlayMenu()
    #Sees if user wants to play connect 4
    if game == "Connect4":
        yes = False
        try:
            #Makes Connect 4 board and intialize variables specific to connect4, if rematch then refreshes variables
            backcon = False
            con = GraphWin("Connect4 - PocketPlay", 1024, 700)
            con.setCoords(0,0,1024,700)
            #Creates a packground
            background= Image(Point(512,350),"image1.png")
            background.draw(con)

            ptBoard1 = Point(0,0)
            ptBoard2 = Point(798,540)
            #Displays title
            ptTitle = Point(462,615)
            title = Text(ptTitle, "Connect 4")
            title.setSize(36)
            title.setTextColor('yellow')
            title.draw(con)
            board = Rectangle(ptBoard1, ptBoard2)
            board.setFill('blue')
            board.draw(con)

            ptWarning = Point(399,270)
            ptWarning1 = Point(228,180)
            ptWarning2 = Point(570,360)
            #Makes the connect4 board horizontally and verticall
            for i in range(114,798,114):
                ptLine1 = Point(i,0)
                ptLine2 = Point(i,540)
                line = Line(ptLine1, ptLine2)
                line.draw(con)
            for z in range(90,540,90):
                ptLineH1 = Point(0, z)
                ptLineH2 = Point(798, z)
                lineH = Line(ptLineH1, ptLineH2)
                lineH.draw(con)
            #Makes empty circles
            for k in range(57,855,114):
                for m in range(45,585,90):
                    ptCircle = Point(k,m)
                    circle = Circle(ptCircle, 30)
                    circle.setFill("white")
                    circle.draw(con)
            #Makes legend
            ptLegend1 = Point(798,0)
            ptLegend2 = Point(1023,540)
            legend = Rectangle(ptLegend1, ptLegend2)
            legend.setOutline('green')
            legend.draw(con)
            ptLegend = Point(900, 500)
            legend = Text(ptLegend, "Legend")
            legend.setSize(30)
            legend.setTextColor('white')
            legend.draw(con)
            won = False
            #Says what each icon means, in terms of what player
            ptCircleW = Point(850,400)
            circleW = Circle(ptCircleW, 30)
            circleW.setFill("white")
            circleW.draw(con)
            
            ptCircleR = Point(850,250)
            circleR = Circle(ptCircleR, 30)
            circleR.setFill("red")
            circleR.draw(con)

            ptCircleY = Point(850,100)
            circleY = Circle(ptCircleY, 30)
            circleY.setFill("yellow")
            circleY.draw(con)
            
            for n in range(100,550,150):
                ptEqual = Point(900, n)
                equal = Text(ptEqual, "=")
                equal.setSize(36)
                equal.setTextColor('white')
                equal.draw(con)

            ptEmpty = Point(970, 400)
            empty = Text(ptEmpty, "Empty")
            empty.setSize(20)
            empty.setTextColor('white')
            empty.draw(con)

            ptRed = Point(970, 250)
            red = Text(ptRed, "Player 1")
            red.setSize(20)
            red.setTextColor('red')
            red.draw(con)

            ptYellow = Point(970, 100)
            if player == 1:
                yellow = Text(ptYellow, "AI")
            if player == 2:
                yellow = Text(ptYellow, "Player 2")
            yellow.setSize(20)
            yellow.setTextColor('yellow')
            yellow.draw(con)
            #Creates Back Button graphic
            ptBackButton1 = Point(830, 670)
            ptBackButton2 = Point(970, 580)
            backButtonBox = Rectangle(ptBackButton1, ptBackButton2)
            backButtonBox.setFill('pink')
            backButtonBox.draw(con)
            ptBackButton = Point(900, 625)
            backButton = Text(ptBackButton, "Back")
            backButton.setSize(25)
            backButton.setTextColor('red')
            backButton.draw(con)
            #Intializes rows
            row6 = ["","","","","","",""]
            row5 = ["","","","","","",""]
            row4 = ["","","","","","",""]
            row3 = ["","","","","","",""]
            row2 = ["","","","","","",""]
            row1 = ["","","","","","",""]
            turn = 1
            end = False
            #Allows player to click and play the game
            while turn <= 42 and not(end):
                #If 1 player then changes turns between computer and user
                if player == 1:
                    if turn % 2 == 1:
                        click = con.getMouse()
                        clickX = click.getX()
                        clickY = click.getY()
                    else:
                        #Waits .2 sec before playing turn to make it seem like a real player
                        time.sleep(.2)
                        conAiNum = random.randint(0,6)
                        click = Point(57 + (114*conAiNum), 1)
                        clickX = click.getX()
                        clickY = click.getY()
                if player == 2:
                    #Alternates turns between 1st Player
                    click = con.getMouse()
                    clickX = click.getX()
                    clickY = click.getY()
                if clickX >= 830 and clickX <= 970 and clickY >= 580 and clickY <= 670:
                    #Checks if user clicks back in connect4
                    backcon = True
                else:
                    backcon = False
                if turn % 2 == 1:
                    red = True
                else:
                    red = False
                #Uses variables to determine where user has clicked, refreshes variables so it can do that
                xval = 0
                xClick = 1
                up = 0
                inboard = False
                for i in range(7):
                    #Checks in what row player has clicked, allows user to click above the board because it drops into the spot
                    xval += 114
                    if clickX < xval and clickX > xval - 114:
                        inboard = True
                        if red:
                            #Reads if player 1 and red Circles since it is player 1
                            if "" == row1[xClick-1]:
                                row1[xClick-1] = "red"
                                up = 1
                            elif "" == row2[xClick-1]:
                                row2[xClick-1] = "red"
                                up = 2
                            elif "" == row3[xClick-1]:
                                row3[xClick-1] = "red"
                                up = 3
                            elif "" == row4[xClick-1]:
                                row4[xClick-1] = "red"
                                up = 4
                            elif "" == row5[xClick-1]:
                                row5[xClick-1] = "red"
                                up = 5
                            elif "" == row6[xClick-1]:
                                row6[xClick-1] = "red"
                                up = 6
                            else:
                                turn -= 1
                            redCircle = Circle(Point(xval - 57,45+(90*(up-1))),30)
                            redCircle.setFill('red')
                            redCircle.draw(con)
                        else:
                            #Reads if player 2 and red Circles since it is player 2
                            if "" == row1[xClick-1]:
                                row1[xClick-1] = "yellow"
                                up = 1
                            elif "" == row2[xClick-1]:
                                row2[xClick-1] = "yellow"
                                up = 2
                            elif "" == row3[xClick-1]:
                                row3[xClick-1] = "yellow"
                                up = 3
                            elif "" == row4[xClick-1]:
                                row4[xClick-1] = "yellow"
                                up = 4
                            elif "" == row5[xClick-1]:
                                row5[xClick-1] = "yellow"
                                up = 5
                            elif "" == row6[xClick-1]:
                                row6[xClick-1] = "yellow"
                                up = 6
                            else:
                                turn -=1
                            yellowCircle = Circle(Point(xval - 57,45+(90*(up-1))),30)
                            yellowCircle.setWidth(2)
                            yellowCircle.setFill('yellow')
                            yellowCircle.draw(con)
                        turn += 1
                    
                    else:
                        xClick +=1
                if backcon:
                    #If back goes back to Main menu
                    break
                else:
                    if not(inboard):
                        #If user clicks outside of board says a warning
                        warning()
                    if inboard:
                        #Refreshes list of horizontal values every turn
                        hor7 = hor(6)
                        hor6 = hor(5)
                        hor5 = hor(4)
                        hor4 = hor(3)
                        hor3 = hor(2)
                        hor2 = hor(1)
                        hor1 = hor(0)
                        for z in range(0,7):
                            counter = 0
                            for n in range(0,5):
                                #Checks if player 1 or player2/ai has won horizontally
                                if hor(z)[n] == hor(z)[n+1] and hor(z)[n] != "":
                                    counter += 1
                                else:
                                    counter = 0
                                if counter == 1:
                                    #Creates Points to show user where they won
                                    ptLi1 = Point(57+114*(z),45+90*(n))
                                if counter == 3:
                                    won = True
                                    #Draws winning Line
                                    ptLi2 = Point(57+114*(z),45+90*(n+1))
                                    bo = Line(ptLi1, ptLi2)
                                    bo.draw(con)
                                    winTeam = str(hor(z)[n])
                                    
                        for z in range(1,7):
                            counter = 0
                            for n in range(0,6):
                                #Checks if anyone has won vertically
                                if row(z)[n] == row(z)[n+1] and row(z)[n] != "":
                                    counter += 1
                                else:
                                    counter = 0
                                if counter == 1:
                                    #Creates Points to show user where they won
                                    ptLine1 = Point(57+114*(n),45+90*(z-1))
                                if counter == 3:
                                    won = True
                                    #Draws winning Line
                                    ptLine2 = Point(57+114*(n+1),45+90*(z-1))
                                    li = Line(ptLine1, ptLine2)
                                    li.draw(con)
                                    winTeam = str(row(z)[n])
                                    
                        for z in range(1,13):
                            counter = 0
                            if len(dialr(z)) >= 4:
                                #Checks if user has won diagnoally from bottom left to top right
                                for n in range(0, (len(dialr(z))-1)):
                                    if dialr(z)[n] == dialr(z)[n+1] and dialr(z)[n] != "":
                                        counter += 1
                                    else:
                                        counter = 0
                                    if counter == 1:
                                        #Creates Points to show user where they won
                                        diaP = list(dialrPt(z)[n])
                                        ptDia = Point(diaP[0],diaP[1])
                                    if counter == 3:
                                        #Draws winning Line
                                        diaP = list(dialrPt(z)[n+1])
                                        ptDia1 = Point(diaP[0],diaP[1])
                                        di = Line(ptDia,ptDia1)
                                        di.draw(con)
                                        won = True
                                        winTeam = str(dialr(z)[n])
                                        break
                                if won:
                                    break             
                        for z in range(1,13):
                            counter = 0
                            if len(diarl(z)) >= 4:
                                #Checks if user has won diagnoally from top left to bottom right
                                for n in range(0, (len(diarl(z))-1)):
                                    if diarl(z)[n] == diarl(z)[n+1] and diarl(z)[n] != "":
                                        counter += 1
                                    else:
                                        counter = 0
                                    if counter == 1:
                                        #Draws winning Line
                                        diaP = list(diarlPt(z)[n])
                                        ptDia = Point(diaP[0],diaP[1])
                                    if counter == 3:
                                        #Draws winning Line
                                        diaP = list(diarlPt(z)[n+1])
                                        ptDia1 = Point(diaP[0],diaP[1])
                                        di = Line(ptDia,ptDia1)
                                        di.draw(con)
                                        won = True
                                        winTeam = str(diarl(z)[n])
                                        break
                        if won:
                            break
            #Checks if user has won, creates a box saying who has won                    
            if won:
                ptWinBox = Point(499, 350)
                ptWin1 = Point(308, 250)
                ptWin2 = Point(680,430)
                winRect = Rectangle(ptWin1, ptWin2)
                winRect.setFill("light pink")
                winRect.draw(con)
                if winTeam == "red":
                    winText = Text(ptWinBox,"Player 1 has won")
                    winText.setSize(22)
                    winText.setTextColor("red")
                    winText.draw(con)
                    time.sleep(3)
                    winText.undraw()
                    winRect.undraw()

                    ptTryBox = Point(499, 350)
                    ptTry1 = Point(308, 250)
                    ptTry2 = Point(680,430)
                    tryRect = Rectangle(ptWin1, ptWin2)
                    tryRect.setFill("light pink")
                    tryRect.draw(con)
                    #Creates a box that checks if user wants to play again or go back to main menu
                    tryText = Text(ptTryBox,"Do you want to play again?")
                    tryText.setSize(15)
                    tryText.setTextColor("red")
                    tryText.draw(con)
                    ptYesBox = Point(425, 300)
                    ptYes1 = Point(375,325)
                    ptYes2 = Point(475,275)
                    yesRect = Rectangle(ptYes1, ptYes2)
                    yesRect.setFill("white")
                    yesRect.draw(con)
                    yesText = Text(ptYesBox,"Yes")
                    yesText.setSize(15)
                    yesText.setTextColor("green")
                    yesText.draw(con)
                    ptNoBox = Point(575, 300)
                    ptNo1 = Point(525,325)
                    ptNo2 = Point(625,275)
                    noRect = Rectangle(ptNo1, ptNo2)
                    noRect.setFill("white")
                    noRect.draw(con)

                    noText = Text(ptNoBox,"No")
                    noText.setSize(15)
                    noText.setTextColor("red")
                    noText.draw(con)
                    yes = False
                    no = False
                    #Checks if user wants to play again or go back to main menu
                    while not(yes) and not(no):
                        yesNo = con.getMouse()
                        yesNoX = yesNo.getX()
                        yesNoY = yesNo.getY()
                        if yesNoX >= 375 and yesNoX <= 475 and yesNoY >=275 and yesNoY <= 325:
                            yes = True
                        elif yesNoX >= 525 and yesNoX <= 625 and yesNoY >=275 and yesNoY <= 325:
                            no = True
                        else:
                            ptPick = Point(499, 400)
                            pickText = Text(ptPick, "Please pick Yes or No")
                            pickText.setSize(20)
                            pickText.setTextColor("red")
                            pickText.draw(con)
                            time.sleep(2)
                            pickText.undraw()
                    if yes:
                        rematch = True
                    tryText.undraw()
                    tryRect.undraw()
                    yesRect.undraw()

                elif winTeam == "yellow":
                    if player == 1:
                        winText = Text(ptWinBox, "Ai has won")
                    if player == 2:
                        winText = Text(ptWinBox,"Player 2 has won")
                    winText.setSize(22)
                    winText.setTextColor("yellow")
                    winText.draw(con)
                    time.sleep(3)
                    winText.undraw()
                    winRect.undraw()
                    ptTryBox = Point(499, 350)
                    ptTry1 = Point(308, 250)
                    ptTry2 = Point(680,430)
                    tryRect = Rectangle(ptWin1, ptWin2)
                    tryRect.setFill("light pink")
                    tryRect.draw(con)

                    #Creates a box that checks if user wants to play again or go back to main menu
                    tryText = Text(ptTryBox,"Do you want to play again?")
                    tryText.setSize(15)
                    tryText.setTextColor("red")
                    tryText.draw(con)
                    ptYesBox = Point(425, 300)
                    ptYes1 = Point(375,325)
                    ptYes2 = Point(475,275)
                    yesRect = Rectangle(ptYes1, ptYes2)
                    yesRect.setFill("white")
                    yesRect.draw(con)
                    yesText = Text(ptYesBox,"Yes")
                    yesText.setSize(15)
                    yesText.setTextColor("green")
                    yesText.draw(con)
                    ptNoBox = Point(575, 300)
                    ptNo1 = Point(525,325)
                    ptNo2 = Point(625,275)
                    noRect = Rectangle(ptNo1, ptNo2)
                    noRect.setFill("white")
                    noRect.draw(con)

                    noText = Text(ptNoBox,"No")
                    noText.setSize(15)
                    noText.setTextColor("red")
                    noText.draw(con)
                    yes = False
                    no = False
                    #Checks if user wants to play again or go back to main menu
                    while not(yes) and not(no):
                        yesNo = con.getMouse()
                        yesNoX = yesNo.getX()
                        yesNoY = yesNo.getY()
                        if yesNoX >= 375 and yesNoX <= 475 and yesNoY >=275 and yesNoY <= 325:
                            yes = True
                        elif yesNoX >= 525 and yesNoX <= 625 and yesNoY >=275 and yesNoY <= 325:
                            no = True
                        else:
                            ptPick = Point(499, 400)
                            pickText = Text(ptPick, "Please pick Yes or No")
                            pickText.setSize(20)
                            pickText.setTextColor("red")
                            pickText.draw(con)
                            time.sleep(2)
                            pickText.undraw()
                    if yes:
                        rematch = True
                    tryText.undraw()
                    tryRect.undraw()
                    yesRect.undraw()
            elif not(won) and not(backcon):
                ptWinBox = Point(499, 350)
                ptWin1 = Point(308, 250)
                ptWin2 = Point(680,430)
                winRect = Rectangle(ptWin1, ptWin2)
                winRect.setFill("light pink")
                winRect.draw(con)
                winText = Text(ptWinBox,"Tie, No one wins")
                winText.setSize(22)
                winText.setTextColor("black")
                winText.draw(con)
                time.sleep(3)
                winText.undraw()
                winRect.undraw()
                
                #Creates a box that checks if user wants to play again or go back to main menu
                ptTryBox = Point(499, 350)
                ptTry1 = Point(308, 250)
                ptTry2 = Point(680,430)
                tryRect = Rectangle(ptWin1, ptWin2)
                tryRect.setFill("light pink")
                tryRect.draw(con)
                tryText = Text(ptTryBox,"Do you want to play again?")
                tryText.setSize(15)
                tryText.setTextColor("red")
                tryText.draw(con)
                ptYesBox = Point(425, 300)
                ptYes1 = Point(375,325)
                ptYes2 = Point(475,275)
                yesRect = Rectangle(ptYes1, ptYes2)
                yesRect.setFill("white")
                yesRect.draw(con)
                yesText = Text(ptYesBox,"Yes")
                yesText.setSize(15)
                yesText.setTextColor("green")
                yesText.draw(con)
                ptNoBox = Point(575, 300)
                ptNo1 = Point(525,325)
                ptNo2 = Point(625,275)
                noRect = Rectangle(ptNo1, ptNo2)
                noRect.setFill("white")
                noRect.draw(con)

                noText = Text(ptNoBox,"No")
                noText.setSize(15)
                noText.setTextColor("red")
                noText.draw(con)
                yes = False
                no = False
                #Checks if user wants to play again or go back to main menu
                while not(yes) and not(no):
                    yesNo = con.getMouse()
                    yesNoX = yesNo.getX()
                    yesNoY = yesNo.getY()
                    if yesNoX >= 375 and yesNoX <= 475 and yesNoY >=275 and yesNoY <= 325:
                        yes = True
                    elif yesNoX >= 525 and yesNoX <= 625 and yesNoY >=275 and yesNoY <= 325:
                        no = True
                    else:
                        ptPick = Point(499, 400)
                        pickText = Text(ptPick, "Please pick Yes or No")
                        pickText.setSize(20)
                        pickText.setTextColor("red")
                        pickText.draw(con)
                        time.sleep(2)
                        pickText.undraw()
                #if user wants to rematch then refreshes game with same players and games or else takes to main menu
                if yes:
                    rematch = True
                tryText.undraw()
                tryRect.undraw()
                yesRect.undraw()
            #Closes connect4
            con.close()
        except:
            #If user closes the game then doesn't cause error and ends the program
            leave = True
#Checks if user wants to play Tic Tac Toe
    if game == "TicTacToe":
        try:
            yes = False
            ttt = GraphWin("TicTacToe - PocketPlay", 1024, 700)
            ttt.setCoords(0,0,1024,700)
            trow1,trow2,trow3 = tttboard()
            thor0 = thor(0)
            thor1 = thor(1)
            thor2 = thor(2)
            wonT = False
            tturn = 1
            #While the user has not won and the turn is not 10
            while tturn <= 9 and not(wonT):
                if player == 1:   
                    if tturn % 2 == 1:
                        click = ttt.getMouse()
                        clickX = click.getX()
                        clickY = click.getY()
                    else:
                        time.sleep(.2)
                        lrList = []
                        lrList.append(trow1[0])
                        lrList.append(trow2[1])
                        lrList.append(trow3[2])
                        rlList = []
                        rlList.append(trow1[2])
                        rlList.append(trow2[1])
                        rlList.append(trow3[0])
                        
                        #Sees if user is about to win and blocks them
                        #Vertical check
                        if trow1[1] == trow1[2] and trow1[2] == "X" and trow1[0] == "":
                            click = Point(249,150)
                        elif trow1[0] == trow1[1] and trow1[1] == "X" and trow1[2] == "":
                            click = Point(549, 150)
                        elif trow1[0] == trow1[2] and trow1[0] == "X" and trow1[1] == "":
                            click = Point(399, 150)
                        elif trow2[1] == trow2[2] and trow2[2] == "X" and trow2[0] == "":
                            click = Point(249, 300)
                        elif trow2[0] == trow2[1] and trow2[1] == "X" and trow2[2] == "":
                             click = Point(549, 300)
                        elif trow2[0] == trow2[2] and trow2[0] == "X" and trow2[1] == "":
                            click = Point(399, 300)
                        elif trow3[1] == trow3[2] and trow3[2] == "X" and trow3[0] == "":
                            click = Point(249, 450)
                        elif trow3[0] == trow3[1] and trow3[1] == "X" and trow3[2] == "":
                            click = Point(549, 450)
                        elif trow3[0] == trow3[2] and trow3[0] == "X" and trow3[1] == "":
                            click = Point(399, 450)
                        #horizontal check
                        elif thor0[1] == thor0[2] and thor0[2] == "X" and thor0[0] == "":
                            click = Point(249, 150)                        
                        elif thor0[0] == thor0[1] and thor0[1] == "X" and thor0[2] == "":
                            click = Point(249,450)   
                        elif thor0[0] == thor0[2] and thor0[0] == "X" and thor0[1] == "":
                            click = Point(249,300)   
                        elif thor1[1] == thor1[2] and thor1[2] == "X" and thor1[0] == "":
                            click = Point(399,150) 
                        elif thor1[0] == thor1[1] and thor1[1] == "X" and thor1[2] == "":
                            click = Point(399, 300)
                        elif thor1[0] == thor1[2] and thor1[0] == "X" and thor1[1] == "":
                            click = Point(399, 450)
                        elif thor2[1] == thor2[2] and thor2[2] == "X" and thor2[0] == "":
                            click = Point(549, 150)
                        elif thor2[0] == thor2[1] and thor2[1] == "X" and thor2[2] == "":
                            click = Point(549, 300)
                        elif thor2[0] == thor2[2] and thor2[0] == "X" and thor2[1] == "":
                            click = Point(549, 450)

                        #Diagonal left to right check
                        elif lrList[1] == lrList[2] and lrList[2] == "X" and lrList[0] == "":
                            click = Point(249, 150)
                        elif lrList[0] == lrList[1] and lrList[1] == "X" and lrList[2] == "":
                            click = Point(549, 450)
                        elif lrList[0] == lrList[2] and lrList[0] == "X" and lrList[1] == "":
                            click = Point(399, 300)
                        #Diagonal right to left check
                        elif rlList[1] == rlList[2] and rlList[2] == "X" and rlList[0] == "":
                            click = Point(549, 150)
                        elif rlList[0] == rlList[1] and rlList[1] == "X" and rlList[2] == "":
                            click = Point(249, 450)
                        elif rlList[0] == rlList[2] and rlList[0] == "X" and rlList[1] == "":
                            click = Point(399, 300)
                        else:
                            #If user is not about to win then places randomly
                            tttAiNumX = random.randint(0,2)
                            tttAiNumY = random.randint(0,2)
                            click = Point(249 + (150*tttAiNumX), 150 + (150*tttAiNumY))
                        clickX = click.getX()
                        clickY = click.getY()
                if player == 2:
                    #Alternates turns between 2 players
                    click = ttt.getMouse()
                    clickX = click.getX()
                    clickY = click.getY()
                if clickX >= 830 and clickX <= 970 and clickY >= 580 and clickY <= 670:
                    #Checks if user clicks back
                    inBoard = True
                    backttt = True
                else:
                    backttt = False
                if tturn % 2 == 1:
                    X = True
                else:
                    X = False
                xval = 99
                xClick = 1
                up = 0
                inboard = False
                for i in range(3):
                    #Places player 1's piece and adds to position list
                    xval += 150
                    if clickX < xval+75 and clickX > xval - 75 and clickY >= 75 and clickY <= 525:
                        inboard = True
                        if X:  
                            draw = False
                            if "" == trow1[xClick-1] and clickY >= 75 and clickY < 225:
                                trow1[xClick-1] = "X"
                                up = 1
                                draw = True
                            elif clickY >= 75 and clickY < 225 and "" != trow1[xClick-1]:
                                tturn -= 1
                            if "" == trow2[xClick-1] and clickY >= 225 and clickY < 375:
                                trow2[xClick-1] = "X"
                                up = 2
                                draw = True
                            elif clickY >=225 and clickY < 375 and "" != trow2[xClick-1] :
                                tturn -= 1
                            if "" == trow3[xClick-1] and clickY >= 375 and clickY < 525:
                                trow3[xClick-1] = "X"
                                draw = True
                                up = 3
                            elif clickY >= 375 and clickY < 525 and "" != trow3[xClick-1]:
                                tturn -= 1
                            if draw:
                                X11 = Point(xval-50,150+(150*(up-1)+50))
                                X12 = Point(xval+50,150+(150*(up-1)-50))
                                X21 = Point(xval-50,150+(150*(up-1)-50))
                                X22 = Point(xval+50,150+(150*(up-1)+50))
                                Xf = Line(X11, X12)
                                Xs = Line(X21, X22)
                                Xf.setWidth(2)
                                Xs.setWidth(2)
                                Xf.draw(ttt)
                                Xs.draw(ttt)
                            draw = False
                        else:
                            #Places player 2's piece and adds to position list
                            if "" == trow1[xClick-1] and clickY >= 75 and clickY < 225:
                                trow1[xClick-1] = "O"
                                up = 1
                                draw = True
                            elif clickY >= 75 and clickY < 225 and "" != trow1[xClick-1]:
                                tturn -= 1
                            if "" == trow2[xClick-1] and clickY >= 225 and clickY < 375:
                                trow2[xClick-1] = "O"
                                up = 2
                                draw = True
                            elif clickY >= 225 and clickY < 375 and "" != trow2[xClick-1]:
                                tturn -= 1
                            if "" == trow3[xClick-1] and clickY >= 375 and clickY < 525:
                                trow3[xClick-1] = "O"
                                up = 3
                                draw = True
                            elif clickY >= 375 and clickY < 525 and "" != trow3[xClick-1]:
                                tturn -= 1
                            if draw:
                                O = Circle(Point(xval,150+(150*(up-1))),35)
                                O.setWidth(2)
                                O.draw(ttt)
                            draw = False

                        tturn += 1
                    else:
                        xClick +=1
                if backttt:
                    #Goes back to main menu
                    break
                else:
                    if not(inboard):
                        #if player is not clicking on the tic tac toe board, gives warning telling to click on board
                        warningt()
                    if inboard:
                        for z in range(0,3):
                            counter = 0
                            for n in range(0,2):
                                #Checks if user has 1 horizontally
                                if thor(z)[n] == thor(z)[n+1] and thor(z)[n] != "":
                                    counter += 1
                                else:
                                    counter = 0
                                if counter == 1:
                                    ptLi1 = Point(249+150*(z),(150+150*(n))-75)
                                if counter == 2:
                                    wonT = True
                                    ptLi2 = Point(249+150*(z),(150+150*(n+1))+75)
                                    bo = Line(ptLi1, ptLi2)
                                    bo.draw(ttt)
                                    symbol = str(thor(z)[n])
                            if wonT:
                                break
                        for z in range(1,4):
                            counter = 0
                            for n in range(0,2):
                                #Checks if user has 1 vertically
                                if trow(z)[n] == trow(z)[n+1] and trow(z)[n] != "":
                                    counter += 1
                                else:
                                    counter = 0
                                if counter == 1:
                                    ptLine1 = Point((249+150*(n))-75,150+150*(z-1))
                                if counter == 2:
                                    wonT = True
                                    ptLine2 = Point((249+150*(n+1))+75,150+150*(z-1))
                                    li = Line(ptLine1, ptLine2)
                                    li.draw(ttt)
                                    symbol = str(trow(z)[n])
                                    w = "row"
                            if wonT:
                                break
                        #Checks if user has left to right diagonally
                        if trow1[0] == trow2[1] and trow2[1] == trow3[2] and trow1[0] != "":
                            ptLine1 = Point(199,100)
                            ptLine2 = Point(599,500)
                            li = Line(ptLine1, ptLine2)
                            li.setWidth(3)
                            li.draw(ttt)
                            symbol = trow1[0]
                            wonT = True
                        if wonT:
                            break
                        #Checks if user has right to left diagonally
                        if trow1[2] == trow2[1] and trow2[1] == trow3[0] and trow1[2] != "":
                            ptLine1 = Point(599,100)
                            ptLine2 = Point(199,500)
                            li = Line(ptLine1, ptLine2)
                            li.setWidth(5)
                            li.draw(ttt)
                            symbol = trow1[2]
                            wonT = True
            if wonT:
                #Creates a box in the middle of the window that says who won between
                #player 1 and player 2/ai
                ptWinBox = Point(499, 350)
                ptWin1 = Point(308, 250)
                ptWin2 = Point(680,430)
                winRect = Rectangle(ptWin1, ptWin2)
                winRect.setFill("light pink")
                winRect.draw(ttt)
                if symbol == "X":
                    winText = Text(ptWinBox,"Player 1 has won")
                    winText.setSize(22)
                    winText.setTextColor("red")
                    winText.draw(ttt)
                    time.sleep(3)
                    winText.undraw()
                    winRect.undraw()
                    ptTryBox = Point(499, 350)
                    ptTry1 = Point(308, 250)
                    ptTry2 = Point(680,430)
                    tryRect = Rectangle(ptWin1, ptWin2)
                    tryRect.setFill("light pink")
                    tryRect.draw(ttt)
                    #Asks if user wants to play again
                    tryText = Text(ptTryBox,"Do you want to play again?")
                    tryText.setSize(15)
                    tryText.setTextColor("red")
                    tryText.draw(ttt)
                    ptYesBox = Point(425, 300)
                    ptYes1 = Point(375,325)
                    ptYes2 = Point(475,275)
                    yesRect = Rectangle(ptYes1, ptYes2)
                    yesRect.setFill("white")
                    yesRect.draw(ttt)
                    yesText = Text(ptYesBox,"Yes")
                    yesText.setSize(15)
                    yesText.setTextColor("green")
                    yesText.draw(ttt)
                    ptNoBox = Point(575, 300)
                    ptNo1 = Point(525,325)
                    ptNo2 = Point(625,275)
                    noRect = Rectangle(ptNo1, ptNo2)
                    noRect.setFill("white")
                    noRect.draw(ttt)

                    noText = Text(ptNoBox,"No")
                    noText.setSize(15)
                    noText.setTextColor("red")
                    noText.draw(ttt)
                    yes = False
                    no = False
                    while not(yes) and not(no):
                        #If user presses no takes back to main menu
                        #If yes resets the game board
                        yesNo = ttt.getMouse()
                        yesNoX = yesNo.getX()
                        yesNoY = yesNo.getY()
                        if yesNoX >= 375 and yesNoX <= 475 and yesNoY >=275 and yesNoY <= 325:
                            yes = True
                        elif yesNoX >= 525 and yesNoX <= 625 and yesNoY >=275 and yesNoY <= 325:
                            no = True
                        else:
                            ptPick = Point(499, 400)
                            pickText = Text(ptPick, "Please pick Yes or No")
                            pickText.setSize(20)
                            pickText.setTextColor("red")
                            pickText.draw(ttt)
                            time.sleep(2)
                            pickText.undraw()
                elif symbol == "O":
                    if player == 1:
                        winText = Text(ptWinBox, "AI has won")
                    if player == 2:
                        winText = Text(ptWinBox,"Player 2 has won")
                    winText.setSize(22)
                    winText.setTextColor("red")
                    winText.draw(ttt)
                    time.sleep(3)
                    winText.undraw()
                    winRect.undraw()
                    ptTryBox = Point(499, 350)
                    ptTry1 = Point(308, 250)
                    ptTry2 = Point(680,430)
                    tryRect = Rectangle(ptWin1, ptWin2)
                    tryRect.setFill("light pink")
                    tryRect.draw(ttt)
                    #Asks if user wants to play again
                    tryText = Text(ptTryBox,"Do you want to play again?")
                    tryText.setSize(15)
                    tryText.setTextColor("red")
                    tryText.draw(ttt)
                    ptYesBox = Point(425, 300)
                    ptYes1 = Point(375,325)
                    ptYes2 = Point(475,275)
                    yesRect = Rectangle(ptYes1, ptYes2)
                    yesRect.setFill("white")
                    yesRect.draw(ttt)
                    yesText = Text(ptYesBox,"Yes")
                    yesText.setSize(15)
                    yesText.setTextColor("green")
                    yesText.draw(ttt)
                    ptNoBox = Point(575, 300)
                    ptNo1 = Point(525,325)
                    ptNo2 = Point(625,275)
                    noRect = Rectangle(ptNo1, ptNo2)
                    noRect.setFill("white")
                    noRect.draw(ttt)

                    noText = Text(ptNoBox,"No")
                    noText.setSize(15)
                    noText.setTextColor("red")
                    noText.draw(ttt)
                    yes = False
                    no = False
                    while not(yes) and not(no):
                        #If user presses no takes back to main menu
                        #If yes resets the game board
                        yesNo = ttt.getMouse()
                        yesNoX = yesNo.getX()
                        yesNoY = yesNo.getY()
                        if yesNoX >= 375 and yesNoX <= 475 and yesNoY >=275 and yesNoY <= 325:
                            yes = True
                        elif yesNoX >= 525 and yesNoX <= 625 and yesNoY >=275 and yesNoY <= 325:
                            no = True
                        else:
                            ptPick = Point(499, 400)
                            pickText = Text(ptPick, "Please pick Yes or No")
                            pickText.setSize(20)
                            pickText.setTextColor("red")
                            pickText.draw(ttt)
                            time.sleep(2)
                            pickText.undraw()
                    if yes:
                        rematch = True
                    tryText.undraw()
                    tryRect.undraw()
                    yesRect.undraw()
            elif not(wonT) and not(backttt):
                #If no one wins then displays a box that says "Tie, no one wins"
                ptWinBox = Point(499, 350)
                ptWin1 = Point(308, 250)
                ptWin2 = Point(680,430)
                winRect = Rectangle(ptWin1, ptWin2)
                winRect.setFill("light pink")
                winRect.draw(ttt)
                winText = Text(ptWinBox,"Tie, No one wins")
                winText.setSize(22)
                winText.setTextColor("red")
                winText.draw(ttt) 
                time.sleep(3)
                winText.undraw()
                winRect.undraw()
                ptTryBox = Point(499, 350)
                ptTry1 = Point(308, 250)
                ptTry2 = Point(680,430)
                tryRect = Rectangle(ptWin1, ptWin2)
                tryRect.setFill("light pink")
                tryRect.draw(ttt)
                #Asks user if you want to play again
                tryText = Text(ptTryBox,"Do you want to play again?")
                tryText.setSize(15)
                tryText.setTextColor("red")
                tryText.draw(ttt)
                ptYesBox = Point(425, 300)
                ptYes1 = Point(375,325)
                ptYes2 = Point(475,275)
                yesRect = Rectangle(ptYes1, ptYes2)
                yesRect.setFill("white")
                yesRect.draw(ttt)
                yesText = Text(ptYesBox,"Yes")
                yesText.setSize(15)
                yesText.setTextColor("green")
                yesText.draw(ttt)
                ptNoBox = Point(575, 300)
                ptNo1 = Point(525,325)
                ptNo2 = Point(625,275)
                noRect = Rectangle(ptNo1, ptNo2)
                noRect.setFill("white")
                noRect.draw(ttt)

                noText = Text(ptNoBox,"No")
                noText.setSize(15)
                noText.setTextColor("red")
                noText.draw(ttt)
                yes = False
                no = False
                while not(yes) and not(no):
                    #If user presses no takes back to main menu
                    #If yes resets the game board
                    yesNo = ttt.getMouse()
                    yesNoX = yesNo.getX()
                    yesNoY = yesNo.getY()
                    if yesNoX >= 375 and yesNoX <= 475 and yesNoY >=275 and yesNoY <= 325:
                        yes = True
                    elif yesNoX >= 525 and yesNoX <= 625 and yesNoY >=275 and yesNoY <= 325:
                        no = True
                    else:
                        ptPick = Point(499, 400)
                        pickText = Text(ptPick, "Please pick Yes or No")
                        pickText.setSize(20)
                        pickText.setTextColor("red")
                        pickText.draw(ttt)
                        time.sleep(2)
                        pickText.undraw()
                if yes:
                    rematch = True
                tryText.undraw()
                tryRect.undraw()
                yesRect.undraw()
            ttt.close()
        except:
            #If user closes window then leaves game
            leave = True
#Ends program with a print statement
print("Thank you for playing Pocket Play")
