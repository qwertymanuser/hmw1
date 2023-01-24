class SuperHero:
    people='people'
    def __init__(self,name,nickname,supername, health_points,catchphrase) -> None:
        self.name = name
        self.nickname = nickname
        self.supername = supername
        self.health_points = health_points
        self.catchphrase = catchphrase
    def info(self):
        return f"Name: {self.name}, Catchphrase: {self.catchphrase}"
    def healthpoints(self):
        return f"Имя: {self.name}, его здоровье {self.health_points * 2}"

    def __str__(self):
        return f"nick: {self.nickname}, super-power: {self.supername}, health: {self.health_points}, catchphrase: {self.catchphrase}"
    def len(self):
        return len(self.catchphrase)

    
hero = SuperHero("superman","pautina", "udar",1000,"supermannc")

class NewSuper(SuperHero):
    def __init__(self, name, nickname, supername, health_points, catchphrase) -> None:
         super().__init__(name, nickname, supername, health_points, catchphrase)
         self.damage = False
         self.fly = False
    def kvodrat(self):
        self.fly = True
        return f"Квадрат: {self.health_points ** 2}, Fly: {self.fly}"
    def newmetod(self):
        return f"newdamage: {self.damage}, newfly: {self.fly}"
    def flyg(self):
        return f"catchphrase: {self.catchphrase}"
newsuper = NewSuper("chuvak", "belka", "teb",10,"fly in the True phrase")
print(newsuper.kvodrat())
print(newsuper.flyg())
print(newsuper.newmetod())
class Villain(SuperHero):
    people = "monstr"
    def gen_x(self):
        pass
    def crit(self,damage1,damage2):
        return f"uron: {damage1 ** damage2}"
villain = Villain("zlodei", "granata", "mech",1001,"hulk")
print(villain.crit(6,10))