import matplotlib.pyplot as plt
import numpy as np

##################### ERROR CALCULATION ###############################
def error(x,y,theta0,theta1):
    sum = 0
    for i in range(len(x)):
        sum += ((theta0 + theta1*x[i]) - y[i])**2
        print(sum)
        
    print(len(x))
    print("Error : ", (2/(float)(len(x)))*(sum))

################### GRADIENT DESCENT #################################
def gradient_descent(m,c,lr,x,y):
    
    Temp_m = 0
    Temp_c = 0
    N = (float)(len(x))

    for i in range(len(x)):

        Temp_c += -(2/N)*(y[i] - (m*x[i] + c))
        Temp_m += -(2/N)*x[i]*(y[i] - (m*x[i] + c))

    new_m = m - lr*Temp_m
    new_c = c - lr*Temp_c

    return [new_c,new_m]
    


################### SETTING OF THETA0 AND THETA1 ######################
def gradient_start(theta0,theta1,x,y,learning_rate,itr):
    m = theta1
    c = theta0
    lr = learning_rate

    for i in range(itr):
        c,m = gradient_descent(m,c,lr,x,y)

    return [m , c]


def run():
    #DATA INPUTS
    x = [1,2,3,4,5,6,7]
    y = [2,4,6,8,10,12,14]

    #INITIALIZE THE PARAMETERS
    theta0 = 0
    theta1 = 0

    #CALCULATE THE ERROR
    error(x,y,theta0,theta1)

    #LEARNING RATE
    learning_rate = 0.001

    #ITERATIONS
    itr = 1000

    #SET VALUE OF THETA0 AND THETA1
    m,c = gradient_start(theta0,theta1,x,y,learning_rate,itr)

    print("ANSWER ",m," ",c)

    xi = []
    yi = []
    
    yes = input("Enter y or n:")
    while (yes == 'y'):
        x_temp = input("Enter x value :")
        y_temp = m*(float)(x_temp) + c
        yes = input("Do you wanna continue : ")
        x.append((float)(x_temp))
        y.append(y_temp)
    print("BREAK")

    print(x)
    #    PLOTTING THE GRAPH     #
    y_reg = [(((float)(m)*(float)(i)) + c) for i in x]
    
    plt.scatter(x,y,color="red")
    plt.plot(x,y_reg)
    plt.show()

if __name__ == '__main__':
    run()
