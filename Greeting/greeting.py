import curses
from curses import wrapper
import time

def Greeting(stdscr):
    stdscr.clear()
    greeting = "Chào thầy và tất cả các bạn"
    wishes = "Chúc thầy và các bạn một ngày vui vẻ"
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
            pad.addstr(18, idx+50, wishes[idx], curses.A_BOLD)
            idx += 1
            pad.refresh(18, 15, 10, 10, 10, idx  + 50)
        else:
            pad.addstr(15, i+50, greeting[i], curses.A_BOLD)
            pad.refresh(15, 15, 5, 5, 5, i+50)
        time.sleep(0.1)
    time.sleep(2)
    loop = 0
    while True:
        if loop == 3:
            break
        if count == 40:
            count = 0
            loop +=1
            continue
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, 0, 3, count, 10, 90 + count)
        count += 1
        time.sleep(0.1)


if __name__ == "__main__":
    wrapper(Greeting)