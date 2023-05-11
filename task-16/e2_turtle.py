class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("s не может быть меньше или равно 0")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return (dx + self.s - 1) // self.s + (dy + self.s - 1) // self.s


turtle = Turtle(0, 0, 1)
print(turtle.count_moves(3, 4))
turtle.evolve()
print(turtle.count_moves(3, 4))
turtle.degrade()
print(turtle.count_moves(3, 4))
