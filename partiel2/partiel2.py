import re
import random

def readWord (file):
	file = open(file, "r", encoding="utf8")
	r = file.read()
	search = re.findall("nom=\".*?\"", r)
	result = []
	for nom in search:
		result.append(nom.replace("nom=","").replace("\"",""))
	return (result)

def randomWord(list):
	return random.choice(list)

def lifeLeft(mode,life):
	pendu = ["  =========\_/=" , "  ||/       | " , "  ||        0 ", "  ||       /|\ " , "  ||       /| " , " /||          " , " ==============" , ""]
	if mode == "f":
		print("Vie restantes :", life)
	elif mode == "m":
		print("Vie restantes :",end = " ")
		for i in range(life - 1):
			print("═", end="")
		print("═")
	elif mode == "d":
		for i in range(len(pendu) - life):
			print(pendu[i])
	return ""

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
        if char[i] not in lowercase and char[i] not in uppercase or len(char[i]) != 1 or len(char) == 0:
            return 0
        elif char[i] in uppercase:
            k = 0
            while char[i] != uppercase[k]:
                k += 1
            char[i] = lowercase[k]
    return "".join(char)    

def pendu():
    while True:
        mode = input("Entrez votre difficulté (f,m,d) : ")
        mode = convertLowercase(mode)
        word = randomWord(readWord("mots.txt")) #input("Entrez votre mot secret : ")
        word = convertLowercase(word)
        if word != 0 and mode == "f" or mode == "m" or mode == "d" :
            break
    grid = emptyList(len(word))
    print(displayList(grid))
    turn = 8 #turn = len(word)
    while turn > 0:
        lifeLeft(mode, turn)
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
            score = open("score.txt", "a")
            score.write("Victoire : " + word + " - " + str(turn) +" restant\n")
            score.close
            return "Vous avez gagné le mot était " + word
    print("  X    X  ")
    print("    ||    ")
    print("   /--\   ")
    score = open("score.txt", "a")
    score.write("Defaite : " + word + " - " + str(turn) + " restant\n")
    score.close
    return "Vous avez perdu le mot était " + word

print (pendu())