import matplotlib.pyplot as plt
import seaborn as sns
import random as random

def hexColor():
    L = '0123456789ABCDEF'
    return '#'+ ''.join([random.choice(L) for i in range(6)][:])

def plot2d(data,width,height,legendSize='xx-small'):
    fig, ax = plt.subplots(1,1, figsize=(width,height))
    ax = sns.scatterplot(data=data[data.clf == 1], x='d1', y='d2', color = 'darkblue')
    ax = sns.scatterplot(data=data[data.clf == -1], x='d1', y= 'd2', color='darkgreen')
    ax = sns.lineplot(x=[0,100], y=[0,100], color='purple', legend=False)
    fig.suptitle('Linearly Separable Data', fontsize='large')
    fig.legend(['Boundary','Class 1','Class 2'], loc='center right', fontsize = legendSize, title='Classes')
    plt.show()

#def plotTraining(data,)