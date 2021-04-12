import numpy as np 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 
import csv
import os
 

# see how the data looks (plot the histograms associated to input data - GDP feature,Freedom feature - and output data - happiness)
def plotDataHistogram(x, variableName):
    plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()




# learning step: init and train a linear regression model y = f(x) = w0 + w1 * x1+ w2*x2
# Prediction step: used the trained model to estimate the output for a new input

def training(trainInputs,trainOutputs):
    # training data preparation (the sklearn linear model requires as input training data as noSamples x noFeatures array;
    #  in the current case, the input must be a matrix of len(trainInputs) lineas and two columns (two  features are used in this problem))
    xx = [[el1,el2] for el1,el2 in zip(trainInputs[0],trainInputs[1])]
    # model initialisation
    regressor = linear_model.LinearRegression()
  


  # training the model by using the training inputs and known training outputs
    regressor.fit(xx, trainOutputs)
    # save the model parameters
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    print('the learnt model: f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')

    return w0,w1,w2

# load data and consider two features feature Economy and Freedom and the output to be estimated (happiness)

def loadData(fileName, inputVariabName1, inputVariabName2, outputVariabName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
  

    inputs=[[float(data[i][ dataNames.index(inputVariabName1)]) for i in range(len(data))], [float(data[i][dataNames.index(inputVariabName2)]) for i in range(len(data))] ]
    selectedOutput = dataNames.index(outputVariabName)
    outputs = [float(data[i][selectedOutput]) for i in range(len(data))]
    
    return inputs, outputs

#ALL STEPS TOGETHER

#load data

crtDir =  os.getcwd()
filePath = os.path.join(crtDir, 'data', '2017.csv')
inputs, outputs = loadData(filePath, 'Economy','Freedom', 'Happiness Score')
    
#show data, check the linearity

plotDataHistogram(inputs[0], 'Economy capital GDP')
plotDataHistogram(inputs[1], 'Freedom')
plotDataHistogram(outputs, 'Happiness score')

      # check the liniarity (to check that a linear relationship exists between the dependent variable (z= happiness) 
      # #and the independent variable (x = capitalEconomy , y= Freedom).)

ax = plt.axes(projection='3d')
ax.scatter3D(inputs[0], inputs[1], outputs, c=outputs, cmap='Oranges')
plt.title('GDP capital ECONOMY & Freedom vs. Happiness')
plt.xlabel('GDP capital ECONOMY')
plt.ylabel('Freedom')
ax.set_zlabel('Happiness')
plt.show()


#split the data in training data and validation data


#
np.random.seed(5)
indexes = [i for i in range(len(outputs))]
     
trainSample = np.random.choice(indexes, int(0.8 * len(outputs)), replace = False)
validationSample = [i for i in indexes  if not i in trainSample]



trainInputs = [ [inputs[0][i] for i in trainSample],[inputs[1][i] for i in trainSample]]

trainOutputs = [outputs[i] for i in trainSample]



validationInputs = [ [inputs[0][i] for i in validationSample], [inputs[1][i] for i in validationSample]]

validationOutputs = [outputs[i] for i in validationSample]



#
#plot the train and validation data

ax = plt.axes(projection='3d')
ax.scatter3D(trainInputs[0], trainInputs[1], trainOutputs, c=trainOutputs, cmap='Blues',label="Training data")
ax.scatter3D(validationInputs[0], validationInputs[1], validationOutputs, c=validationOutputs, cmap='Reds',label="Validation data")
plt.title('train and validation data')
plt.xlabel('GDP capital')
plt.ylabel('Freedom')
ax.set_zlabel('Happiness')
plt.legend()
plt.show()




#training step
    
w0,w1,w2 = training(trainInputs,trainOutputs)
    

    
#plot the learnt model

    # prepare some synthetic data (inputs are random, while the outputs are computed by the learnt model)

noOfPoints = 1000
xref = []
val = min(trainInputs[0]) #minimul de pe feature1
step = (max(trainInputs[0]) - min(trainInputs[0])) / noOfPoints
for i in range(1, noOfPoints):
    xref.append(val)
    val += step

yref = []
val = min(trainInputs[1])
step = (max(trainInputs[1]) - min(trainInputs[1])) / noOfPoints
for i in range(1, noOfPoints):
    yref.append(val)
    val += step


zref = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(xref,yref)]

ax = plt.axes(projection='3d')
ax.scatter3D(xref, yref, zref, c=zref, cmap='Blues',label="Learnt model")
ax.scatter3D(trainInputs[0], trainInputs[1], trainOutputs, c=trainOutputs, cmap='Oranges',label="Training data")
plt.title('train data and the learnt model')
plt.xlabel('Economy')
plt.ylabel('Freedom')
ax.set_zlabel('Happiness')
plt.legend()
plt.show()



# use the trained model to predict new inputs
# makes predictions for test data
    # computedTestOutputs = [w0 + w1 * el + w2*el2 for el in testInputs]
# makes predictions for test data (by tool)

computedValidationOutputs  = [w0 + w1 * el1 + w2 * el2 for el1,el2 in zip(validationInputs[0],validationInputs[1])]

            # plot the computed outputs (see how far they are from the real outputs)
ax = plt.axes(projection='3d')
ax.scatter3D(validationInputs[0], validationInputs[1], computedValidationOutputs, c=computedValidationOutputs, cmap='Blues',label="Computed")
ax.scatter3D(validationInputs[0], validationInputs[1], validationOutputs, c=validationOutputs, cmap='Oranges',label="Real test data")
plt.title('computed validation and real validation data')
plt.xlabel('GDP capital')
plt.ylabel('freedom')
ax.set_zlabel('happiness')
plt.legend()
plt.show()


#compute the differences between the predictions and real outputs
error = 0.0
for t1, t2 in zip(computedValidationOutputs, validationOutputs):
    error += (t1 - t2) ** 2
error = error / len(validationOutputs)
print("prediction error (manual): ", error)


#compute the differences between the predictions and real outputs
    
error = mean_squared_error(validationOutputs, computedValidationOutputs)
print('Prediction error (tool):  ', error)

