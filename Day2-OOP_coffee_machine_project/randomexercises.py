# import another_module
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.speed(1)
# timmy.color(another_module.another_variable)
# for i in range(0, 4):
#     timmy.forward(100)
#     timmy.left(90)
#
#
#
# my_screen = Screen()
#
# my_screen.canvheight = 750
#
# my_screen.listen()
# my_screen.onkey(key="space", fun=timmy.forward)
#
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

pokemon_names = ["Pikachu", "Squirtle", "Charmander", "Charizard"]
pokemon_types = ["Electric", "Water", "Fire", "Fire/Flight"]
pokemon_stats = [40, 40, 40, 200]
pokemon_list = [
    {
        "name": "Pikachu",
        "type": "Electric",
        "hp": "40"
    },
    {
        "name": "Squirtle",
        "type": "Water",
        "hp": "40"
    },
    {
        "name": "Charmander",
        "type": "Fire",
        "hp": "40"
    },
    {
        "name": "Charizard",
        "type": "Fire/Flight",
        "hp": "200"
    }
]

table.field_names = ["Pokemon Name", "Type", "HP"]
for pokemon in pokemon_list:
    table.add_row([pokemon["name"], pokemon["type"], pokemon["hp"]])
table.align = "l"


# table.field_names = ["Pokemon Name", "Type", "HP"]
# for i in range(0, len(pokemon_names)):
#     table.add_row([pokemon_names[i], pokemon_types[i], pokemon_stats[i]])
# table.align = "l"

# table.add_column("Pokemon Name", pokemon_names)
# table.add_column("Type", pokemon_types)
# table.add_column("HP", pokemon_stats)
# table.align = "l"

print(table)