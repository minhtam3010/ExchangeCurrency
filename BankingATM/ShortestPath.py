import curses
from curses import wrapper
import queue
import time

class ShortestPath(object):

    def __init__(self):
        self.q = queue.Queue()
        self.label = {
            0: "Home district 2",
            1: "Sai Gon Bridge",
            2: "Thu Them Tunnel",
            3: "ATM Van Lang District 1",
            4: "ATM Van Lang Phan Van Tri",
            5: "ATM Van Lang Dang Thuy Tram"
        }

        self.distance = [
            [0, 15, 18, 0, 0, 0],
            [0, 0, 0, 18, 15, 0],
            [0, 0, 0, 10, 0, 0],
            [0, 0, 0, 0, 24, 32],
            [0, 0, 0, 0, 0, 8],
            [0, 0, 0, 0, 0, 0]
        ]

    def print_path(self, stdscr, path=[]):
        BLUE_COLOR = curses.color_pair(1)
        RED_COLOR = curses.color_pair(2)

        for i, row in enumerate(self.maze):
            for j, value in enumerate(row):
                if (i, j) in path:
                    stdscr.addstr(i, j*5, "X", RED_COLOR)
                else:
                    stdscr.addstr(i, j*5, "0", BLUE_COLOR)

    def find_start(self, start):
        for i, row, in enumerate(self.maze):
            for j, value in enumerate(row):
                if value == start:
                    return i, j
        return None

    def find_path(self, stdscr):
        start = "B"
        end = "F"
        start_pos = self.find_start(start)
        self.q.put((start_pos, [start_pos]))


        visited = set()
        
        while self.q.empty():
            current_pos, path = self.q.get()
            row, col = current_pos

            stdscr.clear()
            self.print_path(stdscr, path)
            time.sleep(0.2)
            stdscr.refresh()

            if self.maze[row][col] == end:
                return path
            neighbors = self.find_neighbors(row, col)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                
                new_path = path + [neighbor]
                self.q.put((neighbor, new_path))
                visited.add(neighbor)

    def find_neighbors(self, row, col):
        neighbors = []

        if row > 0: # UP
            neighbors.append((row - 1, col))
        if row + 1 < len(self.maze): # DOWN
            neighbors.append((row + 1, col))
        if col > 0: # LEFT
            neighbors.append((row, col - 1))
        if col + 1 < len(self.maze[0]): # RIGHT
            neighbors.append((row, col + 1))
        return neighbors



    def main(self, stdscr):
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        self.find_path(stdscr)
        stdscr.getch()


if __name__ == "__main__":
    sp = ShortestPath()
    wrapper(sp.main)


