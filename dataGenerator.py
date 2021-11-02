import numpy as np
import pandas as pd

def createData(min,max,n,d,bias=False):
    """
    n: int -> number of desired data points;
    d: int -> number of desired dimensions;
    bias: int, float -> value for bias
    """
    data = np.random.randint(min, max,size=(n,d))
    columns = [f'd{dm}' for dm in range(1,d+1)]

    if bias:
        data = pd.DataFrame(data, columns=columns)
        data['bias'] = bias
        return data
    else:
        return pd.DataFrame(data, columns=columns)
