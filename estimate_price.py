import sys
import json




def get_training_data(file_name: str) -> any:
    """Retrieve theta parameters and standardization values (mean, std) from a JSON file."""
    json_file = open(file_name, "r")
    data = json.load(json_file)
    json_file.close()
    
    if "theta0" not in data or "theta1" not in data:
        raise ValueError("Invalid json: missing thetas")
    if "mean" not in data or "std" not in data:
        raise ValueError("Invalid json: missing standarlization values") 
    
    theta0 = float(data["theta0"])
    theta1 = float(data["theta1"])
    mean = float(data["mean"])
    std = float(data["std"])
    return (theta0, theta1), mean, std

      
def estimate_price(mileage: float, theta: tuple) -> float:
    """Estimate price using a linear model"""
    return theta[0] + (theta[1] * mileage)


def main():
    """Main program :
    - Ask the user a mileage
    - Retrieve trained paramenters from a json file
    - Estimate price from prompted mileage
    """
    while(True):
        user_input = input("Please provide a mileage : ")
        try:
            mileage = float(user_input)
            if mileage < 0:
                raise ValueError
            break
        except ValueError:
            print("Incorrect input. Please provide a valid input (positive float).")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
    
    try:  
        theta, mean, std = get_training_data("./utils/training.json")
    except FileNotFoundError:
        print(FileNotFoundError.__name__ + ':', "Can´t access training.json file. Does it exist in ./utils repository ?")
        return 1
    except PermissionError:
        print(PermissionError.__name__ + ':', "No permission to access training.json file.")
        return 1
    except Exception as error:
        print(Exception.__name__ + ":", error)

    norm_mileage = (mileage - mean) / std
    result = estimate_price(norm_mileage, theta)
    
    print(f"Your price is estimated at : ${max(0, int(result))}$")


if __name__ == '__main__' :
	main()