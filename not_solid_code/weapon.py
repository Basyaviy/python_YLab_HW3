class Weapon():
    def attack(self):
        self.fire_a_gun()

    def fire_a_gun(self):
        print('PIU PIU')


class Laser(Weapon):
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class Kick(Weapon):
    def roundhouse_kick(self):
        print('Bump')
