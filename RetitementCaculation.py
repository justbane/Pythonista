import math

amt_saved = 90000.00
yearly_investment = 6000.00
percent_growth = 0.12
monthly_interest = 0.06
formatted = '{total:,}'

for i in range(48, 65):
	saved = round(amt_saved + yearly_investment, 2)
	growth = round(saved * percent_growth, 2)
	amt_saved = round(saved + growth, 2)
	print('age: ', i)
	print('saved: ', formatted.format(total=saved))
	print('growth: ', formatted.format(total=growth))
	print('total saved: ', formatted.format(total=amt_saved), '\n\n')

dollars = formatted.format(total=amt_saved)
print(f"Total at retirement: {dollars}")

calc_interest = round(amt_saved * monthly_interest / 12)
monthly_income = formatted.format(total=calc_interest)
print(f"Monthly income: {monthly_income}")
