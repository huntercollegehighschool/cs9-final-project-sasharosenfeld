print("\nYou wait for the bus, stll feeling the eyes on you. When it finally arrives, the doors open with a groan. The bus driver does not look at you as you get on. It's practically empty, and you sit down near the window. You still feel someone watching you. Maybe someone else can help...")
choiceA = input("\nEnter A to pretend everything is fine or B to ask the bus driver for help: ").upper()
while choiceA != "A" and choiceA != "B":
  print("\nThat is not a valid option.")
  choiceA = input("\nEnter A to pretend everything is fine or B to ask the bus driver for help: ").upper()
if choiceA == "A":  
  import pretend
elif choiceA == "B":
  import busdriver 
  