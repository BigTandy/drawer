import tkinter as tk
import random as rand
import asyncio
import math as m
from lookaround import buildLookAround
from pprint import pprint

pprint(buildLookAround(1, 1), width=120)

def hexcode():
    out = "#"
    r = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    for _ in range(6):
        out += str(rand.choice(r))
    return out


XSIZE = 500
YSIZE = 500

window = tk.Tk()
can = tk.Canvas(width=XSIZE, height=YSIZE)
can.pack()
photo = tk.PhotoImage(width=XSIZE, height=YSIZE)
can.create_image((XSIZE/2, YSIZE/2), image=photo, state="normal")


class turt:
    alive = set()
    def __init__(self, *, ran=False, col=False, tron=False, superran=False):
        self.id = ...#TODO
        self.color = hexcode()
        self.x = rand.randint(0, 500)
        self.y = rand.randint(0, 500)
        #self.vec = [.2, .2]
        self.tron = tron
        if False:#tron:
            self.vec = [.2, 0]
        else:
            #self.vec = [.35, .35]
            #self.vec = [.4, .4]
            self.vec = [.45, .25]
            #self.vec = [1, 1]

        self.ran = ran
        self.col = col
        self.ticks = 0
        turt.alive.add(self)


    async def drive(self):

        newx = self.x + self.vec[0]
        newy = self.y + self.vec[1]

        if (newx >= XSIZE) or (newx <= 0):
           print("X", self.vec[0])
           self.vec[0] = -self.vec[0]
        if (newy >= YSIZE) or (newy <= 0):
            print("Y", self.vec[1])
            self.vec[1] = -self.vec[1]

        #can.create_line(self.x, self.y, newx, newy, fill=self.color)

        if not self.tron:
            photo.put(self.color, (abs(int(self.x)), abs(int(self.y))))
        else:
            try:
                #forward = photo.get(int(self.x + (2 * self.vec[0])), int(self.y + (2 * self.vec[1])))
                for_check = []
                for column in buildLookAround(5,5):
                    for row in column:
                        for_check.append(
                            photo.get(int(self.x + (2 * self.vec[0])), int(self.y + (2 * self.vec[1]))) != (0, 0, 0)
                        )
                #if forward != (0, 0 ,0):
                if any(for_check):
                    self.turn(),
                    photo.put(self.color, (abs(int(self.x)), abs(int(self.y))))
                    #print("f")
                    #can.create_text(self.x, self.y, text=f"F")
                    #print("f", forward, self.x, self.y)  #Doesn't throw an error???
                else:
                    photo.put(self.color, (abs(int(self.x)), abs(int(self.y))))
            except tk.TclError as e:
                print("Exception:", e)
                photo.put(self.color, (abs(int(self.x)), abs(int(self.y))))


        self.x = newx
        self.y = newy

        if self.ran:
            if .05 > rand.random():
                self.turn()
        else:
            if self.ticks > rand.randint(100, 500):
                self.turn()
                self.ticks = 0
            else:
                self.ticks += 1

        #await self.drive()


    def turn(self):
        r = rand.randint(0,1)

        #if not self.tron:
        if r:
            self.vec[0] = -self.vec[0]
        else:
            self.vec[1] = -self.vec[1]
        # else:
        #     v0 = self.vec[0]
        #     v1 = self.vec[1]
        #     self.vec[0] = v1
        #     self.vec[1] = v0

        if self.col:
            self.color = hexcode()




#turt(col=True); turt(col=True); turt(col=True); turt(col=True); turt(col=True)

for x in range(6):
    turt(col=True, tron=True)


# for _ in turt.alive:
#     asyncio.run(_.drive())
#
# window.mainloop()

while True:
    #can.create_line(rand.randint(0,500), rand.randint(0,500), rand.randint(0,500), rand.randint(0,500),
    #                fill=hexcode())

    for _ in turt.alive:
        #_.drive()
        asyncio.run(_.drive())

    window.update_idletasks()
    window.update()











