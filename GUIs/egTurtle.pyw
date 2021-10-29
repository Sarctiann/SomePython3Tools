from turtle import *
from math import*

SPEED = 1

drawer=Turtle()
drawer.speed(SPEED)
writer=Turtle()
writer.hideturtle()
writer.pencolor(0,.5,1)
writer.write("...This is a Test :D", 
	align="center", font=("monospace", 18, "bold")
)

drawer.pu()
drawer.goto(-150,150)

for i in range(48):

	if i==12:
		drawer.right(90)
	if i==24:
		drawer.right(90)
	if i==36:
		drawer.right(90)

	r= float("{:.2f}".format(sin(i)/2+.5))
	g= float("{:.2}".format(5*i/235))
	b= float("{:.2}".format(5*(-i)/235+1))

	print("i= "+str(i)+" r= "+str(r)+" g= "+str(g)+" b= "+str(b))

	drawer.pensize(2)

	drawer.pd()

	drawer.pencolor(r,g,b)

	lados= int((sin(i)/2+.5)*10+3)

	print("lados= "+str(lados))

	drawer.circle(50, 360, lados)

	drawer.pu()

	drawer.forward(25)

	if i==24:
		writer.clear()
		writer.write("Ok...\nThis is Going well \n", 
			align="center", font=("monospace", 18, "bold")
		)

writer.clear()
writer.write("It's Work! \n Great!!!", 
	align="center", font=("Helvetica", 28, "bold")
)

done()
