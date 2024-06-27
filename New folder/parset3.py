product = int(input('etner product:'))
bill = product * 100

if int(bill)>1000 :
    discount= bill * 0.05
    bill = bill - discount
    print('your bill is ',bill)
else :
    print('your bill is',bill)




