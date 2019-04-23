import curses
import random


class MathGame():

    font = {'0': [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            '1': [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            '2': [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            '3': [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            '4': [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            '5': [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            '6': [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            '7': [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            '8': [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            '9': [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            ' ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            '+': [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
            '-': [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            '=': [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            '?': [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
            '*': [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            '/': [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]}

    badges = { 0: '🐣',
               1: '🐥',
               2: '🦈',
               3: '🦉',
               4: '🐝',
               5: '🦕',
               6: '🦛',
               7: '🦓',
               8: '🐈',
               9: '🦖',
               10: '🦄'}


    def __init__(self, stdscr):
        self.screen = stdscr
        h, w = stdscr.getmaxyx()
        self.h = h
        self.w = w
        self.score = 0
        self.question = MathQuestion(1)
        self.main()

    def draw_number(self, x, y, char):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        gliph = MathGame.font[char]
        i = 0
        for dy in range(5):
            for dx in range(3):
                bit = gliph[i]
                if bit == 1:
                    self.screen.addstr(y + dy, x + dx, ' ', curses.color_pair(1))
                else:
                    self.screen.addstr(y + dy, x + dx, ' ', curses.color_pair(2))
                i = i + 1

    def draw_expresion(self, x, y, expresion):
        for ch in expresion:
            self.draw_number(x, y, ch)
            x = x + 4

    def main(self):
        expresion, result = self.question.generateQuestion()
        self.print_status()
        self.print_question(expresion)
        key = self.screen.getch()
        keys = []
        while key != ord('q') and key != 27:  # Escape
            if 48 <= key <= 57:
                keys.append(chr(key))
                self.echo_input(''.join(keys))
            elif key == 10:  # Enter
                self.screen.clear()
                user_response = 0
                try:
                    user_response = int(''.join(keys))
                except ValueError:
                    pass
                if user_response == result:
                    self.score = self.score + 1
                else:
                    self.score = self.score - 1
                expresion, result = self.question.generateQuestion()
                keys = []
                self.print_question(expresion)
                self.print_status()
                self.echo_input(''.join(keys))

            key = self.screen.getch()

    def echo_input(self, text):
        self.screen.addstr(self.h - 1, int(self.w/2), text, curses.A_REVERSE)

    def print_status(self):
        decenas = int(self.score / 10)
        self.screen.addstr(0, 0, "Nivel [{}]: {}".format(decenas, MathGame.badges[decenas]))

        if self.score >= 0:
            for i in range(0, self.score):
                self.screen.addstr(1 + i - int(i/5) * 5, int(i/5), MathGame.badges[int(i/10)])

        self.screen.addstr(self.h - 1, 0, "Para salir q/Esc | Score:  " + str(self.score))

    def print_question(self, expresion):
        x = int(self.w/2) - int((len(expresion) * 4)/2)
        y = int(self.h/2) - 3
        self.draw_expresion(x, y, expresion)
        self.screen.addstr(self.h - 1, int(self.w/2) - 2, "? ", curses.A_REVERSE)


class MathQuestion():

    operator = {0: '+',
                1: '-',
                2: '/',
                3: '*'}

    def __init__(self, level):
        self.level = level

    def generateQuestion(self):
        op = random.randint(0, 3)
        a = random.randint(0, self.level * 10)
        b = random.randint(0, self.level * 10)
        result = 0
        if op == 0:  # Add
            result = a + b
        elif op == 1:  # Sub
            result = a - b
        elif op == 2:  # Div
            if a < b:
                temp = a
                a = b
                b = temp
            if b == 0:
                b = 1
            result = int(a/b)
        else:
            result = a * b
        expresion = "{} {} {}".format(a, MathQuestion.operator[op], b)
        return expresion, result


def init_game(stdscr):
    MathGame(stdscr)


curses.wrapper(init_game)
