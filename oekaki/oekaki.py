"""oekaki
"""

import tkinter as tk


class Oekaki(tk.Frame):
    def __init__(self, width=1350, height=670, bg='black', fg='white', line=30):
        self.master = tk.Tk()
        super().__init__(self.master)
        self.pack()
        self.master.title('Oekaki')

        # canvas
        self.canvas = tk.Canvas(self, width=width, height=height, bg=bg)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind('<Button1-Motion>', self.draw)

        # clear button
        self.clearbtn = tk.Button(self, text='Clear', command=self.clear)
        self.clearbtn.grid(row=1, column=0)

        # line width
        self.line = line

        # line color
        self.fg = fg

    def draw(self, event):
        x, y, w = event.x, event.y, self.line
        oval = self.canvas.create_oval(x-w/2, y-w/2, x+w/2, y+w/2)
        self.canvas.itemconfigure(oval, fill=self.fg, outline=self.fg)

    def clear(self):
        self.canvas.delete('all')

    def start(self):
        self.master.mainloop()


def start_oekaki():
    Oekaki().start()


if __name__ == '__main__':
    start_oekaki()
