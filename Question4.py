# Question 4 

import random
import string

def make_path(rows, columns):
    path = []

    for row in range(rows):
        if row % 2 == 0:
            for col in range(columns):
                path.append((row, col))
        else:
            for col in range(columns -1, -1, -1):
                path.append((row, col))

    return path


def encrypt(message, rows, columns, path):
    message = message.upper()
    message = message.replace(" ", "")

    while len(message) < rows * columns:
        message += random.choice(string.ascii_uppercase)

    grid = []
    index = 0

    for row in range(rows):
        new_row = []

        for col in range(columns):
            new_row.append(message[index])
            index += 1

        grid.append(new_row)

    encrypted = ""

    for position in path:
        row = position[0]
        col = position[1]

        encrypted += grid[row][col]

    return encrypted


def decrypt(ciphertext, rows, columns, path):

    grid = []

    for row in range(rows):
        new_row = []

        for col in range(columns):
            new_row.append("")

        grid.append(new_row)

    index = 0

    for position in path:
        row = position[0]
        col = position[1]

        grid[row][col] = ciphertext[index]
        index += 1

    decrypted = ""

    for row in range(rows):
        for col in range(columns):
            decrypted += grid[row][col]

    return decrypted


def main():
    rows = 5
    columns = 6

    message = input("Enter a message: ")

    message = message.upper()
    message = message.replace(" ", "")

    if len(message) > rows * columns:
        print("Message is too long.")
    else:
        path = make_path(rows, columns)

    ciphertext = encrypt(message, rows, columns, path)
    print("Encrypted message:", ciphertext)

    plaintext = decrypt(ciphertext, rows, columns, path)
    print("Decrypted message:", plaintext)

main()