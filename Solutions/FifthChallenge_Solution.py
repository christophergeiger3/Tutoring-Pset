# Import tools
import re, urllib.request as scrape, sys
# I also imported 'sys' here to exit out of the program if a zodiac sign is misspelled. This isn't necessary.

# Take user input
print('Please enter your zodiac sign! ')
zodiac_number = {
    'aries': 1,
    'taurus': 2,
    'gemini': 3,
    'cancer': 4,
    'leo': 5,
    'virgo': 6,
    'libra': 7,
    'scorpio': 8,
    'sagittarius': 9,
    'capricorn': 10,
    'aquarius': 11,
    'pisces': 12,
}.get(input().strip().lower(), 0)
if zodiac_number == 0:
    print('Error. Please try again.')
    sys.exit('Zodiac sign misspelled.')

# Create a base url
base_url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="
base_url += str(zodiac_number)

# Download the page
html = scrape.urlopen(base_url)
html = str(html.read())

# Regular expressions

# Display to the user
