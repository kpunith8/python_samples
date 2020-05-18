class Person:
    def __init__(self, real_name):
        self.real_name = real_name

    def report(self):
        print("I'm {}".format(self.real_name))


class Agent(Person):  # Agent inherits Person class
    # class object attribute
    planet = "Earth"

    def __init__(self, real_name, eye_color, height):
        Person.__init__(self, real_name)
        self.eye_color = eye_color
        self.height = height

    def report(self):
        print("Overriding the Person's report()")

    # _ defines a private method which won't be accessible directly
    def _secrets(self):
        print("secrets")

    # Pythons built-in functions can be overridden, this function prints the string representation of this class
    def __str__(self):
        return "Name is {}, eye colour is {}, and height is {}.".format(
            self.real_name, self.eye_color, self.height
        )


# agent = Agent("Punith", "black", 165)
# agent1 = Agent("Rama", "blue", 178)

# agent.report()  # allows calling Person's methods using Agent's object
# agent._secrets()

# print(agent)
# print(agent1)

# print(agent.real_name, agent.eye_color, agent.height)
# print(agent1.real_name, agent1.eye_color, agent1.height)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * Circle.pi * self.radius


# circle = Circle(3)
# print("Area of circle:", circle.area(), " Perimeter:", circle.perimeter())
