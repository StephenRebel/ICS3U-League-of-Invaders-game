print("Enter 0 to quit!")
score_list = []
while True:

    #Get score and name
    score = int(input("Enter a score: "))
    if score == 0:
        break
    name = input("Enter a name: ")

    #Adds values to list
    namescore = [name, score]
    score_list.append(namescore)

    #Sorts all values
    for i in range(len(score_list)):
        smallest = score_list[i][1]
        for n in range(i, len(score_list)):
            if smallest > score_list[n][1]:
                score_list[i], score_list[n] = score_list[n], score_list[i]

while len(score_list) > 3:
    score_list.pop(0)

print(score_list)