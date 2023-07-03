mapp = [["O", "O", "1", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "0", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"]]
lines = len(mapp)


def main():
    for i in range(lines):
        print(mapp[i])


def getpo():
    r = []
    for i in range(lines):
        try:
            r.append(mapp[i].index("1"))
        except:
            r.append(0)
    return r


def delself(lis):
    global po, i
    for i in range(lines):  # which lines
        if lis[i] != 0:
            po = lis[i]
    mapp.remove(i[po])
