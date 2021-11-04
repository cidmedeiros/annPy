"""
The Perceptron Algorithm:
    1 - For every input, multply that input by its weight;
    2 - Sum all of the weighted inputs;
    3 - Compute the output of the perceptron based on that sum passed through an activation function (the sign function)
"""
import random
#The Activation Function
def sign(pred):
    """
    pred: int -> Generally 1 or -1 classifying the prediction.

    returns: int -> the classification defined by the defined rule and the sum generated by the perceptron weights.
    """
    try:
        if pred > 0:
            return 1
        else:
            return -1
    except ValueError:
        print('Input is not a number')

#PERCEPTRON
class Perceptron:
    """
    n: int -> number of dimensions including the bias if applied;
    lr: float -> learning rate.

    Perceptron object with all its data and methods for training and predicting.
    """

    def __init__(self, n, lr):
        self.n = n
        self.lr = lr
        self.weights = [] #the n dimension weights plus 1 for the bias parameter
        #Initialize the weights randomly
        self.predictions = []
        for i in range(0, n):
            self.weights.append(random.random())
    
    #METHOD TO TRAIN THE PERCEPTRON
    #Training simply means updating the weights accordingly
    #to the error coming from the predictions made on the
    #training data
    def train(self,inputs,target):
        """
        inputs: [] -> array with the data associated with each data point;
        target: int -> Generally 1 or -1 classifying the prediction.

        returns: None -> It updates the objects's weights.
        """
        for i in range(0, len(self.weights)):
            #if error = 0, weight doesn't get updated
            #the weights and the respective dimension is linked by the indices in both arrays
            guess = self.guess(inputs)
            #possible errors -> -1-(-1) = 0; -1-(1) = -2; 1-(-1) = 2; 1-(1) = 0 
            error = target - guess
            #Tune all the weights Gradient Descent style
            currentWeight = self.weights[i]
            self.weights[i] = currentWeight + (error*inputs[i]*self.lr)
    
    def guess(self,inputs):
        """
         inputs: [] -> array with the data associated with each data point. 
         return: int -> the value returned by the activation function.
        """
        sum = 0
        for i in range(0,len(self.weights)):
            currentSum = sum
            sum = currentSum + inputs[i]*self.weights[i]
        
        return sign(sum)
    
    def predict(self, df):
        """
        df: pandas data frame -> data with only the dimensions including the bias if applied;
        """
        columns = [col for col in df.columns]
        pred = []

        for index, row in df.iterrows():
            inputs = []
            for col in columns:
                inputs.append(row[col])
            prediction = self.guess(inputs)
            pred.append(prediction)
        
        self.predictions = pred

    #Get the weights
    def getWeights(self):
        """
        return: [] -> current weights for the perceptron.
        """
        return self.weights
    #Set Learning rate
    def setWeights(self, newWeights):
        """
        newWeights: [] -> array with the new weight values in the same ordered as the targeted dimensions.
        return: None
        """
        self.weights = newWeights
    #Get the weights
    def getLr(self):
        """
        return: float -> current learning rate for the perceptron.
        """
        return self.lr
    #Set Learning rate
    def setLr(self,lRate):
        """
        lRate: float -> new learning rate value.
        return: None
        """
        self.lr = lRate
    
    def getPredictions(self):
        """
        return: [] -> array containing the latest predictions made
        """
        return self.predictions
    
    def __str__(self):
        return f'Perceptron Object -> Weights:({self.weights}, Learning Rate: {self.lr})'
