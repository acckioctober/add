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
        return f'Nickname: {self.nickname.title()}\n' \
               f'Superpower: {self.superpower.capitalize()}\n' \
               f'Health_points: {self.health_points}'

    '''step #6'''
    def __len__(self):
        return len(self.catchphrase)

'''step #7'''
my_hero = SuperHero("arnold schwarzenegger", "terminator t-800", "titanium alloy skeleton", 100, "i'll be back")

print(my_hero.people.title())           # вывод значения собственного атрибута класса
my_hero.print_name()                    # вызов метода экземпляра класса для вывода имени героя
my_hero.doubling_health_points()        # вызов метода экземпляра класса для вывода здоровья героя умноженного на 2
print(my_hero)                          # вывод информации об экземпляре класса используя магический метод __str__
print(len(my_hero))                     # вывод информации о длине коронной фразы используя магический метод __len__






