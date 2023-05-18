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
        if dx % self.s + dy % self.s == 0:
            return dx // self.s + dy // self.s
        print(
            f"Точка ({x2}, {y2}) недостижима из точки ({self.x}, {self.y}) с шагом {self.s}"
        )
        return None


turtle = Turtle(0, 0, 1)
print(turtle.count_moves(3, 4))
turtle.evolve()
print(turtle.count_moves(3, 4))
turtle.degrade()
print(turtle.count_moves(3, 4))
