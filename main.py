from random import randint  # призываю рандом для дальнейших целей
import time
import turtle

username = input("Enter your username: ")  # здесь запрашиваю имя пользователя
if username == "splash" or username == "Splash":  # если юзернэйм равен Splash выйдет сообщение приведенное снизу
    turtle.clear()
    print("Welcome to Defuser, mr. Splash! Love to see you here!")
    turtle.bgcolor("black")
    turtle.color("white")
    style = ("FunGames", 25, "underline")
    turtle.write("Welcome to Defuser, mr. Splash! Love to see you here!", font=style, align="center")
    turtle.hideturtle()
    time.sleep(0.5)
else:
    turtle.clear()
    print(username, ",", "Welcome to DEFUSER on Python 3")  # тут юзернэйм не равен Splash
    turtle.bgcolor("black")
    turtle.color("white")
    style = ("FunGames", 25, "underline")
    turtle.write("Welcome to DEFUSER on Python 3", font=style, align="center")
    turtle.hideturtle()
    time.sleep(1.5)
score = 0  # переменная для зачисления очков

info = {  # эта переменная в которую записал dictionary с доп инфой
  "Splash": {"Full name": "Max Splash Hacicheant", "age": "13", "e-mail": "max.hacicheant@gmail.com"}
}

alive = True  # переменная для цикла while и в дальнейшем удобный tool
while alive:
    square = input(" Enter a number of a square from 1 to 8: ")  # запрашиваю число у юзера
    num_square = int(square)  # превращаю square в тип int
    square = num_square
    bomb_square = randint(1, 8)  # рандомное число из-за которого игра завершится
    if square > 8 or square < 1:      # если юзер будет читерить вводя числа > 8
        username = "Cheater"  # его никнейм измениться на приведенный в этой строке
        print("Not this time,", username)  # и выйдет это сообщение
        alive = False  # здесь игра завершится
        turtle.clear()
        turtle.bgcolor("black")
        turtle.color("white")
        style = ("FunGames", 45, "underline")
        turtle.write("Not this time, Cheater!", font=style, align="center")
        time.sleep(1.5)
        turtle.hideturtle()
    elif square == bomb_square:  # тут Game Over Script
        alive = False
        print("You are dead...  Your score is", score)  # здесь выводит набранное кол-во очков
        turtle.clear()
        turtle.bgcolor("black")
        turtle.color("white")
        style = ("Hellovetica", 55, "underline")
        turtle.write("You are dead...", font=style, align="center")
        time.sleep(3)
        turtle.clear()
        style = ("Hellovetica", 25, "underline")
        turtle.write("For some more information type 'info', if you want to leave type 'quit':", font=style, align="center")
        turtle.hideturtle()
        time.sleep(0.5)
        user_prompt = input("If you want to see some more information type 'info' or if you want to leave type 'quit': ")
        if user_prompt == "info":
            turtle.clear()
            print(list(info.items()))  # вывожу и листую доп инфу       # спрашиваю если юзер хочет доп инфу или уйти ^
        elif user_prompt == "quit":  # закрываю прогу
            turtle.clear()
            print("Closing program...")
            turtle.bgcolor("black")
            turtle.color("white")
            style = ("Hellovetica", 55, "underline")
            turtle.write("Closing program...", font=style, align="center")
            turtle.hideturtle()
            time.sleep(0.5)
        else:
            turtle.clear()
            print("Unknown command been received: Closing program...")  # вывожу это если не info и не quit
            turtle.bgcolor("black")
            turtle.color("white")
            style = ("Hellovetica", 25, "underline")
            turtle.write("Unknown command been received: Closing program...", font=style, align="center")
            time.sleep(0.5)
            turtle.hideturtle()
    else:
        turtle.clear()
        print("No bomb here")  # вывожу это если не попался
        turtle.bgcolor("black")
        turtle.color("white")
        style = ("Hellovetica", 55, "underline")
        turtle.write("No bomb here", font=style, align="center")
        turtle.hideturtle()
        time.sleep(0.5)
        score += 1  # начисляю пойнты
