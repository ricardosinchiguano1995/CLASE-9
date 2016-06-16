import turtle
t=turtle.Pen()
#for x in range(1,9):
	#t.forward(100)
	#t.left(225)
#t.reset()
#turtle.getscreen()._root.mainloop()

#ejericicio con usuario 
x=int(input("ingreseel numero de lados"))
grado=360/x
for i in range(0,x):
	t.forward(50)
	t.left(grado)
t.reset()
turtle.getscreen()._root.mainloop()