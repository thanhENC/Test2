# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  my_dictionary = {}
  for word in words:
    if word in my_dictionary:
      my_dictionary.extend({word:0})
    else:
      my_dictionary[word] += 1
  return my_dictionary
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}