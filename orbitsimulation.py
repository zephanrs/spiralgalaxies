import turtle
import math
import time


class particle(turtle.Turtle):
    def __init__(
            self,
            galaxy,
            mass,
            display_size,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = display_size

        self.penup()
        self.hideturtle()

        galaxy.add_body(self)

    def draw(self):
        self.clear()
        self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])

    def gravity(self, bodies):
        for body in bodies:
            try:
                acc = body.mass / self.distance(body) ** 2
                angle = self.towards(body)
                self.velocity = (
                    self.velocity[0] + (acc * math.cos(math.radians(angle))),
                    self.velocity[1] + (acc * math.sin(math.radians(angle)))
                )
                print(acc)
            except:
                continue



class blackHole(particle):
    def __init__(
            self,
            galaxy,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__(galaxy, mass, 10, position, velocity)
        self.color("red")


class star(particle):
    def __init__(
            self,
            galaxy,
            mass,
            position=(0, 0),
            velocity= (0, 0),
    ):
        super().__init__(galaxy, mass, math.log(mass, 1.1), position, velocity)
        self.color("white")


class galaxy:
    def __init__(self, width, height):
        self.galaxy = turtle.Screen()
        self.galaxy.tracer(0)
        self.galaxy.setup(width, height)
        self.galaxy.bgcolor("black")

        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    def update_all(self):
        for body in self.bodies:
            body.gravity(self.bodies)
        for body in self.bodies:
            body.move()
            body.draw()
        self.galaxy.update()