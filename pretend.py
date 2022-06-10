#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.

print("\nYou try to pretend everything is fine. Maybe the gray of the cty will take your mind off things? You look out the window and see the reflection of a person behind you. They look pretty pale...")
choiceP = input("\nEnter A to mind your own business or B to check on the person: ").upper()
while choiceP != "A" and choiceP != "B":
  print("\nThat is not a valid option.")
  choiceP = input("\nEnter A to mind your own business or B to check on the pale person: ").upper()
if choiceP == "A":
  print("\nYou get off the bus and make it home. That was weird. You think nothing of it. You minded your own business! You survived. Congrats. Unfortunately, you were so focused on minding your own business, you forgot to check if your roommate turned the stove off. Your apartment goes up in flames and you die. Your pitiful life has come to an end!")
elif choiceP == "B":
  print("\nThey’re dead. You scream. The bus crashes. You are thrown out a window. Your pitiful life has come to an end!")