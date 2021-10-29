from tkinter import *

MIDDLE_OCT = 4

root = Tk()
root.title("Freq Transporter")
root.resizable(width=False, height=False)

freq = StringVar()
note = StringVar()

class Transporter():

    def __init__(self):
        self.freq = 440
        self.ST = 2**(1/12)
        self.count = 9
        self.notes = [
            "Do  ","Do #","Re  ","Re #","Mi  ","Fa  ",
            "Fa #","Sol ","Sol#","La  ","La #","Si  "
        ]

        iniF = f"{self.freq:.3f}"
        freq.set(iniF)
        note.set(
            f"{self.notes[self.count % 12]} {self.count // 12 + MIDDLE_OCT} = {iniF}Hz"
        )
    
    def up(self, *args,**kw):
        tra = self.freq*self.ST
        val = "%.3f" % tra
        self.freq = tra
        self.count += 1
        freq.set(val)

        note.set(
            f"{self.notes[self.count % 12]} {self.count // 12 + MIDDLE_OCT} = {val}Hz"
        )

    def down(self, *args,**kw):
        tra = self.freq/self.ST
        val = "%.3f" % tra
        self.freq = tra
        self.count -= 1
        freq.set(val)

        note.set(
            f"{self.notes[self.count % 12]} {self.count // 12 + MIDDLE_OCT} = {val}Hz"
        )

frame1 = Frame(root)
frame1.pack(expand=True, fill="both")

nota = Transporter()

displN = Label(frame1, textvariable=note, width=12, font="monospace",
    fg="white", bg="#337777"
)
displN.grid(row=0, column=0, columnspan=2, sticky="ns", ipadx=50, ipady=20)

btn1 = Button(frame1, text="st -", command=nota.down, bg='#ffaaaa')
btn1.grid(row=1, column=0, sticky="ew")

btn2 = Button(frame1, text="st +", command=nota.up, bg='#aaffaa')
btn2.grid(row=1, column=1, sticky="ew")

root.bind("<Right>", nota.up)
root.bind("<Left>", nota.down)

root.mainloop()
