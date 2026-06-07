import webbrowser #importing required library

#defined required functions
def map1(latitude, longitude):
    url = f"https://www.google.com/maps?q={latitude},{longitude}"
    print("Opening:", url)
    webbrowser.open(url)
    print("You are being redirected to Google Maps")

def map2(address):
    url = f"https://www.google.com/maps/search/{address}"
    print("Opening:", url)
    webbrowser.open(url)
    print("You are being redirected to Google Maps")

#question output
print("""
Select any option:
    1. Address
    2. Latitude and Longitude
""")

#program ends with user input
selection = int(input(">> "))

if selection == 1:
    address = input("Give the address >> ")
    map2(address)

elif selection == 2:
    latitude = input("Latitude >> ")
    longitude = input("Longitude >> ")
    map1(latitude, longitude)

else:
    print("That was a wrong input. Try again!")

