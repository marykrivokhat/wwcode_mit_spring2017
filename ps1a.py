#введем ЗП за год:
annual_salary = float(int(input('Enter your annual salary: ')))

#введем % от ЗП, который откладываем:
portion_saved = float(str(input('Enter the percent of your salary to save, as a decimal: ')))

#введем стоимость дома:
total_cost = float(int(input('Enter the cost of your dream home: ')))

portion_down_payment = total_cost*0.25
current_savings = 0
months = 0
while current_savings < portion_down_payment:
    current_savings += annual_salary*portion_saved/12 + current_savings*0.04/12
    months += 1
print('Number of months: ' + str(months))