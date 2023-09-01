x = [12,34,1,78,3,6,7,8,9,15,13,14]
print(len(x))
x.append(300)
x.pop()
# x.sort(reverse=False)
x.insert(9,2000)
y = x.copy()
x.remove(2000)
y.clear()
print(y)
print(x.index(3))
print(x)
sum = 0
average = 0.0

for i in range(len(x)):
    sum += x[i]

# for i in range(len(x)):
#     largest = x[i]
#     ni = i+1
#     if x[ni] > largest:
#         largest = x[i+1]
#         print("The maximun of them all is: " ,largest)
        

# print("The maximun of them all is: " ,largest)
average = (sum/len(x))

print(x[:9])
print(x[-1])
print("The Sum of the numbers is : ", sum)
print("The Average of the numbers is : ", average)
print(i)


