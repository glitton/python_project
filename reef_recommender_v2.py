# This program recommends a reef in Monterey or Carmel depending on the 
#diver's criteria including ability, location, and photography.
import csv
# input_reef = csv.DictReader(open("reef_master.csv"))
# funtion that opens the csv file as a dictionary

# def open_reef_csv(input_reef):
# 	file = "reef_master.csv"
# 	with open(file,'rU') as f: 
# 	    input_reef = csv.DictReader(f)
# 	    return input_reef

#open the diver csv file
# def open_reef_file():
# 	global input_reef
# 	with open("reef_master.csv") as csvfile:
# 		input_reef = csv.DictReader(csvfile)
# 		for row in input_reef:
# 			print row					

# display menu choice and ask user input 
def diver_choice_menu():
	print """
	0 - Main Menu
	1 - Choose reefs based on ability.
	2 - Choose reefs based on location.
	3 - Choose reefs based on photography.
	4 - Show complete list of reefs.
	5 - Type exit when you are done.
	"""	
	choice = int(raw_input("Choose from the menu options. "))
	return choice

def number_dives(num):
	if num <= 40:
		diver_skill = "Beginner"	
	elif 40 < num <= 100:
		diver_skill = "Intermediate"
	elif num > 100:
		diver_skill = "Advanced"	
	return diver_skill

def diver_ability(diver_skill):
	input_reef = csv.DictReader(open("reef_master.csv"))
	recommend_reef = []
	for reef in input_reef: 
		if reef["Skill Level"] == diver_skill:
			recommend_reef.append(reef)
	return recommend_reef

def dive_location(place):
	pass

def reef_location(location):	
	pass

def dive_photo(photo_type):
	pass	

def reef_photo(photo_reef):
	pass

# print out reef recommendations
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


		elif choice == 5:
			break

if __name__ == '__main__':
	main()				



