#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.

print("\nThe bus driver pulls out a knife.")
choiceK = input("\nEnter A to run to the back of the bus or B to try and talk down the bus driver: ").upper()
while choiceK != "A" and choiceK != "B":
  print("\nThat is not a valid option.")
  choiceK = input("\nEnter A to run to the back of the bus or B to try and talk down the bus driver: ").upper()
if choiceK == "A":
  import sleeping
elif choiceK == "B":
  print("\nYou are not very persuasive. The bus driver stabs you. Your pitiful life has come to an end!")
