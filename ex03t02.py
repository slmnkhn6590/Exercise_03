n = int(input("Type a number to see it's  sum like (1+ 2 + ...n): "))
count = 0
Minimum = []
maximum = []
average = []
print("solving it using a count controlled loop")

for i in range(1, n+1):
    Minimum.append(i)
print(min(Minimum))

for i in range(1, n+1):
    maximum.append(i)
print(max(maximum))

print(n/len(str(n)))

for i in range(1,n+1 ):
    count += i
print(count) 

print("solving the problem using condition controlled loop")
count = 0
maxi = []
mini = []
average =[]


while n != 0:
    count +=n
    maxi.append(n)
    mini.append(n)
    n -= 1




print(min(mini))
print(max(maxi))
print(n/len(str(n)))
print(count)