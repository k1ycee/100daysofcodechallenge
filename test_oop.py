class Circle:

    pi = 3.14
    
    
    def __init__(self, diameter):
        print("New circle with diameter: "+ str(diameter))
        pass



class Circle:
      pi = 3.14
  def __init__(self, diameter):
    self.radius = diameter/2
    print("Creating circle with diameter {d}".format(d=diameter))
  def circumference(self):
    return 2 * self.pi * self.radius
  


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())



class Circle:
      pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius " + str(self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)



class Student:
  def __init__(self, name, year):
    self.name = name 
    self.year = year
    self.grades = []


  def add_grade(self, grade):
    if(type(grade)) is Grade:
      self.grades.append(grade)


class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score



roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))



class InsurancePolicy:
      def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return 0.001 * self.price_of_insured_item
  pass 


class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return 0.00005 * self.price_of_insured_item
  pass

  class SortedList(list):
      def append(self, value):
    super().append(value)
    self.sort()