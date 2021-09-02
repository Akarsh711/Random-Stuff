choice = int(input("Enter the choice \n 1 for Circle \n 2 for Rectangle \n 3 for Triangle\n"))

if choice == 1:
	# Area of Circle
	r = float(input("Enter the radius of the cicle:"))
	C = 3.14*r**2
	print("The area of circle is:",C)

if choice ==2:
	# Are of Rectangle
	length = float(input("Enter the length of rectangle"))
	bradth = float(input("Enter the breadth of rectangle"))
	R = length * bradth
	print("The area of rectangle is:", R)

if choice == 3:
	base = float(input("Enter the base of triangle:"))
	height = float(input("Enter the height of triangle"))
	T = 0.5*base*height
	print("The area of triangle is:", T)