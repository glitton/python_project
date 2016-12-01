# This program recommends a reef depending on various criteria such as ability, location, and photography

# create csv file of reefs, convert list to dictionary and read the file
import csv
input_reef = open_csv("reef_master.csv")

def open_reef_csv(("reef_master.csv"):
	with open(filepath) as file_in:
		input_reef = csv.DictReader(file_in)
	return input_reef

#Ask how many dives had in the last year, determines ability
def dive_ability(ability):
	if ability <= 30:
		diver_skill = "Beginner"	
	elif 30 < ability <= 100:
		diver_skill = "Intermediate"
	elif ability > 100:
		diver_skill = "Advanced"	
	return diver_skill	

# 1 menu, compare ability with csv Skill level and then print out appropriate reefs
def reef_skill_level(reef_ability, input_reef):
	recommend_reef = []
	for reef in input_reef: 
		if reef["Skill Level"] == reef_ability:
			recommend_reef.append(reef)
	return recommend_reef	

#2 menu, function that shows reef based on location.  Choices are Monterey or Carmel
def reef_location(location):
	recommend_reef = []
	if location == "m":
		location = "Monterey Bay"
	elif location == "c":
		location = "Carmel"
	for reef in input_reef:
		for key, value in reef.items():
			if location == value: 
				recommend_reef.append(reef)
	return recommend_reef	

# 3 menu, determines whether the diver wants a reef that is best for macro, wide-angle or both
def photo_type(macro_wide):
	if reef["Photography"] == macro_wide.lower('r'):
		photo = "Macro"
	elif reef["Photography"] == macro_wide.lower('w'):
		photo = "Wide-angle"
	elif reef["Photography"] == macro_wide.lower('b'):
		photo = "Macro and Wide-angle"
	return photo_type	

# print out reef recommendations
def display_reef(recommend_reef_list):
	for reef in recommend_reef_list:
		print "Reef Name:", reef["Name"], "Location:", reef["Location"], "Depth:", reef["Depth"], "Access:", reef["Access"], "Visibility:", reef["Viz"], "Level:", reef["Skill Level"], "Photography:", reef["Photography"], "Cautions:", reef["Cautions"]

# menu for user to display reefs based on their criteria
def diver_choice():

	choice = int(raw_input("Choose from the menu options. "))
	return choice
# displays menu

def display_menu():
	print """
	0 - Main Menu
	1 - Choose reefs based on ability.
	2 - Choose reefs based on location.
	3 - Choose reefs based on photography.
	4 - Show complete list of reefs.
	5 - Type exit when you are done.
	"""	

# main function 
def main():
	

	while True:
	#shows main menu
		display_menu()
		choice = diver_choice()
		if choice == 0: 
			choice = diver_choice()
	# determines skill user based on number of dives in the last 2 years	
		elif choice == 1:
			ability = int(raw_input("How many dives have you had in the last 2 years? "))
			reef_ability = dive_ability(ability) # calls dive_ability function, assigns variable 
			recommend_reef_list = reef_skill_level(reef_ability) # call reef_recommend function using dive_ability function, displays reefs
			display_reef(recommend_reef_list)
		elif choice == 2:
			location_input = raw_input("Where would you like to dive? Enter 'm' for Monterey and 'c' for Carmel: ")
			# reef_location_input = reef_location(location_input) 
			recommend_reef_list = reef_location(location_input) # call reef_recommend function using reef_location function, displays reefs
			print recommend_reef_list
			display_reef(recommend_reef_list)
			# choice = 0 # prompt with the main menu	
if __name__ == '__main__':
		main()	

