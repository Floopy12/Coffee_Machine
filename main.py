from timet import*

class Coffee_Machine:
    def __init__(self, name, types_coffee, ingredients):
        self.types_coffee = types_coffee
        self.name = name
        self.ingredients = ingredients

    #Доступные виды кофе 
    def available_coffee(self):
        print(f'Автомат может приготовить: ')
        for index, type in enumerate(self.types_coffee):
            print(f'{index} {type.name}')
        print(f'Ингридиенты в наличии: {self.ingredients}')

    #Выбор кофе
    def pick_coffee(self, sec):
        for index, type in enumerate(self.types_coffee):
            print(f'{index} {type.name}')
        pick = input(f'Выбирите номер кофе из списка: ')
        your_pick = self.types_coffee[int(pick)]
        print(f'Готовлю {your_pick.name}. До приготовления {sec} секунд.')
        countdown(sec)
        print(f'Ваш {your_pick.name} готов.\nМожете забрать стаканчик.')

        

class Coffee:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    

latte = Coffee('Latte', ingredients = {'Water' : 1, 'Coffee' : 1, 'Milk' : 1})
cappuccino = Coffee('Cappuccino', ingredients = {'Water' : 1, 'Coffee' : 2, 'Milk' : 1})
americano = Coffee('Americano', ingredients = {'Water' : 1, 'Coffee' : 1})
espresso = Coffee('Espresso', ingredients = {'Water' : 1, 'Coffee' : 1})
irish = Coffee('Irish Coffee', ingredients = {'Water' : 1, 'Coffee' : 1, 'Whiskey' : 1})

simple_machine = Coffee_Machine('Simple_Machine', [latte, cappuccino, espresso, americano, irish], ingredients = {'Water' : 20, 'Coffee' : 20, 'Milk' : 15, 'Wiskey' : 5})

