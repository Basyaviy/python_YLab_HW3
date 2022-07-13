from abc import ABC
from antagonistfinder import AntagonistFinder
from weapon import Laser, Kick


class SuperHero(ABC):
    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)



class Superman(SuperHero, Laser):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        self.incinerate_with_lasers()


class ChackNorris(SuperHero, Kick):
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', True)

    def ultimate(self):
        self.roundhouse_kick()

