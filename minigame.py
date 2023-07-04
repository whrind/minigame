mapp = [["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "1"]]
lines = len(mapp)


def main():
    showmapp()
    movew(getpo())
    showmapp()
    pass


def showmapp():
    print("----------------------------")
    for i in range(lines):
        print(mapp[i])


def getpo():                                             # 0 --------> x +
    global x, y                                          # |
    r = []                                               # |
    for i in range(lines):                               # |
        try:                                             # y +
            r.append(mapp[i].index("1"))
        except:
            r.append(0)
    for i in range(lines):  # which lines
        if r[i] != 0:
            x = r[i]     # the "1" horizon position
            y = i          # the "1" vertical position
    return [x, y]


def dele(coord):   # lis = r
    mapp[coord[1]].pop(coord[0])
    mapp[coord[1]].insert(coord[0], "O")


def movew(coord):   # (x, y-1)
    newcoord = [coord[0], coord[1]-1]
    mapp[newcoord[1]].pop(newcoord[0])
    mapp[newcoord[1]].insert(newcoord[0], "1")
    dele(coord)


main()

