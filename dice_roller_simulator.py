import random

# ● ┌ ─ ┐ │ └ ┘


x="roll"


while x=="roll":
    randnumber = random.randint(1,6)
    if   randnumber == 1:
          print("\n┌────────┐")
          print("|        |")
          print("|    ●   |")
          print("|        |")
          print("└────────┘")

    if   randnumber == 2:
          print("\n┌────────┐")
          print("| ●      |")
          print("|        |")
          print("|      ● |")
          print("└────────┘")

    if   randnumber == 3:
          print("\n┌────────┐")
          print("| ●      |")
          print("|   ●    |")
          print("|     ●  |")
          print("└────────┘")
      
    if   randnumber == 4:
          print("\n┌────────┐")
          print("| ●    ● |")
          print("|        |")
          print("| ●    ● |")
          print("└────────┘")

    if   randnumber == 5:
          print("\n┌────────┐")
          print("| ●    ● |")
          print("|    ●   |")
          print("| ●    ● |")
          print("└────────┘")

    if   randnumber == 6:
          print("\n┌────────┐")
          print("| ●    ● |")
          print("| ●    ● |")
          print("| ●    ● |")
          print("└────────┘")
      
    x= input("\n type roll to roll again dice = ")
    print("\n")



