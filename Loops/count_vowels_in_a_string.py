str = "apple"
vowel_count = 0
for char in str.lower() :
  if char in "aeiou" :
    vowel_count+=1

print(vowel_count)