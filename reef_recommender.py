# This program recommends a reef depending on the diver's ability

# create csv list of reefs
# ask user their ability
# compare answer with reef list
# print out reef aligned with their ability

import csv
input_reef = csv.DictReader(open("reef_master1.csv"))

#Ask how many dives had in the last year? Will recommend reef based on ability
def dive_ability(ability):
	if ability <= 30:
		diver_skill = "Beginner"	
	elif 30 < ability <= 100:
		diver_skill = "Intermediate"
	elif ability > 100:
		diver_skill = "Advanced"	
	return diver_skill	

# compare ability with Dictionary Skill level and then print out appropriate reefs
def reef_recommend(reef_ability):
	recommend_reef = []
	for reef in input_reef: 
		if reef["Skill Level"] == reef_ability:
			recommend_reef.append(reef)
	return recommend_reef	

def display_reef(recommend_reef):
	for reef in recommend_reef:
		print reef["Name"], reef["Location"]


def main():
	ability = int(raw_input("How many dives have you had in the last year? "))
	reef_ability = dive_ability(ability)
	recommend_reef = reef_recommend(reef_ability)
	display_reef(recommend_reef)
	# print "We recommend these reefs: ", reef["Name"]

main()	

