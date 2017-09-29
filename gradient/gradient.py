import turtle
import webcolors

def gen(color_a, color_b, steps,hight):
	turtle.colormode(255)

	t = turtle.Turtle()
	t.speed(0)
	turtle.tracer(0,0)
	t.hideturtle()
	t.pensize(100/steps)
	Diff = []
	Color = []

	#Checks and changes colortypes to rgb 255
	def check(TransIn):

		if type(TransIn) == list:

			if TransIn > [1,1,1]:
				return([round(x) for x in TransIn])

			elif TransIn <= [1,1,1]:

				for x in range(3):
					TransIn[x] *= 255

				return([round(x) for x in TransIn])

		elif type(TransIn) == str:

			if "#" in TransIn:
				TransIn = webcolors.hex_to_rgb(TransIn)

				return(list(TransIn))

			else:
				TransIn = webcolors.name_to_rgb(TransIn)
				return(list(TransIn))
		else:
			#Throw Error
			pass

	color_a = check(color_a)
	color_b = check(color_b)

	for x in range(3):
		Diff.append((color_a[x] - color_b[x]) / steps)
	Color = color_a
	for x in range(-round(steps/2),round(steps/2)):
		t.color(round(Color[0]),round(Color[1]),round(Color[2]),)
		for y in range(3):
			Color[y] -= Diff[y]
		t.penup()
		t.goto(x,-round(hight/2))
		t.pendown()
		t.goto(x,round(hight/2))
