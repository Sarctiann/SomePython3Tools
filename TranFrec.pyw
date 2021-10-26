from tkinter import *

vent = Tk()
vent.title("Transportador")
vent.resizable(width=False, height=False)

tono = StringVar()

class Nota():

    def __init__(self):
        self.la = 440
        self.st = 2**(1/12)
        ini = "%.3f" % self.la
        tono.set(ini)

        self.cont = 0
        self.notas = ["La","La#","Si","Do","Do#","Re",
                      "Re#","Mi","Fa","Fa#","Sol","Sol#"]
    
    def subir(self, *args,**kw):
        tra = self.la*self.st
        val = "%.3f" % tra
        tono.set(val)
        self.la = tra

        self.cont += 1
        print(self.notas[self.cont])
        if self.cont == 11: self.cont = -1 

    def bajar(self, *args,**kw):
        tra = self.la/self.st
        val = "%.3f" % tra
        tono.set(val)
        self.la = tra

        self.cont -= 1
        print(self.notas[self.cont])
        if self.cont == -12: self.cont = 0 

cuadrito = Frame(vent)
cuadrito.pack()

nota = Nota()
print("La")

displ = Label(cuadrito, textvariable=tono, width=12)
displ.grid(row=0, column=1)

btn1 = Button(cuadrito, text="st -", command=nota.bajar)
btn1.grid(row=0, column=0)

btn2 = Button(cuadrito, text="st +", command=nota.subir)
btn2.grid(row=0, column=2)

vent.bind("<Right>", nota.subir)
vent.bind("<Left>", nota.bajar)

vent.mainloop()
