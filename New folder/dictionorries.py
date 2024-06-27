month = {
    "jan": 'january',
    'feb': 'february',
    'mar': 'march',
}
print(month['mar'])
                       #dedfult value
print(month.get('jan','not valid key'))




#H = {
   # 'name':'N/A',
   #  'phone':'N/A'
   #  'address':'N/A'
#}

#M = {
  #  'name':'rick',
   # 'phone':'7821893947'
#}   

#H |= M 

  
dic = {
    'u':'uday shaharwale',
    'b':'bruce',
    't':'tony',
    'm':'mike',
}
while True:
     put = input('enter: ')
     print(dic.get(put,"invailed!"))

