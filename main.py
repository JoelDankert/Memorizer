import os

def first_letters(line,empty=0):
    if empty == 2:
        return " "*len(line)
    newline = ""
    excluded_chars = " -,.!?–\"\'&@…_()<>[]{}"
    for i,ch in enumerate(line):
        if ch == " ":
            newline += ch

        elif empty == 1:
            newline += "■"

        elif i == 0:
            newline += ch

        elif line[i-1] in excluded_chars:
            newline += ch

        elif ch in excluded_chars:
            newline += ch

        else:
            newline += "■"

        
    return newline

def improve_lines(lines):
    newlines = []
    for line in lines:
        if line == "\n":
            continue
        newlines.append(line.strip())
    return newlines

filename = input("filename\n> ")

with open(f"texts/{filename}","r") as f:
    lines = f.readlines()

lines = improve_lines(lines)

def main_loop():
    i = 0;
    while 1:
        os.system("clear")
        pos = int(i//3)
        if i % 3 == 0:
            print(first_letters(lines[pos],1))
        if i % 3 == 1:
            print(first_letters(lines[pos],0))
        elif i % 3 == 2:
            print(lines[pos])

        next = input();

        if next == "":
            i += 1
            if i >= len(lines)*2:
                i = 0
        if next == " " and i > 0:
            i -= 1
        if next == "b":
            return

main_loop()


