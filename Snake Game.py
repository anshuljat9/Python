import tkinter as tk
import random

window = tk.Tk()
window.title("Snake Game")
window.geometry("600x600")

canvas = tk.Canvas(window, width=600, height=600, bg="black")
canvas.pack()

snake = [(100, 100), (90, 100), (80, 100)]
direction = "Right"
food = (random.randint(0, 59) * 10, random.randint(0, 59) * 10)
game_over = False


def move():
    global snake, direction, food, game_over

    if game_over:
        return

    head_x, head_y = snake[0]

    if direction == "Up":
        new_head = (head_x, head_y - 10)
    elif direction == "Down":
        new_head = (head_x, head_y + 10)
    elif direction == "Left":
        new_head = (head_x - 10, head_y)
    else:
        new_head = (head_x + 10, head_y)

    # Wall collision
    if (new_head[0] < 0 or new_head[0] >= 600 or
            new_head[1] < 0 or new_head[1] >= 600):

        game_over = True

        canvas.create_text(
            300, 280,
            text="GAME OVER",
            fill="red",
            font=("Arial", 30)
        )

        canvas.create_text(
            300, 330,
            text="Press ENTER to restart",
            fill="white",
            font=("Arial", 18)
        )

        return

    # Snake collision
    if new_head in snake:

        game_over = True

        canvas.create_text(
            300, 280,
            text="GAME OVER",
            fill="red",
            font=("Arial", 30)
        )

        canvas.create_text(
            300, 330,
            text="Press ENTER to restart",
            fill="white",
            font=("Arial", 18)
        )

        return

    snake.insert(0, new_head)

    # Food
    if new_head == food:

        food = (
            random.randint(0, 59) * 10,
            random.randint(0, 59) * 10
        )

    else:
        snake.pop()

    # Draw snake
    canvas.delete("all")

    for x, y in snake:
        canvas.create_rectangle(
            x, y,
            x + 10, y + 10,
            fill="green"
        )

    # Draw food
    canvas.create_rectangle(
        food[0], food[1],
        food[0] + 10,
        food[1] + 10,
        fill="red"
    )

    window.after(100, move)


def change_direction(event):
    global direction

    if event.keysym == "Up" and direction != "Down":
        direction = "Up"

    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"

    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"

    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"


def restart(event):
    global snake, direction, food, game_over

    if event.keysym == "Return" and game_over:

        snake = [(100, 100), (90, 100), (80, 100)]
        direction = "Right"

        food = (
            random.randint(0, 59) * 10,
            random.randint(0, 59) * 10
        )

        game_over = False

        canvas.delete("all")

        move()


window.bind("<KeyPress>", change_direction)
window.bind("<Return>", restart)

move()

window.mainloop()