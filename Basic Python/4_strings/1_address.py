""" 1. Create 3 variables to store street, city and country, now create address variable to
store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line """

street = "PA-01"
city = "Paris"
country = "France"

# using '+' operator
address = street+" "+city+" "+ country
print(address)

#using f-string
address = f"{street} {city} {country}"
print(address)

# Print the address in such a way that the street, city and country prints in a separate line
address = address.split()
for txt in address:
    print(txt)
