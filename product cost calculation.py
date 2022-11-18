
print('Enter your •	Original cost of product:')
cost = input()
print(" •	Original cost of product " + cost)
print('Enter your •	Mark-up as a %:')
 markup= input()
print(" Mark-up :	" + markup)
print('•	The price the store sells the product for:')
price = input()
print(" •	The price the store sells the product for:	" + price)
print('•	Sales tax rate as a %:')
tax = input()
print(" •	Sales tax rate as a %:	" + tax)
print('•	Total sales tax:')
ttax = ((markup+tax)*price)/100
print(" •	Total sales tax:" + ttax)
ftotal = cost + ttax  
print(" Total Cost:		" + total)
