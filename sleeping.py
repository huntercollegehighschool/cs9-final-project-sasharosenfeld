print ("\nYou sprint, as fast as you can. Which isn't very fast. Still, you get to the back before the bus driver can stab you. There’s one person back here, sleeping.")
choiceS = input("\nEnter A to try and open the doors or B to ask the person for help: ").upper()
while choiceS != "A" and choiceS != "B":
  print("\nThat is not a valid option.")
  choiceS = input("\nEnter A to try and open the doors or B to ask the person for help: ").upper()
if choiceS == "A":
  print ("\nYou’re not very strong. The bus driver stabs you. Your pitiful life has come to an end!")
elif choiceS == "B": 
  print("\nThe person was NOT sleeping. They’re dead. The bus driver stabs you too. Your pitiful life has come to an end!")