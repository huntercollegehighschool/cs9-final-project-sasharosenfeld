print("\nAs you’re walking into the shop, you see someone in the reflection of the shop window.")
choiceB2 = input("\nEnter A to turn around or B to go into the shop: ").upper()
while choiceB2 != "A" and choiceB2 != "B":
  print("\nThat is not a valid option")
  choiceB2 = input("\nEnter A to turn around or B to go into the shop: ").upper()
if choiceB2 == "A":
  print("\nThere is a person! You have no idea who they are, but they quickly kill you. You don't even know how you die. Your pitiful life has come to an end!")
elif choiceB2 == "B":
  print("\n It is NOT a shop! You just walked into a mafia meeting. They kill you very quickly. Your pitiful life has come to an end!")
