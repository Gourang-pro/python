#python programing for gross salary

basic_salary=eval(input('enter the basic salary : '))

dearness = 0.4*basic_salary
house_rent = 0.2*basic_salary

gross_salary=basic_salary+dearness+house_rent

print('ramesh gross salary is :',gross_salary)
