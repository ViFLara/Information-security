import phonenumbers
from phonenumbers import geocoder, carrier

phone = input("Enter a phone number in the format +551140028922: ")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

# Getting carrier of a phone number
Carrier = carrier.name_for_number(phone_number, 'pt')

# Validating a phone number
valid = phonenumbers.is_valid_number(phone_number)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone_number)

# Printing the output
print(valid)
print(possible)
print(Carrier)