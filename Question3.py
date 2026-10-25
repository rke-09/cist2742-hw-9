# Question 3

def encrypt(message, keyword):
    message = message.upper()
    message = message.replace(" ", "")
    keyword = keyword.upper()

    columns = len(keyword)
    rows = (len(message) + columns - 1) // columns

    while len(message) < rows * columns:
        message += "X"

    grid = []
    index = 0

    for row in range(rows):
        new_row = []

        for col in range(columns):
            new_row.append(message[index])
            index += 1

        grid.append(new_row)

    column_order = []

    for letter in sorted(keyword):
        column_order.append(keyword.index(letter))

    encrypted = ""

    for col in column_order:
        for row in range(rows):
            encrypted += grid[row][col]

    return encrypted

def decrypt(ciphertext, keyword):
    columns = len(keyword)
    rows = len(ciphertext) // columns

    column_order = []

    for letter in sorted(keyword):
        column_order.append(keyword.index(letter))

    grid = []

    for row in range(rows):
        new_row = []

        for col in range(columns):
            new_row.append("")

        grid.append(new_row)

    index = 0

    for col in column_order:
        for row in range(rows):
            grid[row][col] = ciphertext[index]
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

    ciphertext = encrypt(message, keyword)
    print("Encrypted message:", ciphertext)

    plaintext = decrypt(ciphertext, keyword)
    print("Decrypted message:", plaintext)

main()