import sys
import json

def estimate_price(mileage: float, theta: tuple) -> float:
    return theta[0] + (theta[1] * mileage)

def get_theta(file_name: str) -> tuple:
    json_file = open(file_name, "r")
    theta = json.load(json_file)
    json_file.close()
    
    if "theta0" not in theta or "theta1" not in theta:
        raise ValueError("Invalid json: missing keys")
    
    theta0 = float(theta["theta0"])
    theta1 = float(theta["theta1"])
    return (theta0, theta1)
        

def main():
    while(1):
        user_input = input("Please provide a mileage : ")
        try:
            mileage = float(user_input)
        except:
            print("Incorrect input. Please provide a valid input (float).")
            continue
        break
    
    try:
        theta = get_theta("../utils/theta.json")
        result = estimate_price(mileage, theta)
        print("Your price is estimated at :", result)
        sys.exit(0)
    except FileNotFoundError:
        print(FileNotFoundError.__name__ + ':', "Can´t access theta.json file. Does it exist in ./utils repository ?")
    except PermissionError:
        print(PermissionError.__name__ + ':', "No permission to access theta.json file.")
    except Exception as error:
        print(Exception.__name__ + ":", error)
    sys.exit(1)
        
if __name__ == '__main__' :
	main()