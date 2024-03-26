class Pet:
 def __init__(self):
  self.name = "Бобік"
  self.gender = "male"
  self.age = 12
  self.type = "dog"
  self.Gladness = 100
  self.Alive = True

 def printer(self):
  print("name =", self.name,"gender =",self.gender,"age =",self.age,"type =",self.type,"Gladness =",self.Gladness,"Alive =",self.Alive)
Pet = Pet()
Pet.printer()


