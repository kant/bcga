from .base import ComplexOperator, context

#faces
f = "f"
#edges
e = "e"
#vertices
v = "v"

front = "front"
back = "back"
left = "left"
right = "right"
top = "top"
bottom = "bottom"
side = "side"
all = "all"

from .base import ComplexOperator, context

def decompose(*parts):
	return context.factory["Decompose"](*parts)

class Decompose(ComplexOperator):
	def __init__(self, *parts):
		self.parts = parts
		super().__init__(len(parts))
