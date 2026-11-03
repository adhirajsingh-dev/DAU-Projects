prices=[]
while True:
    a=input('Enter a price(or enter exit to end):')
    if a.upper()=='EXIT':
        break
    prices.append(float(a))

def tax_price(x):
    return (108.0*x)/100.0
taxes=list(map(tax_price,prices))
print(taxes)

filt_price=list(filter(lambda x:x>10.0,prices))
print(filt_price)
