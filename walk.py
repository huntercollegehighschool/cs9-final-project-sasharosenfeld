print("\nYou set off home. It's pretty empty today, which is weird. It's the middle of the city, and it's not that later. Whatever. You're too focused on those eyes you feel, and now you think you hear footsteps behind you, but can’t see anyone. Maybe it'd be a good idea to find other people...")
choiceB = input("\nEnter A to keep walking or B to go into a shop: ").upper()
while choiceB != "A" and choiceB != "B":
  print("\nThat is not a valid option.")
  choiceB = input("\nEnter A for keep walking or B for go into a shop: ").upper()
if choiceB == "A":
  import keepwalking
elif choiceB == "B":
  import shop
