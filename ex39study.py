#create a mapping of state to abbreviation


counties = {
	"Bucuresti": "Buc",
	"Arges": "AG",
	"Maramures": "MR",
	"Olt": "OT",
	"Constanta": "CT",
	"Brasov": "BV",
	"Cluj-Napoca": "CJ",
	"Sibiu": "SB",
	"Timis": "TM",
	"Bihor": "BH"
}

#create a basic set of states and some cities in them
towns = {
	"AG": "Pitesti",
	"SB": "Sibiu",
	"OT": "Slatina",
	"TM": "Timisoara",
	"BH": "Oradea",
	"CJ": "Cluj",
	"Buc": "Bucuresti"

}

# add some more cities
towns["TM"] = "Timisoara"
towns["MR"] = "Baia Mare"
towns["CT"] = "Constanta"
towns["MR"] = "Baia Mare"
towns["CT"] = "Constanta"
towns["BV"] = "Brasov"



# print(orase)

# print some cities 
print('*' * 30)
print(towns["TM"], " is a town in the county of Timis, Romania.")
print("Arges county has as city ", towns["AG"], ".")
print("Oradea is situated in the county", counties["Bihor"], ".")

# print some states
print('*' * 30)
print("Bucuresti abbreviation is", counties["Bucuresti"], ".")
print("The abbreviation of Cluj-Napoca is", counties["Cluj-Napoca"],".")

# do it by using the state and cities dict
print('*' * 30)
print("Arges has:", towns[counties["Arges"]])
print("Timis has:", towns[counties["Timis"]])
print("Bihor has:", towns[counties["Bihor"]])

# print every state abbreviation
print('*' * 30)
for county, abbrev in list(counties.items()):
	print(f"{county} is abbreviated as {abbrev}")


# print every city in state
print('*' * 30)
for abbrev, town in list(towns.items()):
	print(f"{abbrev} has the town {town}.")

# now do both at the same time
print('*' * 30)
for county, abbrev in list(counties.items()):
	print(f"{county} county is abbreviated as {abbrev}.")
	print(f"and has city {towns[abbrev]}")
	

# safely get a abbreviation by state that might not be there
print('*' * 30)
county = counties.get("Teleorman")

if not county:
	print("Sorry, no Teleorman")

# get a city with a default value
print('*' * 30)
town = towns.get("TL", "Doesn't exist")
print(f"The city for the county of 'TL' is {town}")



