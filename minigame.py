line0 = ["O", "O", "1", "O", "O"]
line1 = ["O", "O", "O", "O", "O"]
line2 = ["O", "O", "O", "O", "O"]
line3 = ["O", "O", "O", "O", "O"]
line4 = ["O", "O", "O", "0", "O"]
line5 = ["O", "O", "O", "O", "O"]
line6 = ["O", "O", "O", "O", "O"]
line7 = ["O", "O", "O", "O", "O"]


def main():
    print(f"{line0}\n{line1}\n{line2}\n{line3}\n"
          f"{line4}\n{line5}\n{line6}\n{line7}\n")


def getpo():
    r = [chec(line0), chec(line1), chec(line2), chec(line3),
         chec(line4), chec(line5), chec(line6), chec(line7)]
    print(r)


def chec(list):
    try:
        return list.index("1")
    except:
        return 0


getpo()
