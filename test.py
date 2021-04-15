ball = input("Enter String: ")

count = 0
wordCount = 0

for i in ball:
    count = count + 1
    if(i == ''):
       wordCount = wordCount + 1

print ("Number of Words in the String")
print (wordCount)

print ("Number of Charactors in the String including Space")
print (count)