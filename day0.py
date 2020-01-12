
people = {"Ameh": "Jan 1",
          "Chinaza": "Jan 8",
          "Emma Boards": "Jan 10",
          "Timi": "Jan 21",
          "Joy": "Feb 14",
          "Uwem": "Feb 16",
          "Bastard": "March 15",
          "Mama Favour": "May 12",
          "Nwene": "May 29",
          "Favo": "June 24",
          "Neric": "July 25",
          "Ebube": "August 4",
          "Winston": "August 8",
          "Chinoyelum": "Dec 23"}

while True:
    name = input('Which person: ')
    if name == '':
        break
    if name in people:
        print(people[name]+' is the birthday of ' + name)
    else:
        print("you haven't told me of a " + name)
        print("what's their birthday")
        bday = input('Tell me: ')
        people[name] = bday
        print("Birthday Noted sir!!")