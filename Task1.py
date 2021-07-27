n = int(input("Number of words: "))
my_dict = {}

for i in range(n):
    temp = input("Enter the word: ")
    if temp in my_dict.keys():
        my_dict[temp]+=1
    else:
        my_dict[temp]=1

l = len(my_dict)
print(l)
for i in my_dict.keys():
    print(my_dict[i], end=" ")
print(" ")
sorted_dict = dict(sorted(my_dict.items(), key= lambda item: item[1]))

count=0
least_occured=" "
most_occured=" "

for i in sorted_dict.keys():
    print(i, end=" ")
    print("occured", end=" ")
    print(sorted_dict[i])
    if count==0:
        least_occured = i
    if count==(l-1):
        most_occured = i
    count+=1

print("The most occured word is", end=" ")
print(most_occured)

print("The least occured word is", end=" ")
print(least_occured)