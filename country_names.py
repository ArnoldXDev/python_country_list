# install pycountry 
# pip install pycountry
# =========================
# country_names.py
# =========================
# This Python script displays a list of all countries using the pycountry library.
# It fetches the country names based on ISO standards and prints them to the console.

import pycountry

def display_all_countries():
    # Fetch all countries
    countries = pycountry.countries
    # Print the name of each country
    for country in countries:
        print(country.name)

# Call the function to display all countries
display_all_countries()
