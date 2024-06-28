import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
import pandas as pd

df = pd.read_csv('Real estate.csv')

def findMin(xdf):
    min_value = xdf.iloc[0]
    min_index = 0
    
    # Iterate over index and value using .items()
    for index, row in xdf.items():
        if row < min_value:
            min_value = row
            min_index = index
    
    return min_index, min_value

def findMax(xdf):
    max_value = xdf.iloc[0]
    max_index = 0
    
    # Iterate over index and value using .items()
    for index, row in xdf.items():
        if row > max_value:
            max_value = row
            max_index = index
    
    return max_index, max_value

def SS(m, b, xdf, ydf):
    SS = 0
    for x, y in zip(xdf, ydf):
        yhat = (m * x + b)
        SS += (y - yhat)**2
    return SS

# initially start with any line
# adjust slope by 1
    # if SS is smaller then make the line this
    # else look in the other direction
# stop until next steps are both larger


# draw an inital line

index, min = findMin(df['X2 house age'])
x1 = min
index, min = findMin(df['Y house price of unit area'])
y1 = min
index, max = findMax(df['X2 house age'])
x2 = max
index, max = findMax(df['Y house price of unit area'])
y2 = max

m = (y2 - y1) / (x2 - x1)
b = y2 - m * x2
x_values = df['X2 house age']
y_values = m * x_values + b

# calculate SS

min_sum = SS(m, b, df['X2 house age'], df['Y house price of unit area'])

# itarate

while 1:
    up = m+1
    bUp = y2 - up * x2
    down = m-1
    sumUP = SS(up, b, df['X2 house age'], df['Y house price of unit area'])








plt.scatter(df['X2 house age'], df['Y house price of unit area'])
plt.plot(x_values, y_values, color='black', label='Fitted Line')  # Plot the line
plt.scatter(x1, y1, color="red")
plt.scatter(x2, y2, color="red")

plt.xlabel('House Age')
plt.ylabel('Price')
plt.show()

