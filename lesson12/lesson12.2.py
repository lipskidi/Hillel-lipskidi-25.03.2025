from typing import Dict

class Item:
    def __init__(self, name: str, price: float, description: str, dimensions: str) -> None:
        self.name: str = name
        self.price: float = price
        self.description: str = description
        self.dimensions: str = dimensions

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name: str, surname: str, numberphone: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.numberphone: str = numberphone

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user: User) -> None:
        self.products: Dict[Item, int] = {}
        self.user: User = user

    def add_item(self, item: Item, cnt: int) -> None:
        self.products[item] = cnt

    def get_total(self) -> float:
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self) -> str:
        result = f"User: {self.user}\nItems:"
        for item, cnt in self.products.items():
            result += f"\n{item.name}: {cnt} pcs."
        return result

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart.add_item(apple, 10)
print(cart)

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40