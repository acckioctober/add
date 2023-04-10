''' step #1'''
class SuperHero():
    people = 'people'

    '''step #2'''
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    '''step #3'''
    def print_name(self):
        print(self.name.title())

    '''step #4'''
    def doubling_health_points(self):
        print(self.health_points * 2)

    '''step #5'''
    def __str__(self):
        description = f'Nickname: {self.nickname}\n' \
               f'Superpower: {self.superpower}\n' \
               f'Health_points: {self.health_points}'
        return description.title()

    '''step #6'''
    def __len__(self):
        return len(self.catchphrase)

'''step #7'''

my_hero = SuperHero("linda hamilton", " sarah j. connor", "sews curtains", 10, "i am not sleeping")
print(my_hero.people.title())           # вывод значения собственного атрибута класса
my_hero.print_name()                    # вызов метода экземпляра класса для вывода имени героя
my_hero.doubling_health_points()        # вызов метода экземпляра класса для вывода здоровья героя умноженного на 2
print(my_hero)                          # вывод информации об экземпляре класса используя магический метод __str__
print(len(my_hero))                     # вывод информации о длине коронной фразы используя магический метод __len__


'''Homework #2'''

class Terminator(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def doubling_health_points(self):
        print(self.health_points ** 2)
        self.fly = True
    def true_phrase(self):
        print('fly in the ' + str(self.fly)+'_phrase')

terminator = Terminator("arnold schwarzenegger", "terminator t-800", "titanium alloy skeleton", 100, "i'll be back", 100)
terminator.doubling_health_points()
terminator.true_phrase()

class Villain(Terminator):
    people = 'monster'
    def gen_x(self):...
    def crit(self):
        print(self.damage ** 3)

vill = Villain("robert patrick", "terminator t-1000", "liquid skeleton", 200, "i know it hurts", 200)
vill.crit()
Villain.crit(terminator)