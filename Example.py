import pandas as pd
import numpy as np

data = pd.DataFrame([1, 5, 9, 15, 56])


# print(data.values)
# print(data[1:4])

def log(x):
    return np.log(x)


if __name__ == "__main__":
    print(data.applymap(log))
    print("_________________")
    print(data.applymap(lambda x: np.log(x)))
    print("_________________")
    print(np.log(data))
