heights = input("Input a list of heights ").split()
for n in range(0, len(heights)):
  heights[n] = int(heights[n])

#------------SOLUTION WITH SUM AND LEN FUNCTIONS------------
#total_height = sum(student_heights)
#number_of_students = len(student_heights)
#average_height = round(total_height / number_of_students)
#print(average_height)
#-----------------------------------------------------------

#                     BOTH WORKS WELL.

#------------------SOLUTION WITH FOR LOOPS------------------

total_height = 0 
for i in heights:
  total_height = total_height + i 
print(f"Total Height: {total_height}")
  
for x in heights:
  total_number = n+1

print(f"Total Number Input: {total_number}")

average_height = round(total_height / total_number)
print(f"Average Height: {average_height}")

#-----------------------------------------------------------
