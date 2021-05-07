data_scientist = {
    "name": None,
    "age" : None,
    "years": None
}

data_scientist["name"] = input("Enter your name: ")
data_scientist["age"] = input("Enter your age: ")
data_scientist["years"] = input("How long have you been coding? ")
print(data_scientist)

first_languages = input("Enter the first three programming languages you learned, separated by commas: ")
lang_list = first_languages.split(",")
lang_tuple = tuple(lang_list)
data_scientist["first_languages"] = lang_tuple

fav_langs = input("Enter your favorite programming languages, separated by commas: ")
fav_list = fav_langs.split(",")
data_scientist["favorite_languages"] = fav_list

first_set = set(lang_list)
fav_set = set(fav_list)
consistant_fav = first_set.intersection(fav_set)
data_scientist["consistant_favorites"] = consistant_fav 
print(data_scientist)