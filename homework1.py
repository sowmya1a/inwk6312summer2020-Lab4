import string

book= open ("book.txt")
book1= book.read()
book2= book1.replace("-"," ")
new_book= book2.split()
new_book_list= []
for word in new_book:
  word1= word.strip(string.punctuation+string.whitespace)
  word2= word1.lower()
  new_book_list.append(word2)
print(new_book_list)

word_list= open("words.txt")
new_word_list=[]
for char in word_list:
  char= char.strip()
  new_word_list.append(char)
print(new_word_list)

def subtraction(l1, l2):
  temp=[]
  for item in l1:
    if item not in l2:
      temp.append(item)
  print(temp)
  print(len(temp))

subtraction(new_book_list, new_word_list )
