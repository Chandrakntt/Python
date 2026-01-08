# Conditionals 

age = int(input("Enter Your Age: "))

if age < 18:
    print("Minor")
elif age >= 65:
    print("Senior")
else:
    print("Adult")



# Loops 

# for loop
for i in range(5):              # 0 to 4
    print(i)

fruits = ["Apple","Banana","Orange","Mango","Pineapple"]

for fruit in fruits:            # Iterate list
    print(fruit)


# while loop
for i in range(10):
    if i == 3:
        continue                # skip iteration
    if i == 7:
        break                   # Exit loop
    print(i)

