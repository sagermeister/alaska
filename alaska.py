#to do list:
#implement starvation
#action points till starvation/health decrease
#weather forces action points to be depleted and starvation to increase (ie shoveling snow)
#medicine, cooking pot, matches, lighter implementation
#score

import sys
import os
import random

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

clear()

#=================
#Initial Inventory
#=================

#Bear Meat, Elk Meat, Rabbit Meat,
#Bear Hide, Elk Hide, Rabbit Hide,
#Food Rations, Medicine, Water,
#Hunting Knife, Hunting Rifle,
#Bullets, Cooking Pot, Matches,
#Lighter, Snare, Money, 

bmeat = 1
emeat = 1
rmeat = 1
bhide = 0
ehide = 0
rhide = 0
food = 1
meds = 0
water = 0
knife = 1
rifle = 1
bullt = 100
cookp = 0
match = 0
light = 0
snare = 5
money = 300
day = 1
health = 100
hunger = 100

inv = [bmeat, emeat, rmeat, bhide, ehide, rhide, food, meds, water, knife, rifle, bullt, cookp, match, light, snare, money]

#====================
#General Store Prices
#====================

#Sell prices
bmeatsp = 30
emeatsp = 15
rmeatsp = 5
bhidesp = 20
ehidesp = 10
rhidesp = 1
foodsp = 5
medssp = 5
watersp = 5
knifesp = 5
riflesp = 200
bulltsp = 5
cookpsp = 10
matchsp = 1
lightsp = 2
snaresp = 5

sellinv = [bmeatsp, emeatsp, rmeatsp, bhidesp, ehidesp, rhidesp, foodsp, medssp, watersp, knifesp, riflesp, bulltsp, cookpsp, matchsp, lightsp, snaresp]

#Buy prices
bmeatbp = 60
emeatbp = 30
rmeatbp = 10
bhidebp = 40
ehidebp = 20
rhidebp = 2
foodbp = 10
medsbp = 30
waterbp = 10
knifebp = 10
riflebp = 400
bulltbp = 10
cookpbp = 30
matchbp = 2
lightbp = 5
snarebp = 10

buyinv = [bmeatbp, emeatbp, rmeatbp, bhidebp, ehidebp, rhidebp, foodbp, medsbp, waterbp, knifebp, riflebp, bulltbp, cookpbp, matchbp, lightbp, snarebp]

#===================
#Hunting Probability
#===================

bearprob = 0.1
deerprob = 0.2
rabbitprob = 0.3
snarebearp = 0.05
snaredeerp = 0.1
snarerabbitp = 0.5

huntp = [bearprob, deerprob, rabbitprob, snarebearp, snaredeerp, snarerabbitp]

#==================
#Buy & Sell Strings
#==================

bmeatstr = " bear meat"
emeatstr = " deer meat"
rmeatstr = " rabbit meat"
bhidestr = " bear hide"
ehidestr = " deer hide"
rhidestr = " rabbit hide"
foodstr = " food rations"
medsstr = " medicine"
waterstr = " water"
knifestr = " hunting knife"
riflestr = " hunting rifle"
bulltstr = " bullet(s)"
cookpstr = " cooking pot"
matchstr = " match(es)"
lightstr = " lighter"
snarestr = " snare(s)"

strinv = [bmeatstr, emeatstr, rmeatstr, bhidestr, ehidestr, rhidestr, foodstr, medsstr, waterstr, knifestr, riflestr, bulltstr, cookpstr, matchstr, lightstr, snarestr]

#=========
#Functions
#=========

#Needs filtering and names (dictionary??)
#def checkinv():
#	print(inv)

def chkhealth():
	global health	
	if health <= 0:
		print("You died.")
	else:
		actions()		
		return

def actions():
	print("\nWhat do you want to do?\n1 - Shop at General Store\n2 - Hunt\n3 - Eat\n4 - Sleep\n5 - Exit\n6 - Test dmghealth()\n")
	actionInput = input("Enter Selection: ")
	if actionInput == "1":
		clear()
		store()
	elif actionInput == "2":
		clear()
		hunt()
	elif actionInput == "3":
		clear()
		eat()
	elif actionInput == "4":
		clear()
		print(sleep())
	elif actionInput == "5":
		clear()
		print("Goodbye " + name + ".\n")
		sys.exit()
	elif actionInput == "6":
		#Testing stuff
		clear()
		print(inv)
		actions()
	else:
		gamebreak()

def store():
	clear()
	global inv, buyinv, strinv
	print("Do you want to buy or sell?\n\n1 - Buy\n2 - Sell\n3 - Go Back\n")
	buysellInput = input("Enter Selection: ")
	if buysellInput == "1":
		clear()
		print("What do you want to buy?\n\n1 - Food\n2 - Medicine\n3 - Water\n4 - Hunting Knife\n5 - Hunting Rifle\n6 - Rifle Ammo\n7 - Cooking Pot\n8 - Matches\n9 - Lighter\n10 - Snare\n")
		buyInput = input("Enter Selection: ")
		try:
			int(buyInput)
		except ValueError:
			gamebreak()
		buy(buyInput)
		store()
	elif buysellInput == "2":
		clear()
		print("What do you want to sell?\n\n1 - Bear Meat\n2 - Deer Meat\n3 - Rabbit Meat\n4 - Bear Hide\n5 - Deer Hide\n6 - Rabbit Hide\n7 - Food Rations\n8 - Medicine\n9 - Water\n10 - Hunting Knife\n11 - Hunting Rifle\n12 - Rifle Ammo\n13 - Cooking Pot\n14 - Matches\n15 - Lighter\n16 - Snare\n")
		sellInput = input("Enter Selection: ")
		try:
			int(sellInput)
		except ValueError:
			gamebreak()
		sell(sellInput)
		store()
	elif buysellInput == "3":
		clear()
		actions()
	else:
		gamebreak()

def buy(i):
	global inv, strinv, buyinv
	clear()
	print("Your bank: $" + str(inv[16]) + ".\nHow many do you want to buy? Price: $" + str(buyinv[int(i)+5]) + ".\n")
	purchase = input("Enter Selection: ")
	try:
		int(purchase)
	except ValueError:
		gamebreak()
	if inv[16] >= (inv[int(i)+5]*buyinv[int(i)+5]):
		clear()
		inv[int(i)+5] += int(purchase)
		inv[16] -= (int(purchase)*buyinv[int(i)+5])
		print("You now have " + str(inv[int(i)+5]) + str(strinv[int(i)+5]) + ". Your bank is $" + str(inv[16]) + ".")
		actions()
	elif inv[16] < (inv[int(i)+5]*buyinv[int(i)+5]):	#if inv[money] < (quantity*itemprice)
		clear()
		print("You don't have enough money to buy that much!")
		store()
	else:
		gamebreak()
	store()

def sell(i):											#i is array position +1
	global inv, strinv, sellinv
	clear()
	print("Your bank: $" + str(inv[16]) + ".\nHow many do you want to sell? Price: $" + str(sellinv[int(i)-1]) + ".\n")
	sale = input("Enter Selection: ")					#sale is number of purchases
	try:
		int(sale)
	except ValueError:
		gamebreak()
	if int(sale) <= inv[int(i)-1]: 						#if requested sale is less than inv
		clear()
		inv[16] += (int(sale)*sellinv[int(i)-1])			#money += (quantity*itemsellprice)
		inv[int(i)-1] -= int(sale)
		print("You now have " + str(inv[int(i)-1]) + str(strinv[int(i)-1]) + ". Your bank is $" + str(inv[16]) + ".")
		actions()
	elif int(sale) > inv[int(i)-1]:
		print("You dont have enough" + str(strinv[int(i)-1]) + " to complete that sale.")
		store()
	else:
		gamebreak()
	store()

def hunt():
	#inv[9] is knife, inv[10] is rifle, inv[11] is bullets, inv[15] is snare
	clear()
	global inv, huntp
	print("You have " + str(inv[10]) + " rifle, " + str(inv[11]) + " bullet(s), and " + str(inv[15]) + " snare(s).\nWhat do you want to use to hunt?\n\n1 - Rifle\n2 - Snare\n3 - Go Back\n")
	huntInput = input("Enter Selection: ")
	if huntInput == "1":
		clear()
		if inv[10] < 1 or inv[11] < 1 or inv[9] < 1:
			clear()
			if inv[10] < 1:
				print("You don't have a rifle!")
				actions()
			if inv[11] < 1:
				print("You don't have any bullets!")
				actions()
			if inv[9] < 1:
				print("You don't have a knife to gather meat!")
				actions()
		print("How many bullets do you want to use?\n")
		bulltInput = input("Enter Selection: ")
		bulltInput = int(bulltInput)
		if bulltInput > inv[11]:
			clear()
			print("You don't have that many bullets!")
			actions()
		#huntp[0] is bearprob, huntp[1] is deerprob, huntp[2] is rabbitprob
		hitBear = round(random.random() * (bulltInput/3) * huntp[0])
		hitDeer = round(random.random() * (bulltInput/3) * huntp[1])
		hitRabbit = round(random.random() * (bulltInput/3) * huntp[2])
		clear()
		print("You got " + str(hitBear) + " bear meat and bear hides, " + str(hitDeer) + " deer meat and deer hides, " + str(hitRabbit) + " rabbit meat and rabbit hides.")
		inv[0] += hitBear
		inv[1] += hitDeer
		inv[2] += hitRabbit
		inv[3] += hitBear
		inv[4] += hitDeer
		inv[5] += hitRabbit
		
	elif huntInput == "2":
		clear()
		if inv[15] < 1 or inv[9] < 1:
			if inv[15] < 1:
				print("You don't have any snares!")
				actions()
			if inv[9] < 1:
				print("You don't have a knife to gather meat!")
				actions()
		snareInput = input("How many snares do you want to set?")
		snareInput = int(snareInput)
		if snareInput > inv[15]:
			clear()
			print("You don't have that many snares.")
			actions()
		#huntp[3] is snarebearp, huntp[4] is snaredeerp, huntp[5] is snarerabbitp
		catchBear = round(random.random() * (snareInput/3) * snarebearp)
		catchDeer = round(random.random() * (snareInput/3) * snaredeerp)
		catchRabbit = round(random.random() * (snareInput/3) * snarerabbitp)
		clear()
		print("You got " + str(catchBear) + " bear meat and bear hides, " + str(catchDeer) + " deer meat and deer hides, " + str(catchRabbit) + " rabbit meat and rabbit hides.")
	elif huntInput == "3":
		clear()
		actions()
	else:
		gamebreak()
		
def eat():
	#inv[0] is bear, inv[1] is deer, inv[2] is rabbit, inv[6] is food
	clear()
	global inv, health, hunger
	print("You have " + str(inv[0]) + " bear meat, " + str(inv[1]) + " deer meat, " + str(inv[2]) + " rabbit meat, and " + str(inv[6]) + " food rations. What would you like to eat?\n\n1 - Bear Meat\n2 - Deer Meat\n3 - Rabbit Meat\n4 - Food Ration\n5 - Go Back\n")
	eatInput = input("Enter Selection: ")
	if eatInput == "1":
		if inv[0] < 1:
			clear()
			print("You don't have any Bear Meat.")
			actions()
		else:		
			health += 25
			hunger += 50
			inv[0] -= 1
			if health > 100:
				health = 100
			if hunger > 100:
				hunger = 100
			clear()
			print("Your health has increased to " + str(health) + ". Your hunger has increased to " + str(hunger) + ". And your Bear Meat has decreased to " + str(inv[0]) + ".")
	elif eatInput == "2":
		if inv[1] < 1:
			clear()
			print("You don't have any Deer Meat.")
			actions()
		else:
			health += 15
			hunger += 25
			inv[1] -= 1
			if health > 100:
				health = 100
			if hunger > 100:
				hunger = 100
			clear()
			print("Your health has increased to " + str(health) + ". Your hunger has increased to " + str(hunger) + ". And your Deer Meat has decreased to " + str(inv[1]) + ".")
	elif eatInput == "3":
		if inv[2] < 1:
			clear()
			print("You don't have any Rabbit Meat.")
			actions()
		else:
			health += 5
			hunger += 10
			inv[2] -= 1
			if health > 100:
				health = 100
			if hunger > 100:
				hunger = 100
			clear()
			print("Your health has increased to " + str(health) + ". Your hunger has increased to " + str(hunger) + ". And your Rabbit Meat has decreased to " + str(inv[2]) + ".")
	elif eatInput == "4":
		if inv[6] < 1:
			clear()
			print("You don't have any Food Rations.")
			actions()
		else:
			health += 30
			hunger += 80
			inv[6] -= 1
			if health > 100:
				health = 100
			if hunger > 100:
				hunger = 100
			clear()
			print("Your health has increased to " + str(health) + ". Your hunger has increased to " + str(hunger) + ". And your Food Rations have decreased to " + str(inv[6]) + ".")
	elif eatInput == "5":
		clear()
		actions()
	else:
		gamebreak()

def sleep():
	global day, hunger, health
	day += 1
	return "Good morning, Today is " + str(day) + ". Your hunger has decreased by 25, and your health has increased by 25."
	health += 25
	hunger -= 25

def dmghealth(i):
	global health
	health -= i
	return "You've taken damage. Your health is now " + str(health) + "."

def gamebreak():
	global inv
	clear()
	inv[16] -= 10
	print("Attempt to break the game: Failed!\nYour bank has decreased by $10.")
	actions()
		
#=============
#Game Run Time
#=============
print("[][][][][][][][][][][][][][][][][][]\n|Welcome to Alaska Winter Survival!|\n[][][][][][][][][][][][][][][][][][]\n")
name = input("Please enter your name: ")
clear()
if name == "dev":
	inv[16] = 10000
	print("Attempt to break the game: Success!\nYou now have $10,000...cheater.")
elif name == "Les":
	inv[16] = 0
	inv[15] = 5
	inv[9] = 1
	print("Survivor man extraordinaire! Today is day " + str(day) + ". You have $0, 1 knife, and 5 snares. Good luck...")
else:
	print("Hello " + str(name) + ". Today is day " + str(day) + ".")
while health > 0:
	chkhealth()
clear()
print("You died.")
sys.exit()

	
