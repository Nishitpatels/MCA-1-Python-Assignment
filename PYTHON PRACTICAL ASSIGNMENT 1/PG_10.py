# -----------------------------------------------------------

str = "Python123"

print("Reversed: ",str[::-1])

str1 = "Emma is a data scientist who knows Python."
bit = str1.split(" ")

for i in bit:
    print(i)


# -----------------------------------------------------------

# Create a string made of the first, middle and last character - slicing

str1 = "James"
print(str1[::2])

# Create a string made of the middle three characters
str2 = "JhonDipPeta"
print(str2[4:7])

str3 = "JaSonAy"
print(str3[2:5])

# -----------------------------------------------------------

# Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
s3 = s1+s2
print(s3)

# -----------------------------------------------------------

str4 = "PYnAtivE"

lower = []
upper = []

for i in str4:
    if(i.islower()):
        lower.append(i)
    else:
        upper.append(i)

joined = ''.join(lower + upper)
print(joined)

# -----------------------------------------------------------

input_str = "PYnative29@#8496"

total = 0
flag = 0

for i in input_str:
    if(i.isdigit()):
        flag = flag + 1
        total = total + int(i)

avg = total / flag
print(avg)

# -----------------------------------------------------------