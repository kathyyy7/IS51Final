"""""

STRUCTURED ENGLISH

Class Grade Program

To display the number of grades, average and percentage of grades above the average
in the final exam 
Create a lsit that stores 24 numbers (float) from the text file - final.txt
Capture user's input 24 times for their grades
Append the number/grade to the list

Then define a function that calculate the number of grades
Which will calculate that average which takes the total/number of grades
We convert the output of the percentage of grades that are above the average to a percentage

Finally the output calculated value to the user

end of program

"""""

"""""

PSEUDO CODE

import final.txt
main():
    infile = open ("final.txt)
    num_grades =formListofGrades
    avg_grade = createAverageGrade (num_grades)
    calculate_percent_above_average = createPercentAboveAverage

def create_dictionary ("final.txt")
read in final.txt
create lsit = each line from the text file
close file 
create dict off of the list 


"""""

infile = open("final.txt")
grades = [line.rstrip() for line in infile]
infile.close()
for i in range (len(grades)):
    grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0 
for grade in grades:
    if grade > average:
        num += 1
print("Number of grades: ", len(grades))
print("Average grade: ", average)
print("Percentage of grades above average: {0:.2f}%".format(100*num / len(grades)))
