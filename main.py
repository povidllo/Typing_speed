import curses
import random
from curses import wrapper

def main(stdscr):
    l = get_file()  # return a list of the sentenses
    text = get_text(l)  # return full text
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_GREEN, 0)
    curses.init_pair(2, curses.COLOR_RED, 0)

    stdscr.addstr(0,50,'Typing Speed')
    for i in range(len(text)):
        SYMBOLS = 0
        stdscr.addstr(1, 0, text[i] + '\n')

        SYMBOLS += typing(stdscr, text[i])  #add curret symbols

        stdscr.addstr(10, 10, 'Слов в минуту: ' + str(SYMBOLS))
        stdscr.refresh()

    stdscr.refresh()
    stdscr.getch()
    # stdscr = curses.initscr()


def typing(stdscr, text):
    SYMBOLS = 0
    # for letter in range(len(text)):
    #     w = stdscr.get_wch(1, letter)
    #     if w == '\n':
    #         break
    #     if str(w) == str(text[letter]):
    #         stdscr.addstr(1, letter, w, curses.color_pair(1))
    #         SYMBOLS += 1
    #     elif w == ' '
    #     else:
    #         stdscr.addstr(1, letter, w, curses.color_pair(2))
    position = 0
    while True:
        w = stdscr.get_wch(1, position)
        if str(w) == ']':
            continue
        if w == '\n':
            break
        if str(w) == str(text[position]) :
            stdscr.addstr(1, position, w, curses.color_pair(1))
            position += 1
            SYMBOLS += 1
        else:
            stdscr.addstr(1, position, w, curses.color_pair(2))
            position += 1

    # stdscr.addstr(text[letter], curses.A_UNDERLINE)
    return SYMBOLS


def get_text(l):  # return a list of the sentenses
    text = []
    first = random.randint(0, len(l) - 1)
    for i in range(first - 10, first):
        text.append(l[i])
    return text


def get_file():  # return full text
    with open('avidreaders.ru__mertvye-dushi.txt', encoding='utf-8') as file:
        l = [line.rstrip() for line in file.readlines()]
        l = "".join(l)
        l = l.replace('.', '.$').replace('?', '?$').replace('!', '!$').split('$')
    return l


if __name__ == '__main__':
    wrapper(main)
