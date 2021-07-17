import phonenumbers

from phonenumbers import geocoder, carrier

phone = input("Digite o telefone no formato +551140028922: ")

phone_number = phonenumbers.parse(phone)


print(geocoder.description_for_number(phone_number, 'pt'))
print(carrier.name_for_number(phone_number, "pt"))