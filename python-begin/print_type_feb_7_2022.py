company = 'Tesla'
model = 'Model 3'
fsd = 12000
base_price = 36000
tax_per = 7.5
retail = (fsd + base_price)
tax = ((fsd + base_price) * tax_per )/100

print(retail+tax)
print(type(company))
print(type(base_price))
print(type(tax_per))
print(type(retail))
