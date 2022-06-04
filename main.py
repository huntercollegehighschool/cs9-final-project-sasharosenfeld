"""
Name(s): Serena Taxin, Sasha Rosenfeld
Name of Project: Minding Your Business
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

print("You are an average person. Not very smart or fun. You don't have many friends. Your entire life is your job at the local Starbucks, where you barely interact with your coworkers. One day, on your way home, you feel almost like someone is watching you. How strange: No one ever pays attention to you. You usually walk home, but maybe the bus would be safer today...\n")

choice1 = input("Enter A to take the bus or B to walk home: ").upper()

while choice1 != "A" and choice1 != "B":
  print("That is not a valid option.")
  choice1 = input("Enter A to take the bus or B to walk home:  ").upper()
if choice1 == "A":
  import bus
elif choice1 == "B":
  import walk

