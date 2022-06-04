#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.

print("\nYou get on the bus. You still feel someone watching you.")
choiceA = input("\nEnter A to pretend everything is fine or B to ask the bus driver for help: ").upper()
while choiceA != "A" and choiceA != "B":
  print("\nThat is not a valid option.")
  choiceA = input("\nEnter A to pretend everything is fine or B to ask the bus driver for help: ").upper()
if choiceA == "A":  
  import pretend
elif choiceA == "B":
  import busdriver 
  