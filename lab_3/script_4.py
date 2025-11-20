class Goods:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} : {self.price}руб.")


class Basket:
    def __init__(self):
        self.goods = {}

    def add(self, goods, count=1):
        if goods in self.goods:
            self.goods[goods] += count
        else:
            self.goods[goods] = count

    def delete(self, goods, count=1):
        if self.goods[goods] <= count:
            self.goods.pop(goods)
        else:
            self.goods[goods] -= count

    def display(self):
        i = 1
        for key, value in self.goods.items():
            print(f"{i}. ", end="")
            print(key.name, value)
            i += 1


apple = Goods(0, "Яблоко", 5)
watermelon = Goods(1, "Арбуз", 30)
orange = Goods(2, "Апельсин", 10)

catalog = []
catalog.append(apple)
catalog.append(watermelon)
catalog.append(orange)

basket = Basket()

while (True):
    print("\nВыберите действие:")
    print("1. Посмотреть каталог товаров")
    print("2. Посмотреть содеожимое корзины")
    print("0. Выход")

    select = int(input())
    if select == 0:
        print("Приходите ещё!")
        break

    elif select == 1:
        print("Выберите товар:")
        i = 1
        for elem in catalog:
            print(f"{i}. ", end="")
            elem.display()
            i += 1
        print("0. Назад")
        catalog_select = int(input())
        if catalog_select == 0:
            continue
        else:
            catalog_select -= 1
        goods = catalog[catalog_select]
        print(f"Выбран товар {goods.name}")
        count = int(input("Введите количество: "))
        if count > 0:
            basket.add(goods, count)
            print("Товар успешно добавлен")

    elif select == 2:
        if len(basket.goods) == 0:
            print("Корзина пуста")
            continue
        print("Выберите товар:")
        basket.display()
        print("0. Назад")
        basket_select = int(input())
        if basket_select == 0:
            continue
        else:
            basket_select -= 1
        i = 0
        for key in basket.goods.keys():
            if i == basket_select:
                goods = key
                break
            i += 1
        print(f"Выбран товар {goods.name}")
        count = int(input("Введите количество: "))
        if count > 0:
            basket.delete(goods, count)
            print("Товар успешно удалён")

    else:
        print("Ошибка! Выберите действие из списка")
