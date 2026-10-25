# Question 1

from graphics import *
import time


def main():
    heights = []
    bounces = [0, 0, 0]
    balls = []
    colors = ["red", "blue", "green"]
    positions = [100, 200, 300]
    
    for i in range(3):
        height = float(input("Enter the initial height " + str(i + 1) + ": "))
        heights.append(height)

    win = GraphWin("Bouncing Balls", 400, 400)
    win.setCoords(0, 0, 400, 400)

    for i in range(3):
        ball = Circle(Point(positions[i], 20), 10)
        ball.setFill(colors[i])
        ball.draw(win)
        balls.append(ball)

    while max(heights) >= 0.001:
        for i in range(3):
            if heights[i] >= 0.001:
                distance = heights[i] * 10

                balls[i].move(0, distance)
                update()
                time.sleep(0.03)

                balls[i].move(0, -distance)
                update()
                time.sleep(0.03)
                
                heights[i] = heights[i] * 0.60
                bounces[i] = bounces[i] + 1

    for i in range(3):
        print("Ball", i + 1, "total bounces:", bounces[i])

    win.getMouse()
    win.close()

main()
