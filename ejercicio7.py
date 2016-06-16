import turtle
t=turtle.Pen()

def poligono(size,lado):
	grado=360/lado
	for x in range(0,lado):
		t.forward(size)
		t.left(grado)

lado=int(input("ingrese el numero de lados"))
tamaño=int(input("ingrese el tamaño que no se ha mayor a 10000 "))
poligono(tamaño, lado)
turtle.getscreen()._root.mainloop()


 
