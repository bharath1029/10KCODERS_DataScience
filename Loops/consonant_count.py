str = "apple"
consonant_count = 0
for char in str.lower() :
  if char not in "aeiou" :
    consonant_count+=1

print(consonant_count)