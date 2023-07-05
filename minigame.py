mapp = [["1", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"]]
lines = len(mapp)
vert = len(mapp[0])


def main():
    print(getpo())
    what = input("")
    if what != "q":
        control(what, getpo())
        showmapp()
        main()
    else:
        print("Thx ur playing!")


def showmapp():
    print("----------------------------")
    for i in range(lines):
        print(mapp[i])


def getpo():                                             # 0 --------> x +
    global x, y                                          # |
    r = []                                               # |
    for i in range(lines):                               # |
        try:                                             # y +
            r.append(mapp[i].index("1")+1)
        except:
            r.append(0)
    if r.count(0) != lines:
        for i in range(lines):  # which lines
            if r[i] != 0:
                x = r[i]     # the "1" horizon position
                y = i+1          # the "1" vertical position
        return [x, y]
    else:
        return [0, 0]


def control(wasd, coord):
    if wasd == "w":
        movew(coord)
    elif wasd == "a":
        movea(coord)
    elif wasd == "s":
        moves(coord)
    elif wasd == "d":
        moved(coord)


def dele(coord):   # lis = r
    mapp[coord[1]-1].pop(coord[0]-1)
    mapp[coord[1]-1].insert(coord[0]-1, "O")


def movew(coord):   # (x, y-1)
    newcoord = [coord[0], coord[1]-1]
    mapp[newcoord[1]-1].pop(newcoord[0]-1)
    mapp[newcoord[1]-1].insert(newcoord[0]-1, "1")
    dele(coord)


def movea(coord):   # (x-1, y)
    if coord[0]-1 == 0:
        newcoord = [vert, coord[1]]
    else:
        newcoord = [coord[0]-1, coord[1]]
    mapp[newcoord[1]-1].pop(newcoord[0]-1)
    mapp[newcoord[1]-1].insert(newcoord[0]-1, "1")
    dele(coord)

def moves(coord):   # (x, y+1)
    try:
        newcoord = [coord[0], coord[1]+1]
        mapp[newcoord[1]-1].pop(newcoord[0]-1)
    except:
        newcoord = [coord[0], 1]
        mapp[newcoord[1]-1].pop(newcoord[0]-1)
    mapp[newcoord[1]-1].insert(newcoord[0]-1, "1")
    dele(coord)

def moved(coord):   # (x+1, y)
    try:
        newcoord = [coord[0]+1, coord[1]]
        mapp[newcoord[1]-1].pop(newcoord[0]-1)
    except:
        newcoord = [1, coord[1]]
        mapp[newcoord[1]-1].pop(newcoord[0]-1)
    mapp[newcoord[1]-1].insert(newcoord[0]-1, "1")
    dele(coord)


showmapp()
main()

