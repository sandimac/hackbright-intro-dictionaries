# my_stats = {"height":"64", "age":"27", "name":"Alexis"}

# print my_stats["name"], "is", my_stats["age"], "years old with a height of", my_stats["height"]
# del my_stats["age"]
# print my_stats

# vocabulary_words = {
# 	"boolean" :"True or False statement", 
# 	"integer":"whole number", 
# 	"tuple": "List of immutable items", 
# 	"iterate": "To run through"
# }


my_name = "sandi macpherson"

letters = []

for i in my_name:
	letters.append(i)
# print letters

index = 0
d = {}

for i in letters:
	if i in d:
		d[i]+=1
	else:
		d[i]=1


print[d]		