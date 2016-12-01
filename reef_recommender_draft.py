# This program recommends a reef depending on various criteria such as ability, location, and photography

# create csv file of reefs, convert list to dictionary and read the file
import csv
input_reef = csv.DictReader(open("reef_master.csv"))

#Ask how many dives had in the last year, determines ability
def dive_ability(ability):
	if ability <= 30:
		diver_skill = "Beginner"	
	elif 30 < ability <= 100:
		diver_skill = "Intermediate"
	elif ability > 100:
		diver_skill = "Advanced"	
	return diver_skill	

def location(location_input):
	if location == "m":
		location = "Monterey Bay"
	elif location == "c":
		location = "Carmel"	

# 1 menu, compare ability with csv Skill level and then print out appropriate reefs
def reef_skill_level(reef_ability):
	recommend_reef = []
	for reef in input_reef: 
		if reef["Skill Level"] == reef_ability:
			recommend_reef.append(reef)
	return recommend_reef	

#2 menu, function that shows reef based on location.  Choices are Monterey or Carmel
def reef_location(location):
	recommend_reef = []
	for reef in input_reef:
		if reef["Location"] == location_list:
			recommend_reef.append(reef)
	return recommend_reef		


	# for reef in input_reef:
	# 	for key, value in reef.items():
	# 		if location == value: 
	# 			recommend_reef.append(reef)
	# return recommend_reef	

# print out reef recommendations
def display_reef(recommend_reef_list):
	for reef in recommend_reef_list:
		print "Reef Name:", reef["Name"], "Location:", reef["Location"], "Depth:", reef["Depth"], "Access:", reef["Access"], "Visibility:", reef["Viz"], "Level:", reef["Skill Level"], "Photography:", reef["Photography"], "Cautions:", reef["Cautions"]

ability = int(raw_input("How many dives have you had in the last 2 years? "))
reef_ability = dive_ability(ability) # calls dive_ability function, assigns variable 
recommend_reef_list = reef_skill_level(reef_ability) # call reef_skill_level function using dive_ability function
display_reef(recommend_reef_list)

# location_input = raw_input("Where would you like to dive? Enter 'm' for Monterey and 'c' for Carmel: ")
# location_list = location(location_input)
# recommend_reef_list = reef_location(location_list) # call reef_location function using reef_location function, displays reefs
# print display_reef(recommend_reef_list)

		
	

