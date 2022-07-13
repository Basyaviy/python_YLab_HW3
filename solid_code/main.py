from heroes import Superman, SuperHero, ChackNorris
from places import Place, Kostroma, Tokyo
from not_solid_code.massmedia import TV


def save_the_place(hero: SuperHero, place: Place):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    TV.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo())
