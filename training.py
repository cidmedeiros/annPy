import numpy as np
def singleTrain(inputs, p, target):
    """
    inputs: [] -> data with only the dimensions to be passed on to the perceptron;
    p: Perceptron object -> perceptron to have its weights updated;
    target: any -> value to compare and calculate error;

    returns: Perceptron object -> the updated perceptron.
    """
    p.train(inputs, target)
    return p

def trackTraining(df,p,target):
    """
    df: pandas data frame -> data with only the dimensions including the bias is applied to be passed on to the perceptron;
    p: Perceptron object -> perceptron to have its weights updated;
    target: any -> value to compare and calculate error.

    returns: pandas data frame -> new cols: 'pred'-> perceptron's prediction; 'signal': record wether pred is correct
    """
    dfCopy = df.copy()
    dfCopy['pred'] = p.getPredictions()
    dfCopy['signal'] = np.where(dfCopy[target] == dfCopy.pred,dfCopy[target],0)

    return dfCopy


def roundTrain(df,p,target='clf',track=True):
    """
    df: pandas data frame -> data with only the dimensions including the bias is applied to be passed on to the perceptron;
    p: Perceptron object -> perceptron to have its weights updated;
    columns: [] -> the names of the columns for training
    target: any -> value to compare and calculate error.

    returns: Perceptron object -> the updated perceptron
    """
    columns = [col for col in df.columns]

    for index, row in df.iterrows():
        inputs = []
        for col in columns:
            inputs.append(row[col])

        p = singleTrain(inputs, p, row[target])
    
    print(f'Perceptron after training -> ${p}')
    return p



