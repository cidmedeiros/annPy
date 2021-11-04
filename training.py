def singleTrain(inputs, p, target):
    """
    inputs: [] -> data with only the dimensions to be passed on to the perceptron;
    p: Perceptron object -> perceptron to have its weights updated;
    target: any -> value to compare and calculate error;
    returns: Perceptron object -> the updated perceptron.
    """
    p.train(inputs, target)
    return p

def roundTrain(df,p,target='clf'):
    """
    df: pandas data frame -> data with only the dimensions including the bias is applied to be passed on to the perceptron;
    p: Perceptron object -> perceptron to have its weights updated;
    columns: [] -> the names of the columns for training
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


