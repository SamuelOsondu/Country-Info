# pip install countryinfo -- run this on a terminal to install the module.

# Import the module
from countryinfo import CountryInfo

# Getting a country name from the user.

desired_country = input("Please enter a country name: ")
country = CountryInfo(desired_country)

# Let's get some information about the given country (Not limited to this)

print(f"{desired_country}'s alternate spelling is : ", country.alt_spellings())
print(f"The capital of {desired_country} is : ", country.capital())
print(f"{desired_country}'s currency of is :", country.currencies())
print(f"{desired_country}'s language is : ", country.languages())
print(f"{desired_country}'s borders are : ", country.borders())
print(f"{desired_country}'s calling code is : ", country.calling_codes())
print(f"{desired_country}'s capital latitude and longitude : ", country.capital_latlng())
print(f"{desired_country}'s population is : ", country.population())


