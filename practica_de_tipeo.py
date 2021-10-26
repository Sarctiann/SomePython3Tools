from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def iniciar():
    borrar()
    cuenta(hor.get(),minu.get(), seg.get())
    textEn.focus_force()

proceso=0

def cuenta(hor, minu, seg):
    global proceso

    hor = 0 if hor=='' else int(hor)
    minu = 0 if minu=='' else int(minu)
    seg = 0 if seg=='' else int(seg)

    if hor==0 and minu==0 and seg==0:
        time['text'] = 'Se Terminó el Tiempo'
        contar_palabras(textEn.get(1.0, END))
        ventana.focus()
        return
    tiem = (hor,minu,seg)
    if seg > 0:
        seg -= 1
    else:
        seg = 59
        if minu > 0:
            minu -= 1
        else:
            minu = 59
            if hor > 0:
                hor -= 1

    time['text'] = 'Tiempo restante {}:{}:{}'.format(tiem[0],tiem[1],tiem[2])
    proceso = time.after(1000, lambda:cuenta(hor,minu,seg))

def cancelar():
    global proceso
    time.after_cancel(proceso)
    time['text'] = 'Reloj Cancelado'

def contar_palabras(texto):
    texto = texto.split()
    count = 0
    for i in texto:
        count += 1

    result['text'] = 'Tu texto tiene {} palabras'.format(count)
    return count

def borrar():
    textEn.delete(1.0, END)
    time['text'] = ''
    result['text'] = result['text'].replace('Tu texto tiene', 'Ultima vez')

ventana = Tk()
ventana.geometry("750x500+100+50")
ventana.title("Practica De Tipeo 1.1")
ventana.resizable(False,False)

hor = StringVar()
minu = StringVar()
seg = StringVar()

frame1 = Frame(ventana)
frame1.grid(row=0, sticky='w')

lblHora = Label(frame1, text = "Tiempo:", font = ("Arial",14))
lblHora.grid(row=0, column=0)
txtHora = Entry(frame1, width=3, textvariable = hor)
txtHora.grid(row=0, column=1)
txtHora.focus()

lblMinuto = Label(frame1, text = ":", font = ("Arial",14))
lblMinuto.grid(row=0, column=2)
txtMinuto = Entry(frame1, width=3, textvariable = minu)
txtMinuto.grid(row=0, column=3)

lblSegundo = Label(frame1, text = ":", font = ("Arial",14))
lblSegundo.grid(row=0, column=4)
txtSegundo = Entry(frame1, width=3, textvariable = seg)
txtSegundo.grid(row=0, column=5)

btn1 = Button(frame1, text='INICIAR', background='blue', fg='white',
    command=iniciar)
btn1.grid(row=0, column=6)

btn2 = Button(frame1, text='Cancelar', background='red',
    command=cancelar)
btn2.grid(row=0, column=7)

btn3 = Button(frame1, text='Borrar Todo', background='yellow',
    command=borrar)
btn3.grid(row=0, column=8)

time = Label(frame1, fg='red', width=20,
    font=("Arial",14))
time.grid(row=0, column=9)

frame2 = Frame(ventana)
frame2.grid(row=1, column=0)

textEn = ScrolledText(frame2, font=("Helvetica", 12))
textEn.grid(row=0)

result = Label(frame2, fg='red', width=20,
    font=("Arial",14))
result.grid(row=1)

ventana.mainloop()
