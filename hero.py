class Superhero:
    people = "people"
    def hero(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def mar(self):
        return f"name: {self.name}"
    def hidht(self):
        return f"health_points: {self.health_points *2}"
    def fick(self):
        return f"nick: {self.nickname}, super: {self.superpower}, hedht: {self.health_points}"
    def len (self):
        return f"leaght: {len(self.catchphrase)}"
hero = Superhero()
print(hero.hero("superman", "100web", "web",100,"koncha"))
print(hero.mar())
print(hero.hidht())
print(hero.fick())
print(hero.len())