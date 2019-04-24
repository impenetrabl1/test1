from collections import defaultdict


class Flower:

    def __init__(self, type, cost):
        self.type = type
        self.cost = cost

    def __str__(self):
        return "Type: %s, cost: %s" % (self.type, self.cost)


class Bouquet(Flower):

    def __init__(self, name, flowers, cost=None):
        self.name = name
        self.flowers = defaultdict(int, flowers)
        if cost is not None:
            self.cost = cost
        else:
            self.cost = sum([i.cost * j for i, j in zip(list(flowers.keys()), list(flowers.values()))])

    def add_flower(self, flower, count=1):
        self.flowers[flower] = count

    def del_flower(self, flower):
        del self.flowers[flower]

    def __str__(self):
        return "bouquet: %s, contains: %s, costs: %s" % (self.name, self.flowers, self.cost)


class FlowerShop:
    def __init__(self, name, bouquets, money=250):
        self.name = name
        self.bouquets = defaultdict(int, bouquets)
        self.money = money

    def bouquets_check(self, bouquet, count):
        if count > self.bouquets[bouquet]:
            return False
        return True

    def selling(self, bouquet, count=1):
        if self.bouquets_check(bouquet, count):
            self.bouquets[bouquet] -= count
            self.money += bouquet.cost * count
        else:
            return "not enough bouquets for selling!"

    def add_bouquets(self, bouquet, count=1):
        self.bouquets[bouquet] += count

    def del_bouquet(self, bouquet):
        del self.bouquets[bouquet]

    def __str__(self):
        return "Shop: %s, has bouquets: %s, has money: %s" % (self.name, self.bouquets, self.money)


if __name__ == "__main__":
    rose = Flower("rose", 100)
    tulip = Flower("tulip", 150)
    rose_bouquet = Bouquet("roses", flowers={rose: 5})
    tulip_bouquet = Bouquet("tulips", flowers={tulip: 3})
    flower_shop = FlowerShop("flower shop", bouquets={rose_bouquet: 5, tulip_bouquet: 3})
    flower_shop.selling(rose_bouquet, 3)
    flower_shop.selling(tulip_bouquet)
    flower_shop.add_bouquets(rose_bouquet, 5)
