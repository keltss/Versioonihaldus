import turtle
import math
import time
# See funktsioon joonistab mangu laua, kus mangitakse
def drawBoard():
    #Joonista molemad horisontaalsed jooned, erinevatel korgustel
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)
#Joonista molemad vertikaalsed jooned
    drawer.right(90)
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)
#Lisa numbrid igasse kasti
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-200 + j * 200, 280 - i * 200)
            drawer.pendown()
            drawer.write(num, font=("Arial", 12))
            num += 1

#See funktsioon joonistab x'i sisestatud koordinaadi keskele
def drawX(x, y):
    #Liiguta oigesse kohta
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    drawer.setheading(60)
#Joonista x'i jooned
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
#Uuenda ekraani muudatustega
    drawer.getscreen().update()

#See funktsioon joonsitab O sisestatud koordinaadi keskele
def drawO(x, y):
    #Liiguta oigesse kohta
    drawer.penup()
    drawer.goto(x, y + 75)
    drawer.pendown()

    drawer.setheading(0)
#Joonista oige suurusega ring
    for i in range(180):
        drawer.forward((150 * math.pi) / 180)
        drawer.right(2)
#Uuenda ekraani muudatustega
    screen.update()

#See funktsioon kontrollib kas sisestatud mangija on voitnud
def checkWon(letter):
    #Kontrolli kas seal on horisontaalselt kolm jarjest
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == letter:
            return True
        if board[0][i] == board[1][i] == board[2][i] == letter:
            return True
#Kontrolli kas seal on vertikaalselt kolm jarjest alla
    if board[0][0] == board[1][1] == board[2][2] == letter:
        return True
#Kontrolli kas seal on vertikaalselt kolm jarjest tulp ules
    if board[0][2] == board[1][1] == board[2][0] == letter:
        return True
#Kui keegi pole voitnud
    return False

#See funktsioon paneb O koige paremasse kohta(et teha raskemaks voita)
def addO():
    time.sleep(1)
    #Kontrolli kas mingi koht tooks voidu O jaoks
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if checkWon("O"):
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " "
#Kontrolli kas on mingit kohta mida o voiks plokkida x'i
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "O"
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " "
#Proovi o panna esimesse vabasse nurka
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == " ":
                board[i][j] = "O"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return
#Pane o ukskoik kuhu vabasse kohta
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return

#See aktiveerib need
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i + 1))

#See funktsioon deaktiveerib nad
def deactivate():
    for i in range(9):
        screen.onkey(None, str(i + 1))

#See funktsioon proovib x'i oigesse kohta pigutada (sisestatud koordinaadi jargi)
def addX(row, column):
    #Kustuta koik teated ekraanilt
    announcer.clear()
#Kontrolli kas see koht kuhu nad tahavad panna on tais
    if board[row][column] == "x" or board[row][column] == "O":
        #Utle neile et see koht on voetud
        announcer.write("See koht on juba võetud!", font=("Arial", 36))
        screen.update()
    else:
        #joonista x oigesse kohta
        drawX(-200 + 200 * column, 200 - 200 * row)
        #lisa x arvuti mangulauale
        board[row][column] = "x"
#Kontrolli kas x voitis
    if checkWon("x"):
        #Utle mangijale et ta voitis
        announcer.goto(-97, 0)
        announcer.write("Sa võitsid!", font=("Arial", 36))
        #Uuenda ekraani ja deaktiveeri
        screen.update()
        deactivate()
    else:
        #Kui mangija ei voitnud siis O lisatakse mangulauale
        addO()
        screen.update()


def squareOne():
    addX(0, 0)


def squareTwo():
    addX(0, 1)


def squareThree():
    addX(0, 2)


def squareFour():
    addX(1, 0)


def squareFive():
    addX(1, 1)


def squareSix():
    addX(1, 2)


def squareSeven():
    addX(2, 0)


def squareEight():
    addX(2, 1)


def squareNine():
    addX(2, 2)

#Tee list nendest
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive, squareSix, squareSeven, squareEight, squareNine]

drawer = turtle.Turtle()
announcer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")

# Ekraan
screen = turtle.Screen()
screen.tracer(0)
#joonista mangulaud
drawBoard()

#tee mangulaud
board = [[" " for _ in range(3)] for _ in range(3)]

#Aktiveeri need
activate(functions)
screen.listen()
turtle.done()
