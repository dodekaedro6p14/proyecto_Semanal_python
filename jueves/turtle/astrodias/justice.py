from turtle import *

# Paint half the screen black
color('black')
begin_fill()

# center of screen, turn right
right(90)
forward(window_height() // 2)

right(90)
forward(window_width() // 2)

right(90)
forward(window_height())

right(90)
forward(window_width() // 2)

right(90)
forward(window_height() // 2)

end_fill()
exitonclick()