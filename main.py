from timet import*

class Coffee_Machine:
    def __init__(self, name, types_coffee, ingredients):
        self.types_coffee = types_coffee
        self.name = name
        self.ingredients = ingredients

    #Доступные виды кофе 
    def available_coffee(self):
        print(f'Автомат может приготовить: ')
        s = 0
        for type in self.types_coffee:
            s += 1
            print(f'{s} {type.name}')
        print(f'Ингридиенты в наличии: {self.ingredients}')

    #Выбор кофе
    def pick_coffee(self, sec):
        q = -1
        for type in self.types_coffee:
            q += 1
            print(f'{q} {type.name}')
        pick = input(f'Выбирите номер кофе из списка: ')
        your_pick = self.types_coffee[int(pick)]
        print(f'Готовлю {your_pick.name}. До приготовления {sec} секунд.')
        countdown(sec)
        print(f'Ваш {your_pick.name} готов.\nМожете забрать стаканчик.')
        

class Coffee:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    

latte = Coffee('Latte', {'Water : 1', 'Coffee : 1', 'Milk : 1'})
cappuccino = Coffee('Cappuccino', {'Water : 1', 'Coffee : 2' 'Milk : 1'})
americano = Coffee('Americano', {'Water : 1', 'Coffee : 1'})
espresso = Coffee('Espresso', {'Water : 1', 'Coffee : 1'})
irish = Coffee('Irish Coffee', {'Water : 1', 'Coffee : 1', 'Whiskey : 1'})

simple_machine = Coffee_Machine('Simple_Machine', [latte, cappuccino, espresso, americano, irish], ingredients = {'Water : 20', 'Coffee : 20', 'Milk : 15', 'Wiskey : 5'})

simple_machine.available_coffee()