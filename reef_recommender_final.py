# This program recommends a reef in Monterey or Carmel depending on the 
#diver's criteria including ability, location, and photography.
import csv					

# display menu choice and ask user input 
def diver_choice_menu():
	print """
	0 - Main Menu
	1 - Choose reefs based on ability.
	2 - Choose reefs based on location.
	3 - Choose reefs based on photography.
	4 - Choose reefs based on access: boat or beach.
	5 - Show complete list of reefs.
	6 - Type exit when you are done.
	"""	
	choice = int(raw_input("Choose from the menu options. "))
	return choice

# Designates diver skill based on the number of dives done in the last 2 years.
def number_dives(num):
	if num <= 40:
		diver_skill = "Beginner"	
	elif 40 < num <= 100:
		diver_skill = "Intermediate"
	elif num > 100:
		diver_skill = "Advanced"	
	return diver_skill

# Recommends reef based on the diver skill, determined by the number of dives.
def diver_ability(diver_skill):
	input_reef = csv.DictReader(open("reef_master_v2.csv"))
	recommend_reef = []
	for reef in input_reef: 
		if reef["Skill Level"] == diver_skill:
			recommend_reef.append(reef)
	return recommend_reef

# Recommends reef based on where diver wants to dive
def dive_location(place):
	input_reef = csv.DictReader(open("reef_master_v2.csv"))
	recommend_reef = []
	if place == "m":
		place = "Monterey Bay"
	elif place == "c":
		place = "Carmel"

	for reef in input_reef:
		for key, value in reef.items():
			if place == value: 
				recommend_reef.append(reef)
	return recommend_reef

# Recommends reef based on diver's photograpy desire
def dive_photo(photo):
	input_reef = csv.DictReader(open("reef_master_v2.csv"))
	recommend_reef = []	
	if photo == "r":
		photo = "Macro"
	elif photo == "w":
		photo == "Wide-angle"
	elif photo == "b":
		photo == "Macro and Wide-angle"	

	for reef in input_reef:
		for key, value in reef.items():
			if photo == value: 
				recommend_reef.append(reef)
	return recommend_reef

# Recommends reef based on how diver accesses the site
def dive_access(beach_boat):
	input_reef = csv.DictReader(open("reef_master_v2.csv"))
	recommend_reef = []	
	if beach_boat == "h":
		beach_boat = "Beach"
	elif beach_boat == "t":
		beach_boat == "Boat"	

	for reef in input_reef:
		for key, value in reef.items():
			if beach_boat == value: 
				recommend_reef.append(reef)
	return recommend_reef


# print out reef recommendation based on criteria
def display_reef(reef_list):
	for reef in reef_list:
		print "Reef Name:", reef["Name"], "Location:", reef["Location"], "Depth:", reef["Depth"], "Access:", reef["Access"], "Visibility:", reef["Viz"], "Level:", reef["Skill Level"], "Photography:", reef["Photography"], "Cautions:", reef["Cautions"]

def main():
	choice = diver_choice_menu()

	while True:
		if choice == 0: 
			choice = diver_choice_menu()
				
		# determines skill user based on number of dives in the last 2 years	
		elif choice == 1:
			num = int(raw_input("How many dives have you had in the last 2 years? "))
			diver_skill = number_dives(num) # calls number_dives function, assigns variable 
			reef_list = diver_ability(diver_skill) # call reef_recommend function using dive_ability function, displays reefs
			display_reef(reef_list)
			choice = diver_choice_menu()

		# recommends reef based on location, Monterey or Carmel
		elif choice == 2:
			place = raw_input("Where would you like to dive? Enter 'm' for Monterey and 'c' for Carmel: ")
			place_input = dive_location(place) 
			display_reef(place_input)# call display reef function using dive_location function, displays reefs	
			choice = diver_choice_menu()

		elif choice == 3:
			photo = raw_input("What type of photography would you like to do? Enter 'r' for Macro, 'w' for Wide-angle and 'b' for both: ")
			photo_input = dive_photo(photo) 
			display_reef(photo_input)# call display reef function using dive_photo function, displays reefs	
			choice = diver_choice_menu()

		elif choice == 4:
			access = raw_input("How would you like to access the dive site? Enter 'h' for beach, 't' for boat: ")
			beach_boat = dive_access(access) 
			display_reef(beach_boat)# call display reef function using dive_access function, displays reefs	
			choice = diver_choice_menu()

		elif choice == 5:
			input_reef = csv.DictReader(open("reef_master_v2.csv"))
			display_reef(input_reef)
			choice = diver_choice_menu()

		elif choice == 6:
			break

if __name__ == '__main__':
	main()				



