'''numbers=[1,2,3,4,5,6,7,8,9,10]
header ='|{:^12}|{:^12}|{:^12}|'.format('int','int^2','int^3')

separator=len(header)*'-'
#print(separator,header,separator,sep='\n')
body= ''
for num in numbers:
    body+='|{:^12}|{:^12}|{:^12}|\n'.format(num,num**2,num**3)
table='\n'.join([separator,header,separator,body,separator])
print(table)
 '''
numbers=[1,2,3,4,5,6,7,8,9,10]
header ='|{:^12}|{:^12}|{:^12}|{:^12}|'.format('int','dex','oct','bin')

separator=len(header)*'-'
#print(separator,header,separator,sep='\n')
body= ''
for num in numbers:
    body+='|{0:^12d}|{0:^12x}|{0:^12o}|{0:^12b}|\n'.format(num)
table='\n'.join([separator,header,separator,body,separator])
print(table)