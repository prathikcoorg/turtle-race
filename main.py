from turtle import Turtle,Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width =500,height =400)
user_bet = screen.textinput(title ="make your bet",prompt ="which turtle will win thw race ? enter the color: " )
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
y_position= [-70, -30, 10, 50, 90, 130]
all_turtle =[]


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x =-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)



if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won {winning_color} turtle is winner")
            else:
                print(f"you lost !! , the {winning_color} turtle is the winner")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)








screen.exitonclick()