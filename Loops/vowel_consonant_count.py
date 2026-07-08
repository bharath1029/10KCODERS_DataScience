str = "apple"
vowel_count = 0
consonant_count = 0
for char in str.lower() :
  if char in "aeiou" :
    vowel_count += 1
  else : 
    consonant_count += 1

print(f"vowel_count : {vowel_count} consonant_count : {consonant_count}")