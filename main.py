import os
import sys
import termios
import tty

def first_letters(line,empty=0):
    if empty == 3:
        return " "*len(line)
    newline = ""
    excluded_chars = " -,.!?–\"\'&@…_()<>[]{}0123456789"
    for i,ch in enumerate(line):
        if ch == " ":
            newline += ch

        elif empty == 2: # empty 1
            newline += "■"

        elif ch in excluded_chars:
            newline += ch

        elif empty == 1: # empty 2
            newline += "■"

        elif i == 0:
            newline += ch

        elif line[i-1] in excluded_chars:
            newline += ch

        else: # rest
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

def read_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def main_loop():
    i = 0;
    stages = 3
    while 1:
        os.system("clear")
        pos = int(i//stages)
        total_steps = len(lines) * stages
        progress = int(((i + 1) / total_steps) * 100)
        red = int(255 * (100 - progress) / 100)
        green = int(255 * progress / 100)
        color = f"\033[38;2;{red};{green};0m"
        print(f"{color}{progress}%\033[0m")
        if i % stages == 0:
            print(lines[pos])
        elif i % stages == 1:
            print(first_letters(lines[pos],0))
        elif i % stages == 2:
            print(first_letters(lines[pos],1))

        next = read_key()

        if next in ("\n", "\r"):
            i += 1
            if i >= len(lines)*stages:
                i = 0
        if next == " " and i > 0:
            i -= 1
        if next == "q":
            return

main_loop()
