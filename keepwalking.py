print("\nThe footsteps stop at some point, but you’re too distracted by a small dog in front of you to realize. It's tiny! You almost tripped over it. It was almost like it hadn't been there a second before! You've never had much of an opinion on dogs, but this one looks very sad...")
choiceB1 = input("\nEnter A to lean down to check on the dog or B to mind your own business: ").upper()
while choiceB1 != "A" and choiceB1 != "B":
  print("That is not a valid option.")
  choiceB1 = input("\nEnter A to lean down to check on the dog or B to mind your own business: ").upper()
if choiceB1 == "A":
  print("\nThe dog IS sad. It’s sad because it is incredibly hungry. Fortunately for the dog, you provide quite a bit of meat. Your pitiful life has come to an end!")
elif choiceB1 == "B":
  print("\nYou skirt around the dog and make it home. What a weird commute. You think nothing of it. You minded your own business! You survived. Nice going. Unfortunately, you were so focused on minding your own business, you forgot your little cousin had spent the day hanging out in your house. The kid removed the carbon monoxide alarm. What a brat. You go to sleep and never wake up. Your pitiful life has come to an end!")