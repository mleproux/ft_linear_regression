import numpy as np
import matplotlib.pyplot as plt
import sys
import json


def get_data(file_name: str):
    """Retrieve data from a csv file.
    """
    data = np.genfromtxt(file_name, delimiter=",", skip_header=1)
    x = data[:,0]
    y = data[:,1]
    
    
    x = x.reshape(x.shape[0], 1)
    y = y.reshape(y.shape[0], 1)
    
    mean = np.mean(x)
    std = np.std(x)
    
    x = (x - np.mean(x)) / np.std(x)
    x_bias = np.hstack((np.ones((x.shape[0], 1)), x))
    
    return x, y, x_bias, mean, std

def save_training_data(theta, mean, std):
    """Save the training data in a JSON file.
    """
    data = {
        "theta0": float(theta[0, 0]),
        "theta1": float(theta[1, 0]),
        "mean": float(mean),
        "std": float(std)
    }

    with open("./utils/training.json", "w") as f:
        json.dump(data, f, indent=4)


def model(x, theta):
    """Compute linear prediction
    """
    return x.dot(theta)


def cost_function(x, y, theta):
    """Mean squared error cost for linear regression.
    """
    m = len(y)
    return 1/(2*m) * np.sum((model(x, theta) - y)**2)


def gradient_descent(x, y, theta, learning_rate, n_iterations):
    """Run gradient descent to minimize the mean squared error cost.
    Returns the optimized theta and the cost history over all iterations.
    """
    print(x)
    m = len(y)
    cost_history = np.zeros(n_iterations)
    
    for i in range(0, n_iterations):
        theta = theta - learning_rate * 1/m * x.T.dot(model(x, theta) - y)
        cost_history[i] = cost_function(x, y, theta)
    return theta, cost_history


def main():
    """Main program :
    - Retrieve data from a csv file
    - perform a gradient descent algorith to get the best theta values
    - Save theta and standardization values in a JSON file
    - Prompt the user if they want to see a graph of the linear regression result
    """
    try:
        x, y, x_bias, mean, std = get_data("./utils/data.csv")
    except FileNotFoundError:
        print(FileNotFoundError.__name__ + ':', "Can´t access data.csv file. Does it exist in ./utils repository ?")
        return 1
    except Exception as error:
        print(Exception.__name__ + ":", error)
        return 1
    
    try:
        theta = np.random.randn(2, 1)
        n_iterations = 1000
        learning_rate = 0.07
        new_theta, cost_history = gradient_descent(x_bias, y, theta, learning_rate, n_iterations)
        
        save_training_data(new_theta, mean, std)
        print("theta and standardization values has been saved in ./utils/training.json.")
        
        while(True):
            user_input = input("Pick a graph to show: (1: Linear regression result, 2: Cost history, 3: Exit)\n")
            try:
                choice = int(user_input)
                if choice < 1 or choice > 3:
                    raise ValueError
                break
            except ValueError:
                print("Incorrect input. Please provide a valid input (1-3).")
        
        if choice == 3:
            return 0
        if choice == 1:
            plt.scatter(x, y)
            plt.plot(x, model(x_bias, new_theta), c='r')
        if choice == 2:
            plt.plot(range(n_iterations), cost_history)  
        plt.show()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as error:
        print(Exception.__name__ + ":", error)
        

if __name__ == '__main__' :
	main()