##Author:Aditya Jadhav
##Description: Tells you the number of months you need to save a percentage of money
##             so that you could pay for your dream house


annual_salary= int(input('Enter your starting annual salary: '))
saving_percent_of_salary=float(input('Enter the percent of your salary to save, as a decimal:'))
cost_of_dream_home=float(input('Enter the cost of your dream home:'))
semi_annual_raise=float(input('Enter the semi annual raise, as a decimal: '))
current_savings=0
interest_rate=0.04
i=0
while current_savings<cost_of_dream_home/4:
    if (i)%6==0 and i!=0:
        annual_salary+=annual_salary*semi_annual_raise
    current_savings+=((interest_rate/12)*current_savings)
    current_savings+=(saving_percent_of_salary*(annual_salary/12))
    i+=1
print('Number of months',i)
