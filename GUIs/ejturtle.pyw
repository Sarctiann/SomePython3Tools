from turtle import *
from math import*

maru=Turtle()
sebas=Turtle()
sebas.hideturtle()
sebas.pencolor(0,.5,1)
sebas.write("...Esta es una prueba :D", align="center", font=("Helvetica", 20, "bold"))

maru.pu()
maru.goto(-150,150)

for i in range(48):

	if i==12:
		maru.right(90)
	if i==24:
		maru.right(90)
	if i==36:
		maru.right(90)

	r= float("{:.2f}".format(sin(i)/2+.5))
	g= float("{:.2}".format(5*i/235))
	b= float("{:.2}".format(5*(-i)/235+1))

	print("i= "+str(i)+" r= "+str(r)+" g= "+str(g)+" b= "+str(b))

	maru.pensize(2)

	maru.pd()

	maru.pencolor(r,g,b)

	lados= int((sin(i)/2+.5)*10+3)

	print("lados= "+str(lados))

	maru.circle(50, 360, lados)

	maru.pu()

	maru.forward(25)

	if i==16:
		sebas.clear()
		sebas.write("  Epa... \nNo me pisen \n", align="center", font=("Helvetica", 20, "bold"))

sebas.clear()
sebas.write("Funciona! \n todo OK!!!", align="center", font=("Helvetica", 20, "bold"))

done()
