def emptyList(len):
    list = []
    for i in range (len):
        list.append("_")
    return list

def displayList(list):
    for i in range(len(list) - 1):
        print(list[i], end=" ")
    return list[-1]

def convertLowercase(char):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char = list(char)
    for i in range (len(char)):
        if char[i] not in lowercase and char[i] not in uppercase or len(char[i]) != 1:
            return 0
        elif char[i] in uppercase:
            k = 0
            while char[i] != uppercase[k]:
                k += 1
            char[i] = lowercase[k]
    return "".join(char)    

def pendu():
    while True:
        word = input("Entrez votre mot secret : ")
        word = convertLowercase(word)
        if word != 0:
            break
    grid = emptyList(len(word))
    print(displayList(grid))
    turn = len(word)
    while turn > 0:
        print("Il vous reste", turn, "tentative(s)")
        while True:
            guess = input("Entrez une lettre : ")
            guess = convertLowercase(guess)
            if guess != 0 and len(guess) == 1:
                state = False
                break
        for j in range(len(word)):
            if guess == word[j]:
                state = True
                grid[j] = guess
        if not state:
            turn -=1
        state = False
        print (displayList(grid))
        if "_" not in grid:
            return "Vous avez gagné le mot était " + word
    return "Vous avez perdu le mot était " + word
