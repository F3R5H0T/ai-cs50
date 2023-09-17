from logic import *

colors=["red", "blue", "green", "yellow"]
symbols=[]
for i in range(4):
	for color in colors:
		symbols.append(Symbol(f"{color}{i}"))

knowledge=And()

#each color has a position
for color in colors:
	knowledge.add(Or(
		Symbol(f"{color}0"),
		Symbol(f"{color}1"),
		Symbol(f"{color}2"),
		Symbol(f"{color}3")
		))

#only one position per color.
for color in colors:
	for i in range(4):
		for j in range(4):
			if i !=j:
				knowledge.add(Implication(
					Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))
				))

#only one color per position
for i in range(4):
	for color1 in colors;
	for color2 in colors:
		if color1!=color2:
			knowledge.add(Implication(
				Symbol(f"{color1}{i}"),Not(Symbol(f"{color2}{i}"))
				))

