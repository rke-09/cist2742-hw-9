# Question 5

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

def make_column_order(keyword):
    order = []

    for i in range(len(keyword)):
        order.append(i)

    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            if keyword[order[i]] > keyword[order[j]]:
                order[i], order[j] = order[j], order[i]

    return order

def make_grid(message, rows, columns):
    grid = []
    index = 0

    for row in range(rows):
        new_row = []

        for col in range(columns):
            new_row.append(message[index])
            index += 1

        grid.append(new_row)

    return grid

def encrypt(message, keyword, rows, columns):
    message = message.upper()
    message = message.replace(" ", "")

    while len(message) < rows * columns:
        message += random.choice(string.ascii_uppercase)

    grid = make_grid(message, rows, columns)

    path = make_path(rows, columns)
    column_order = make_column_order(keyword)

    encrypted = ""

    for position in path:
        row = position[0]
        col = position[1]

        encrypted += grid[row][column_order[col]]

    return encrypted


def decrypt(ciphertext, keyword, rows, columns):

    grid = []

    for row in range(rows):
        new_row = []

        for col in range(columns):
            new_row.append("")

        grid.append(new_row)

    path = make_path(rows, columns)
    column_order = make_column_order(keyword)

    index = 0

    for position in path:
        row = position[0]
        col = position[1]

        grid[row][column_order[col]] = ciphertext[index]
        index += 1

    decrypted = ""

    for row in range(rows):
        for col in range(columns):
            decrypted += grid[row][col]

    return decrypted


def main():
    message = input("Enter a message: ")
    keyword = input("Enter a keyword: ")
    keyword = keyword.upper()

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    message = message.upper()
    message = message.replace(" ", "")

    if rows <= 0 or columns <= 0:
        print("Rows and columns must be positive.")
    elif len(keyword) != columns:
        print("Keyword length must equal the number of columns.")
    elif len(message) > rows * columns:
        print("Message is too long.")
    else:
        ciphertext = encrypt(message, keyword, rows, columns)
        print("Encrypted message:", ciphertext)

        plaintext = decrypt(ciphertext, keyword, rows, columns)
        print("Decrypted message:", plaintext)

main()