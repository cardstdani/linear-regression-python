import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Data load
data = pd.read_csv('My_Data.csv')
x = (data.iloc[0:, 0].values)
y = (data.iloc[0:, 1].values)
xTrain = np.array(x[:]).reshape((-1, 1))
yTrain = np.array(y[:]).reshape((-1, 1))

# Linear Regression
regression = LinearRegression()
regression.fit(xTrain, yTrain)

# Error values and average error
yErrorValue = []  # Error values on the graph
yErrorValue2 = []  # Error values on the graph
errors = []  # Real error values
maxError = 0
minError = 10 ** 6
averageError = 0
for i in range(len(xTrain)):
    error = regression.predict(xTrain)[i] - yTrain[i]  # Get error value
    yErrorValue.append(regression.predict(xTrain)[i] + abs(error))  # Get error value for the graph
    yErrorValue2.append(regression.predict(xTrain)[i] - abs(error))  # Get error value for the underline error
    if (error > maxError):  # Get max error value
        maxError = error
    if (error < minError):  # Get min error value
        minError = error
    errors.append(error)
    averageError += abs(error)  # Sum error to average
    plt.plot([xTrain[i], xTrain[i]], [regression.predict(xTrain)[i], regression.predict(xTrain)[i] - error], marker=',',
             color='#3F3BFA', linewidth=1)  # Draw error line
averageError /= len(xTrain)  # Get average error value

# Plot settings
plt.scatter(xTrain, yTrain, marker='+', color='#3F3BFA')  # Real data values
lines = plt.plot(xTrain, regression.predict(xTrain), marker='.', color='r', linewidth=2)  # Regression line
lines += plt.plot(xTrain, yErrorValue, marker=',', color='y', linewidth=1)  # Upper line error value
lines += plt.plot(xTrain, yErrorValue2, marker=',', color='g', linewidth=1)  # Lower line error value
plt.grid(color='#1f1f1f', linestyle='dashed', linewidth=0.3)
plt.gca().set_facecolor('#ffffff')
plt.legend(lines, ["Regression/Predictions", "Upper error line", "Lower error line", "Real data points"])
plt.title('Linear regression', fontsize=15, fontname='Montserrat', weight="black", color='#3F3BFA')
plt.xlabel('X axis', fontsize=15, fontname='Montserrat', weight="black", color='#3F3BFA')
plt.ylabel('Y axis', fontsize=15, fontname='Montserrat', weight="black", color='#3F3BFA')
# plt.get_current_fig_manager().full_screen_toggle() #Shows the graph in fullscreen
plt.show()

print("Max error: " + str(maxError))
print("Min error: " + str(minError))
print("Average error: " + str(averageError))
