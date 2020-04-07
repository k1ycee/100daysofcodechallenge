premium = 125

def ground_shipping(weight):
  if weight <= 2:
   return weight*1.50 + 20.00
  elif weight >= 2 and weight <=6:
   return weight*3.00 + 20.00
  elif weight >= 6 and weight <=10:
   return weight*4.00 + 20.00
  elif weight >=10:
   return weight*4.75 + 20.00
  
ground_shipping(8.4)

def drone_shipping(weight):
  if weight <= 2:
   return weight*4.50
  elif weight >= 2 and weight <=6:
   return weight*9.00
  elif weight >= 6 and weight <=10:
   return weight*12.00
  elif weight >=10:
   return weight*14.75
  
drone_shipping(1.5)


def cheapest_shipping(weight):
  if premium < drone_shipping(weight) and ground_shipping(weight):
    print ("You might want to use premium ground shipping it is $" + str(premium))
  elif drone_shipping(weight) < premium and ground_shipping(weight):
    print ("You might want to use drone shipping it is $" + str(drone_shipping(weight)))
  elif ground_shipping(weight) < drone_shipping(weight) and premium:
    print ("You might want to use groun shipping it is $" + str(drone_shipping(weight)))
    
cheapest_shipping(4.8)
cheapest_shipping(41.5)