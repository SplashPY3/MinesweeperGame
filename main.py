import time
import turtle

process = 0

while process < 100:
    print("Hacking NASA...", process, "% done:")
    process += 10
    time.sleep(2.5)

if process >= 100:
    print("NASA Hacked Successfully:")
    turtle.bgcolor("black")
    turtle.color("dark green")
    style = ("Papyrus", 70, "underline")
    turtle.write("NASA Hacked Successfully!", font=style, align="center")
    turtle.hideturtle()
    time.sleep(10)
