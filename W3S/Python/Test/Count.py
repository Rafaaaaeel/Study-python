def count_vowels(txt):
  return sum(c in "aeiou" for c in txt)

print(count_vowels('Rafael')) 