class car:
  def colour(self,c):
    self.colour = c

  def brand(self,br):
   self.brand = br

  def shape(self,sh):
   self.shape = sh
  
  def type(self,ty):
   self.type = ty
  
  def fuel(self,fl):
    self.fuel = fl

cr= car()

cr.brand('Jaguar')
cr.shape('hexagonal')
cr.colour('Red')
cr.type('SUV')
cr.fuel('Petrol')

print(cr.brand)
print(cr.shape)
print(cr.colour)
print(cr.type)
print(cr.fuel)


 
