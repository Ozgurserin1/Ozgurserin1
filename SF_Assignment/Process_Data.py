#---------------------------------------------------
#------Created  : 01/01/2025 - Khurram Asif
#------Modified : on 10/02/2025 by Ozgur Serin
#------Description : Software Foundation Module week 4 Python file handling tutorial 
#------Description : Computational Reasoning Module tutorials week 2 to 7 on excel
#----------------------------------------------------


#-----Define the Functions---------------
def calculate_average(scores):
    return sum(scores) / len(scores)
#-----Define the Grades using if elif commands--------
def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

#-----End Functions---------------

#-----Importing the csv files-----
import csv

#-----Executing the students.csv file list-----
students = []

#-----Reading the student.csv file-----
with open('Students.csv', 'r') as file:
        
        #-----Creating a csv reader object
        reader = csv.reader(file)

        #-----Read the header (first row)
        header = next(reader) 
        
        #-----Extracting field names through first row
        for row in reader:
            name, art, english, maths = row
            average = calculate_average([int(art), int(english), int(maths)])
            grade = assign_grade(average)
            students.append([name, art, english, maths, average, grade])

#-----Write the results to Student_Results.csv file and open the file
#-----Data gained from Students.csv to calculate the grades
with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Art', 'English', 'Maths', 'Average', 'Grade'])
        writer.writerows(students)

#-----Results are saved under the correct names and subject headings with students marks and grades
#-----Results saved and displayed in Students_Results.csv file
print('Results saved to student_results.csv')




