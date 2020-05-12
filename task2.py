import string

import string

book= open("book.txt")
book1= book.read()
new_book= book1.split() # splitting the lines into words based on whitespace

new_list= dict()
count=0
for word in new_book:
  word1= word.strip(string.punctuation+string.whitespace) # remove punctuations and whitepsace from words
  new_word= word1.lower() # convert words into lowercase letters
  new_list[new_word]= new_list.get(new_word,0)+1

for value in new_list.values(): # counting no.of words 
  if value==1:
    count= count+1
print("The total number of words in the book", sum(new_list.values()))
print("The number of times each word is used", new_list)
print(" The number of different words used in the book", count)

lst=[]
for key, value in new_list.items(): # counting no. of common words
  lst.append((value,key))
lst.sort(reverse=True)
print(lst)
for freq, word in lst[:20]:
  print("The most common word:", word, freq, sep='\t') 
