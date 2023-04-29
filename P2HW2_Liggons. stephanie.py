 #CTI-110
#P2HW2 - LIST
#STEPHANIE LIGGONS
#MARCH 25 2023
#
#Get grades from each module from user
#Program calculates lowest grade, highest grade, sum of total grades, and grade average
#Presents lowest grade, highest grade, sum of grades, and average with 2 decimaLs
#
Mod_1 = float(input('Enter grade for Module 1:'))
Mod_2 = float(input('Enter grade for Module 2:'))
Mod_3 = float(input('Enter grade for Module 3:'))
Mod_4 = float(input('Enter grade for Module 4:'))
Mod_5 = float(input('Enter grade for Module 5:'))
Mod_6 = float(input('Enter grade for Module 6:'))

Module_Grades = [Mod_1, Mod_2, Mod_3, Mod_4, Mod_5, Mod_6]
Lowest_Grade = min(Module_Grades)
Highest_Grade = max(Module_Grades)
Grade_Total = sum(Module_Grades)
Grade_Average = sum(Module_Grades) / 6
print()
print('------------Results------------')
print(f'Lowest Grade:      {Lowest_Grade:.2f}')
print(f'Highest Grade:     {Highest_Grade:.2f}')
print(f'Sum of Grades:     {Grade_Total:.2f}')
print(f'Average:           {Grade_Average:.2f}')
print('----------------------------------------')
