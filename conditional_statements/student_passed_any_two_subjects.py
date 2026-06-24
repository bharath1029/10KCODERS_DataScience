maths = int(input("Maths :"))
physics = int(input("Physics :"))
chemistry = int(input("Chemistry :"))
passed_subjects = 0

if maths >= 35 :
  passed_subjects += 1
if physics >= 35 :
  passed_subjects += 1
if chemistry >= 35 :
  passed_subjects += 1

if passed_subjects >=2 :
  print("student passed two subjects")
else :
  print("student failed")