from replit import clear
from art import logo

print(logo)
print ("Welcome to the secret auction program.")
list_of_bid = {}
run = True
while run == True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  list_of_bid[name] = bid
  choice = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if choice == "yes":
    clear()
  elif choice == "no":
    run = False

max_bid = []
for a in list_of_bid:
  x = list_of_bid[a]
  max_bid.append(x)

z = max(max_bid)

for b in list_of_bid:
  if list_of_bid[b] == z:
    print (f"The winner is {b} with a bid of ${z}.")

 