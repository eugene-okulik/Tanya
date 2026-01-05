from flowers import Flower


class Peony(Flower):
    def __init__(self, name, color, price, life_time, stem_length, freshness, fluffy=True):
        super().__init__(name, color, price, life_time, stem_length, freshness)
        self.fluffy = fluffy


class Sunflowers(Flower):
    def __init__(self, name, color, price, life_time, stem_length, freshness, has_seeds=True):
        super().__init__(name, color, price, life_time, stem_length, freshness)
        self.has_seeds = has_seeds


class Orchids(Flower):
    def __init__(self, name, color, price, life_time, stem_length, freshness, has_patterns=True):
        super().__init__(name, color, price, life_time, stem_length, freshness)
        self.has_patterns = has_patterns
