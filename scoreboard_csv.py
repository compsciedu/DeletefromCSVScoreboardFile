import csv

def readfromcsv(scoreboard_array):
    with open("scoreboard.csv", "r", newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            scoreboard_array.append(row)
    return scoreboard_array
    f.close()

def writetocsv(scoreboard_array):
    with open("scoreboard.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(scoreboard_array)
    print("File updated")
    f.close()

def search_array(scoreboard_array,remove_name):
    found = False
    for i in range(len(scoreboard_array)):
        if remove_name == scoreboard_array[i][0]:
            found = True
            scoreboard_array.remove(scoreboard_array[i])
    if found == False:
        print(remove_name,"is not in the scoreboard")
    else:
        return scoreboard_array
    
scoreboard_array = []
scoreboard_array = readfromcsv(scoreboard_array)
remove_name = input("User to Delete?")
scoreboard_array = search_array(scoreboard_array,remove_name)
scoreboard_array = writetocsv(scoreboard_array)
print("Finished")



     


