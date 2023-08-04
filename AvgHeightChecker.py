student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


#Calculate avg without sum() & len() function
print(student_heights)
total_height = 0
total_students = 0

for height in student_heights:
  total_height += height
  total_students +=1

avg_height = total_height / total_students

print(round(avg_height))



  

