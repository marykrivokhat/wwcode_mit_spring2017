'''
РАЗОБРАЛАСЬ (ВЗЯЛА НОВЫЙ КОД), ТЕПЕРЬ ВСЕ СХОДИТСЯ:
'''
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) 
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
rate = 0.04
number_of_months = 0

while current_savings <= portion_down_payment:
    current_savings += annual_salary * portion_saved / 12
    current_savings += current_savings * rate / 12
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months: ", number_of_months)    





#'''
#МОЙ ПРЕДЫДУЩИЙ ВАРИАНТ, ГДЕ-ТО БЫЛА ОШИБКА
#'''
#'''
#ЗА ЕДИНИЦУ БЕРУ ПОЛГОДА
#'''
##введем ЗП за год:
#annual_salary = float(int(input('Enter your annual salary: ')))
#
##введем % от ЗП, который откладываем:
#portion_saved = float(str(input('Enter the percent of your salary to save, as a decimal: ')))
#
##введем стоимость дома:
#total_cost = float(int(input('Enter the cost of your dream home: ')))
#
##введем %, на который увеличивается ЗП:
#semi_annual_raise = float(str(input('Enter the semi­annual raise, as a decimal: ')))
#
#portion_down_payment = total_cost*0.25
#current_savings = 0
#half_of_year = 0
#
##Пока сбережения не превысят авансовый платеж, мы копим:
#while current_savings < portion_down_payment:
#    current_savings += annual_salary/2*(1+semi_annual_raise)*portion_saved + current_savings*0.04/2
#    half_of_year += 1 
#month = half_of_year/6
#print('Number of months: ' + str(half_of_year*6))
#
#'''
#ИТОГО у меня получается 180 месяцев, а должно быть 142, как в примере:
#
#    
#Enter your starting annual salary: 120000
#Enter the percent of your salary to save, as a decimal: .05
#Enter the cost of your dream home: 500000
#Enter the semi­annual raise, as a decimal: .03
#Number of months: 142 
#'''