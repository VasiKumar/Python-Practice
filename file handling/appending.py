f = open("samosa.txt", "a")
f.write("\nbadhiya banaye guru")
f.close()

f = open("samosa.txt", "r")
data=f.read()
print(data)