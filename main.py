# from turtle import Turtle, Screen

# john = Turtle()
# john.shape('turtle')
# john.color('blue4')
# john.forward(100)
# print(john)


# my_screen = Screen()
# print({my_screen.canvheight})
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)