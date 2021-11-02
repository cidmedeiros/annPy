import matplotlib.pyplot as plt
import seaborn as sns

def plot2d(data):
    fig, ax = plt.subplots(1,1, figsize=(18,6))
    ax1 = sns.scatterplot(data=data[data.clf == 1], x='d1', y='d2', color = 'darkblue')
    ax2 = sns.scatterplot(data=data[data.clf == 0], x='d1', y= 'd2', color='darkgreen')
    ax3 = sns.lineplot(x=[0,100], y=[0,100], color='purple', legend=False)
    fig.suptitle('Linearly Separable Data', fontsize='large')
    fig.legend(['Boundary','Class 1','Class 2'], loc='center right', fontsize = 'small', title='Classes')
    plt.show()