class Person:
    def _init_(self, firsname, lastname, health, status):
        " initialize attributes to be used in/vailable for all\ class methods in this class, and for class objects created by this class."
        self.firstname = firsname
        self.lastname = lastname
        self.health = health
        self.status = status
        
    def introduce(self):
        "All people introduce themselves"
        print("hello, my name is {} {}".format(self.firstname, self.lastname))
    
    # def emote(self):
    #     emotion = random.randrange(1,3)
    #     if emotion ==1:
    #         print("{} is happy today".format(self.firstname))
    #     elif emotion ==2:
    #         print("{} is sad right now".format(self.firstname))
    
    def status_change(self):
        if self.health == 100:
            print("{} is totally healty!".format(self.firstname))
        elif self.health <= 50:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 100, status= True)
Rey = Person("Rey", "Jones", 90, status= True)
Lee = Person("Maria", "Gutierrez", 92, status= False)

# print("{} is my friend {}".format(Maria.firstname, Maria.status))
Maria.introduce()
Maria.status_change()

class Enemy(Person):
    def _init_(self, weapon, firsname, lastname, health, status):
        super.__init__(firsname, lastname, health, status)
        self.weaponv= weapon
    def hurt(self, other):
        if self.weaponv == "rock":
            other.health -=10
        elif self.weaponv == "stick":
            other.health -=5
        print(other.health)
    def insult(self, other):
        if other.health <=80:
            print("{}, you are tired and weak".format(o))
        
            
