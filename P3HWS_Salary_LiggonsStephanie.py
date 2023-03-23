#CTI-110
#P3HW2-Salary
#Stephanie Liggons
#
overTime = 0
overTimeP = 0
regHourPay = 0
grossPay = 0

employeeName = input("Enter employee's name:")
#Enter employees name:John Smith
hourWorked = float(input("Enter number of hours worked:"))
#Enter number of hours worked:45
payRate = float(input("Enter employee's pay rate:"))
#Enter employees pay rate:17.5
print("--------------------------------------------")



print("Employee name:\t", employeeName)
      
#Employee name:	 John Smith
print("\n")
  


if hourWorked > 40:
    overTime = hourWorked - 40
    overTimePay = overTime * 1.5 * payRate
    regHourPay = 40 * payRate
    grossPay = regHourPay + overTimePay
else:
    regHourPay = hourWorked * payRate
    grossPay = regHourPay
print(grossPay)
