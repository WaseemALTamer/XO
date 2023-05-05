global Gamebourd
Gamebourd = []
class game():
    def GetGame(x,y):
        global Gamebourd
        Gamebourd = []
        temp = []
        for i in range(0,y):
            for i in range(0,x):
                temp.append("0")
            Gamebourd.append(temp)
            temp = []
    def input(x,y,letter):
        Gamebourd[x][y] = letter
    def CheckLine(line):
        temp = 0
        for i in range (0,len(Gamebourd)):
            for j in range(0,len(Gamebourd[i])):
                if line == "H":
                    temp = temp + ord(Gamebourd[i][j])
                if line == "V":
                    temp = temp + ord(Gamebourd[j][i])
            if temp == 360:
                return [True ,360]
            if temp == 333:
                return [True ,333]
            else:
                temp = 0
        return [False, 0]
    def CheckCross():
        temp = 0
        temp = ord(Gamebourd[0][0]) + ord(Gamebourd[1][1]) + ord(Gamebourd[2][2])
        if temp == 360:
            return [True , 360]
        if temp == 333:
            return [True , 333]
        else:
            temp = 0
        temp = ord(Gamebourd[0][2]) + ord(Gamebourd[1][1]) + ord(Gamebourd[2][0])
        if temp == 360:
            return [True , 360]
        if temp == 333:
            return [True , 333]
        else:
            return [False, 0]
    def CheckDraw():
        temp = 0
        for i in range (0,len(Gamebourd)):
            for j in range(0,len(Gamebourd[i])):
                temp = temp + ord(Gamebourd[i][j])
        if temp == 1044 or temp == 1035:
            return [True , 1]
        else:
            return [False, 0]