#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.

print("You think you hear footsteps behind you, but can’t see anyone.")
choiceB = input("Enter A for keep walking or B for go into a shop:  ").upper()
while choiceB != "A" and choiceB != "B":
  print("That is not a valid option.")
  choiceB = input("Enter A for keep walking or B for go into a shop.").upper()
if choiceB == "A":
  import keepwalking
elif choiceB == "B":
  import shop
