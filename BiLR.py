from numpy import *

#error calculated as difference of y of point and y of gradient at x
def compute_error(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) **2
   
    return totalError / float(len(points))

def gradient_descent(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
   
    return [b, m]

def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        
        #compute partial derivatives for error function (direction with respect to b and m)
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
   
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]

def run():
    #Step 1 - collect data
    points = genfromtxt('.\dataLib\data.csv', delimiter=',')

    #Step 2 - define our hyperparameters
    #how fast the model should converge
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    num_iterations = 10000

    #Step 3 - train our model
    print('starting gradient descent at b = {0}, m = {1}, error = {2}'.format(initial_b, initial_m, compute_error(initial_b, initial_m, points)))
    [b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, num_iterations)
    print('ending point at b = {1}, m = {2}, error = {3}'.format(num_iterations, b, m, compute_error(b, m, points)))

    return b, m, points

if __name__ == '__main__':
    run()