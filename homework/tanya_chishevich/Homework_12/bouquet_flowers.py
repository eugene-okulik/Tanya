from types_flowers import Peony, Sunflowers, Orchids


class BouquetFlowers:
    def __init__(self, name):
        self.name = name
        self.bouquets = []

    def __str__(self):
        return f"Букет состоит из {len(self.bouquets)} цветов: {self.bouquets}"

    def add_bouquet(self, bouquet):
        self.bouquets.append(bouquet)

    def set_cost(self):
        return sum(flower.price for flower in self.bouquets)

    def flower_fading_time(self):
        average_time = round(sum(flower.life_time for flower in self.bouquets) / len(self.bouquets))
        return average_time

    def sort_by_color(self):
        self.bouquets.sort(key=lambda x: x.color)

    def sort_by_price(self):
        self.bouquets.sort(key=lambda x: x.price)

    def sort_stem_length(self):
        self.bouquets.sort(key=lambda x: x.stem_length, reverse=True)

    def sort_freshness(self):
        self.bouquets.sort(key=lambda x: x.freshness, reverse=True)

    # Поиск цветов по среднему времени жизни (например, живут дольше чем life_days)
    def find_flowers_by_life_time(self, life_days):
        find_flowers = [flower.name for flower in self.bouquets if flower.life_time >= life_days]
        return find_flowers


flower1 = Peony("Пион", "розовый", 150, 14, 80, 5)
flower2 = Sunflowers("Подсолнух", "жёлтый", 100, 80, 100, 3)
flower3 = Orchids("Орхидея", "белый", 86, 21, 55, 1)

my_bouquet = BouquetFlowers('Мой букет')
my_bouquet.add_bouquet(flower1)
my_bouquet.add_bouquet(flower2)
my_bouquet.add_bouquet(flower3)
print(my_bouquet)

print(f"\nОбщая стоимость букета {my_bouquet.set_cost()}")

print(f"\nВремя увядания букета по среднему времени жизни: {my_bouquet.flower_fading_time()}")

my_bouquet.sort_by_color()
print("\nСортировка букета по цвету(по алфавиту):", [flower.color for flower in my_bouquet.bouquets])

my_bouquet.sort_by_price()
print("\nСортировка букета по стоимости(по возрастанию):", [flower.price for flower in my_bouquet.bouquets])

my_bouquet.sort_stem_length()
print("\nСортировка букета по длине стебля (по убыванию):", [flower.stem_length for flower in my_bouquet.bouquets])

my_bouquet.sort_freshness()
print("\nСортировка букета по свежести (по убыванию):", [flower.freshness for flower in my_bouquet.bouquets])

print(f"\nПоиск цветов в букете {my_bouquet.find_flowers_by_life_time(15)}")
