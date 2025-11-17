from decimal import Decimal
def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    #
    res = Decimal((liters * 1000) / 1000)
    return res

def miles_gallon_to_liters_100km(miles):
    # Write your code here.
    # 1 mile = 1.609 km x 1000 = 1609 m
    res =Decimal( (miles / 1000) * 1000)
    return res

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

chatgpt version:
from decimal import Decimal, ROUND_HALF_UP

def liters_100km_to_miles_gallon(liters):
    mpg = Decimal('235.215') / Decimal(str(liters))
    return mpg.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def miles_gallon_to_liters_100km(miles):
    l_per_100km = Decimal('235.215') / Decimal(str(miles))
    return l_per_100km.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
