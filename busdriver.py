print("\nYou call a greeting to the bus driver, with no response. Strange, it's not very loud. In fact, it's eerily quiet. Concerned , you walk up near the bus driver. You call out again, and this time get a reaction: The bus driver pulled out a knife!")
choiceK = input("\nEnter A to run to the back of the bus or B to try and talk down the bus driver: ").upper()
while choiceK != "A" and choiceK != "B":
  print("\nThat is not a valid option.")
  choiceK = input("\nEnter A to run to the back of the bus or B to try and talk down the bus driver: ").upper()
if choiceK == "A":
  import sleeping
elif choiceK == "B":
  print("\nYou are not very persuasive. The bus driver stabs you. Your pitiful life has come to an end!")
  end = input("\nWant to try again? Enter R to restart: ").upper()
  if end == "R":
    print("\nToo bad. Life doesn't have second chances.")
  else: 
    print("\nGood. We weren't going to give you a second chance anyways.")