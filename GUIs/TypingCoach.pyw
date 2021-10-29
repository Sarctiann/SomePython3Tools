from tkinter import *
from tkinter.scrolledtext import ScrolledText

def start():
    clear()
    counter(hours.get(),minutes.get(), seconds.get())
    textEn.focus_force()

process=0

def counter(h, m, s):
    global process

    h = 0 if h=='' else int(h)
    m = 0 if m=='' else int(m)
    s = 0 if s=='' else int(s)

    if h==0 and m==0 and s==0:
        time['text'] = 'Time Over!'
        contar_palabras(textEn.get(1.0, END))
        root.focus()
        return
    tiem = (h,m,s)
    if s > 0:
        s -= 1
    else:
        s = 59
        if m > 0:
            m -= 1
        else:
            m = 59
            if h > 0:
                h -= 1

    time['text'] = 'Time Remaining {}:{}:{}'.format(tiem[0],tiem[1],tiem[2])
    process = time.after(1000, lambda:counter(h,m,s))

def cancelar():
    global process
    time.after_cancel(process)
    time['text'] = 'Clock Canceled'

def contar_palabras(text):
    count = len(text.split())

    result['text'] = 'Your Text have {} words'.format(count)
    return count

def clear():
    textEn.delete(1.0, END)
    time['text'] = ''
    result['text'] = result['text'].replace('Your Text have', 'Last try')

root = Tk()
root.geometry("+100+50")
root.title("Typing Coach")
root.resizable(False,False)

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

frame1 = Frame(root)
frame1.grid(row=0, sticky='w')

lblH = Label(frame1, text = "Time:", font = ("Arial",14))
lblH.grid(row=0, column=0)
txtH = Entry(frame1, width=3, textvariable = hours)
txtH.grid(row=0, column=1)
txtH.focus()

lblM = Label(frame1, text = ":", font = ("Arial",14))
lblM.grid(row=0, column=2)
txtM = Entry(frame1, width=3, textvariable = minutes)
txtM.grid(row=0, column=3)

lblS = Label(frame1, text = ":", font = ("Arial",14))
lblS.grid(row=0, column=4)
txtS = Entry(frame1, width=3, textvariable = seconds)
txtS.grid(row=0, column=5)

btn1 = Button(frame1, text='Start', background='green', fg='white',
    command=start)
btn1.grid(row=0, column=6)

btn2 = Button(frame1, text='Cancel', background='red',
    command=cancelar)
btn2.grid(row=0, column=7)

btn3 = Button(frame1, text='Clear', background='yellow',
    command=clear)
btn3.grid(row=0, column=8)

time = Label(frame1, fg='red', width=20,
    font=("Arial",14))
time.grid(row=0, column=9)

frame2 = Frame(root)
frame2.grid(row=1, column=0)

textEn = ScrolledText(frame2, font=("Helvetica", 12))
textEn.grid(row=0)

result = Label(frame2, fg='red', width=20,
    font=("Arial",14))
result.grid(row=1)

root.mainloop()
