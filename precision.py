from estimate_price import get_training_data
from ft_linear_regression import get_data
from ft_linear_regression import model
import json
import numpy as np

def mean_absolute_error(y, prediction):
    """Calculate the mean absolute error between predictions and true values.
    """
    return np.mean(np.abs(prediction - y))

def coefficient_determination(y, prediction):
    """Evaluate the performance of the linear regression model
    """
    u = ((y - prediction)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

def main():
    """Main program :
    - Retrieve data from a csv file
    - Retrieve theta values from a JSON file
    - Calculate the coefficient of determination
    - Calculate the mean absolute error
    - Return the result
    """
    try:
        theta, _, _ = get_training_data("./utils/training.json")
        _, y, x_bias, _, _ = get_data("./utils/data.csv")
        theta = np.array(theta)
        theta = theta.reshape(theta.shape[0], 1)
    except Exception as error:
        print(Exception.__name__ + ":", error)
        return 1
    
    prediction = model(x_bias, theta)
    coef_determination = coefficient_determination(y, prediction)
    mae = mean_absolute_error(y, prediction)        
    
    print(f"The coeffiction of determination is {coef_determination}")
    print(f"The mean absolute error (MAE) is {mae}")

if __name__ == "__main__":
    main()