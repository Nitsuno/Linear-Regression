import BiLR as BiLR
import matplotlib.pyplot as plt
from numpy import *

if __name__ == '__main__':
    b, m, points = BiLR.run()

    #Plots original data points
    x_points = points[:, 0]
    y_points = points[:, 1]
    plt.scatter(x_points, y_points, color='black', label='Data Points')

    #Plots the regression line
    x_values = array([min(x_points), max(x_points)])
    y_values = b + m * x_values
    plt.plot(x_values, y_values, color='red', label='Regression Line')

    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Linear Regression Model')
    plt.legend()
    plt.show()