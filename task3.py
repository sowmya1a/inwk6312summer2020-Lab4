import string
import matplotlib.pyplot as plt

book= open("book.txt")
book1= book.read()
new_book= book1.split() # splitting the lines into words based on whitespace

new_list= dict()
count=0
for word in new_book:
  word1= word.strip(string.punctuation+string.whitespace) # remove punctuations and whitepsace from words
  new_word= word1.lower() # convert words into lowercase letters
  new_list[new_word]= new_list.get(new_word,0)+1

lst=[]
for key, value in new_list.items(): # counting no. of common words
  lst.append((value,key))
lst.sort(reverse=True)
print(lst)
rank= []
count= 1
for tup in lst:
  for value in tup:
    if isinstance(value,int):
      rank.append(value)
rank2= {}
for item in rank:
  rank2[count]= item
  count= count+1
print(rank2)

lst1=[]
for var in rank2.items():
  lst1.append(var)

lst2=[]
for val in rank2.values():
  lst2.append(val)


plt.clf()
plt.xscale('log')
plt.yscale('log')
plt.title('Graph')
plt.xlabel('Logf')
plt.ylabel('Logr')
plt.plot(lst2, lst1)
plt.show()
