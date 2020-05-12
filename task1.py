  GNU nano 4.9.2                                 task1.py

import string

book= open("book.txt")
book1= book.read()
new_book= book1.split()
print(new_book)

new_list= []
for word in new_book:
  word1= word.strip(string.punctuation+string.whitespace)
  word2= word1.lower()
  new_list.append(word2)
print(new_list)

