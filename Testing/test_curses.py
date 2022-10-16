import curses
from curses import wrapper
import time

def main(stdscr):
    stdscr.clear()
    greeting = "Chào thầy và tất cả các bạn"
    wishes = "Chúc các bạn một ngày vui vẻ"
    heading = "AI - Greedy Algorithms - Exchange Currency - ATM Banking"
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    GREEN_COLOR = curses.color_pair(1)
    pad = curses.newpad(150, 150)
  

    pad.addstr(heading, GREEN_COLOR)
    length = len(greeting) + len(wishes)
    idx = 0
    count = 0
    isLoop = False
    for i in range(length):
        if i  >= len(greeting):
            pad.addstr(28, idx+90, wishes[idx], curses.A_BOLD)
            idx += 1
            pad.refresh(28, 25, 15, 15, 15, idx  + 90)
        else:
            pad.addstr(25, i+90, greeting[i], curses.A_BOLD)
            pad.refresh(25, 25, 10, 10, 10, i+90)
        time.sleep(0.1)
    time.sleep(1)
    while True:
        if count == 130:
            count = 0
            continue
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, 0, 3, count, 10, 70 + count)
        count += 1
        time.sleep(0.1)


if __name__ == "__main__":
    wrapper(main)