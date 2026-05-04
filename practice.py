#Question 1 – Password Guessing Program [10 Marks]

secret_password = input("Enter the secret password: ")
attempts = 0
for i in range(10000):
  guess = f"{i:04d}"
  attempts += 1

  if guess == secret_password:
    print(f"Password found: {guess}")
    print(f"Number of attempts: {attempts}")
    break

# Question 2 – Prime Number Check [10 Marks]
def isPrime(n):
  if n <= 1:
    return False

  for i in range (2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True


n = int(input("Enter a number: "))
if isPrime(n):
  print(f"{n} is a prime number")
else:
  print(f"{n} is not a prime number")
  
# Question 3 – Largest Number in a List [10 Marks]
numbers = []

for i in range(5):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

m = numbers[0]

for n in numbers:
    if n > m:
        m = n

print(f"The largest number is: {m}")

# Question 4 – Find Pair with Target Sum [10 Marks]

numbers = [2,4,7,11,5]
target = 9

for i in range (len(numbers)):
  for j in range (i + 1, len(numbers)):
    if numbers[i] + numbers[j] == target:
      print(f"Pair found: {numbers[i]} + {numbers[j]} = {target}")
      
      
# Question 5 – Count Number Frequency [10 Marks]
numbers = [3, 5, 3, 7, 9, 5, 3]

frequency = {}

for num in numbers:
  if num in frequency:
    frequency[num]+=1
  else:
    frequency[num]=1

print(frequency)

# Question 6 – Word Search in Sentence [10 Marks]
text = "machine learning is interesting"
word = "learning"
index = text.find(word)
if index != -1:
  print(f"The word '{word}' starts at index {index}.")
else:
  print(f"The word '{word}' was not found in the text.")


# Question 7 – Grade Calculator [10 Marks]

marks = float(input("Enter the student's marks: "))

if 80 <= marks <= 100:
    grade = 'A+'
elif 70 <= marks < 80:
    grade = 'B'
elif 60 <= marks < 70:
    grade = 'C'
elif 50 <= marks < 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The student's grade is: {grade}")

# Question 8 – NumPy Random Numbers [10 Marks]
import numpy as np
random_numbers = (np.random.rand(10))
print("Random Numbers:", random_numbers)

mean_value = np.mean(random_numbers)
print("Mean:", mean_value)

max_value = np.max(random_numbers)
print("Maximum Value:", max_value)

min_value = np.min(random_numbers)
print("Minimum Value:", min_value)

# Question 9 – Student DataFrame Analysis [10 Marks]
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Marks': [85, 72, 90, 65, 78]
}
df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

average_marks = df['Marks'].mean()
print(f"\nAverage Marks: {average_marks:.2f}")

students_above_75 = df[df['Marks'] > 75]['Name']
print("\nStudents with marks greater than 75:")
print(students_above_75.to_list())

# Question 10 – Study Hours vs Marks Visualization [10 Marks]

import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5, 6]
marks = [50, 55, 60, 65, 70, 80]
plt.scatter(hours, marks, color='red', marker='*')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study Hours vs Marks')
plt.show()

# Question 11 – Linear Regression Prediction [15 Marks]
from sklearn.linear_model import LinearRegression

x = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()

model.fit(x, y)

predicted_value = model.predict([[6]])

intercept = model.intercept_
slope = model.coef_[0]

print(f"Predicted value when x = 6: {predicted_value[0]:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"Slope: {slope:.2f}")

# Question 12 – Regression Visualization [15 Marks]

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

plt.scatter(x, y, color='blue', label='Data points')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter plot of the data')

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.plot(x, y_pred, color='red', linewidth=2, label='Best-fit line')
plt.legend()
plt.show()

print(f"Intercept: {model.intercept_[0]:.2f}")
print(f"Slope: {model.coef_[0][0]:.2f}")