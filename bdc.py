#!/usr/bin/python

from __future__ import print_function
import os
from datetime import date, datetime
import json


datafile = '/users/lizzie/bin/burns-depression-checklist/bdc-data.json'

# functions

def check_for_datafile():
	if os.path.isfile(datafile) and os.access(datafile, os.R_OK):
		# checks if file exists
		# print("file exists and is readable")
		return
	else:
		# print("either file is missing or is not readable, creating file...")
		open(datafile, 'a').close()

def get_answer(prompt):
	while True:
		try:
			value = int(raw_input(prompt))
		except ValueError:
			print("\nYour answer should be a number between 0 and 4, where:\n0 - not at all\n1 - somewhat\n2 - moderately\n3 - a lot\n4 - extremely\n")
			# continue
		else:
			if 0 <= value <= 4:
				break
			else:
				print("\nYour answer should be a number between 0 and 4, where:\n0 - not at all\n1 - somewhat\n2 - moderately\n3 - a lot\n4 - extremely\n")
	return value


# the program

os.system('clear')
check_for_datafile()
score = 0

print("BURNS DEPRESSION CHECKLIST")
print("**************************")
print("\nIndicate how much you have experienced each symptom during the past week, where:")
print("\n0 - not at all\n1 - somewhat\n2 - moderately\n3 - a lot\n4 - extremely")

print("\npart 1: thoughts and feelings\n")
score += get_answer("1. Feeling sad or down in the dumps: ")
score += get_answer("2. Feeling unhappy or blue: ")
score += get_answer("3. Crying spells or tearfulness: ")
score += get_answer("4. Feeling discouraged: ")
score += get_answer("5. Feeling hopeless: ")
score += get_answer("6. Low self-esteem: ")
score += get_answer("7. Feeling worthless or inadequate: ")
score += get_answer("8. Guilt or shame: ")
score += get_answer("9. Criticizing yourself or blaming yourself: ")
score += get_answer("10. Difficulty making decisions: ")


print("\npart 2: activities and personal relationships\n")
score += get_answer("11. Loss of interest in family, friends or colleagues: ")
score += get_answer("12. Loneliness: ")
score += get_answer("13. Spending less time with family or friends: ")
score += get_answer("14. Loss of motivation: ")
score += get_answer("15. Loss of interest in work or other activities: ")
score += get_answer("16. Avoiding work or other activities: ")
score += get_answer("17. Loss of pleasure or satisfaction in life: ")


print("\npart 3: physical symptoms\n")
score += get_answer("18. Feeling tired: ")
score += get_answer("19. Difficulty sleeping or sleeping too much: ")
score += get_answer("20. Decreased or increased appetite: ")
score += get_answer("21. Loss of interest in sex: ")
score += get_answer("22. Worrying about your health: ")


print("\npart 4: suicidal urges\n")
score += get_answer("23. Do you have any suicidal thoughts?: ")
score += get_answer("24. Would you like to end your life?: ")
score += get_answer("25. Do you have a plan for harming yourself?: ")


print("\nYou've scored", score, "on the Burns Depression Checklist.")

if score <= 5:
	print("You show no signs of depression.")
elif 6 <= score <= 10:
	print("You are normal but unhappy.")
elif 11 <= score <= 25:
	print("You show signs of mild depression.")
elif 26 <= score <= 50:
	print("You show signs of moderate depression.")
elif 51 <= score <= 75:
	print("You show signs of severe depression.")
else:
	print("You show signs of extreme depression.")
print("\n")

today = date.today()
now = datetime.now()

entry = {
	str(today): str(score)
}

# update the json datafile with the new entry, or fill in with entry if empty

with open(datafile) as f:
	if os.stat(datafile
).st_size != 0:
		data = json.load(f)
		data.update(entry)
	else:
		data = entry

with open(datafile, 'w') as f:
	json.dump(data, f)

