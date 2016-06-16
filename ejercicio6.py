import turtle
t=turtle.Pen()
def cuadrado(size):
	for x in range(1,5):
		t.forward(size)
		t.left(90)
x=int(input("ingrese la longitud"))
cuadrado(x)
turtle.getscreen()._root.mainloop()