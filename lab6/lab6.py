from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


# version 1 - using the sklearn functions
def evalClassificationV1(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

    cm = confusion_matrix(realLabels, computedLabels, labels = labelNames)
    acc = accuracy_score(realLabels, computedLabels)
    precision = precision_score(realLabels, computedLabels, average = None, labels = labelNames)
    recall = recall_score(realLabels, computedLabels, average = None, labels = labelNames)
    return acc, precision, recall 
    
def desen(realOutputs,computedOutputs):
    indexes = [i for i in range(len(realOutputs))]
    real, = plt.plot(indexes, realOutputs, 'ro', label = 'real')
    computed, = plt.plot(indexes, computedOutputs, 'bo', label = 'computed')    
    plt.xlim(0,8)
    plt.ylim(0, 10)
    plt.legend([real, (real, computed)], ["Real", "Computed"])
    plt.show()


#represents the overall performance of classification model
#accuracy=corecctedpredicted/noofallsamples
def accuracy(realOutputs, computedOutputs):
    return sum([1 if realOutputs[i] == computedOutputs[i] else 0 for i in range(0, len(realOutputs))]) / len(
        realOutputs)

#evalClassificationV2
def evalClassification(realOutputs, computedOutputs, pos):
    TP = sum([1 if (realOutputs[i] == pos and computedOutputs[i] == pos) else 0 for i in range(len(realOutputs))])
    FP = sum([1 if (realOutputs[i] != pos and computedOutputs[i] == pos) else 0 for i in range(len(realOutputs))])
    TN = sum([1 if (realOutputs[i] != pos and computedOutputs[i] != pos) else 0 for i in range(len(realOutputs))])
    FN = sum([1 if (realOutputs[i] == pos and computedOutputs[i] != pos) else 0 for i in range(len(realOutputs))])


#precision indicates how accurate the positive predictions are:
##precizia indică cât de exacte sunt predicțiile pozitive:
#probabilitatea ca un exemplu clasificat pozitiv să fie relevant
# nr. de exemple pozitive corect clasificate / nr. total de exemple clasificate ca pozitive

    precision = TP / (TP + FP)
#recall indica acoperirea esantionului pozitiv real
#recall indicates the coverage of actual positive sample:
# Probabilitatea ca un exemplu pozitiv să fie identificat corect de către clasificator
#Probabilitatea ca un exemplu pozitiv să fie identificat corect de către clasificator
    recall = TP / (TP + FN)

    return precision, recall


def eval(realLabels, computedLabels, labels):
    precision = []
    recall = []
    for label in labels:
        pre, rec = evalClassification(realLabels, computedLabels, label)
        precision.append(pre)
        recall.append(rec)
    return precision, recall


#suma absoluta
def sumaAbsoluta(r1, c1):
    suma = 0
    for i in range(len(r1)):
                #realOutputs-computedOutputs
        suma += abs(r1[i] - c1[i])
    return suma


def sumaPatrat(r1, c1):
    suma = 0.0
    for i in range(len(r1)):
        #realOutputs-computedOutputs
        suma += (r1[i] - c1[i]) ** 2
    return suma


#compute de differences between the predictions and real outputs
#eroarea de predicție
def predictionError(realOutputs, computedOutputs):
                                            
    errorL1 = sum(sumaAbsoluta(r, c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)
  #  print('Error (the absolute difference) = Loss : ', errorL1)
    print('Error (the absolute difference) : ', errorL1)
    errorL2 = sqrt(sum(sumaPatrat(r, c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs))
    print('Error (the square difference): ', errorL2)

#de regresie
#multi-target
def problem1_regression():
    realOutputs = [[1, 2, 3,4,5],  [16, 17, 18,19,20], [5, 15, 75]]
    computedOutputs = [[1.5, 2, 2.8,3.5,4.5], [10.2, 19,15,14.0,19.0], [4.9, 15, 75]]
    print('Problema 1:')
    print('Prediction error:')
    predictionError(realOutputs, computedOutputs)
    print('')

 


#multiclass, clasificare
def problem2_clasificare():
    realLabels = ["mar", "para", "para", "strugure", "mar", "strugure"]
    labels = ["mar", "para", "strugure",]
    computedLabels =  ["mar", "para", "para", "strugure", "mar", "strugure"]
    precision, recall = eval(realLabels, computedLabels, labels)
    acc = accuracy(realLabels, computedLabels)
    print('Problema 2:')
    print("Accuracy: " + str(acc))
    print( " Precision: " + str(precision))
    print(" Recall: " + str(recall))
   # desen(realLabels,computedLabels)


#binara 
def problem_binara():
    labels = ["fruit", "non-fruit"]
    #echilibrata
    #realLabels = ["fruit", "non-fruit", "fruit", "non-fruit", "non-fruit", "fruit"]
   
    #echilibrata
    #computedLabels =  ["fruit", "non-fruit", "non-fruit", "non-fruit", "fruit", "fruit"]


   
    #neechilibrata
    realLabels = ["fruit", "fruit", "fruit", "non-fruit", "non-fruit", "fruit"]
    computedLabels = ["fruit", "fruit", "fruit", "fruit","non-fruit", "fruit",]

  
    precision, recall = eval(realLabels, computedLabels, labels)
    acc = accuracy(realLabels, computedLabels)
    print('Problema 3:')
    print("Accuracy: " + str(acc))
    print( " Precision: " + str(precision))
    print( " Recall: " + str(recall))

  
    #desen(realLabels,computedLabels)
  

#clasificare binara cu output de tip probabilitati
def problem4_probabilitati():
    from sklearn.metrics import log_loss
# we want ot estimate the error of prediction (classification)
# Problem specification:
# input: realLabels, computedOutputs - arrays of the same length containing labels (some discrete values) and real values, respectively
# output: accuracy, precision, recall - real values in range [0,1]


# if the rawOutputs of the ML algorithms are probabilities (not labels)
    realLabels =        ['spam', 'spam', 'ham', 'ham', 'spam', 'ham']
    computedOutputs = [ [0.3, 0.7], [0.4, 0.6], [0.9, 0.1], [0.85, 0.15], [0.7, 0.3], [0.4, 0.6]]
# computedLabels have to be  ['spam', 'ham', 'ham', 'spam', 'spam', 'ham']

# step1: transform the raw outputs into labels

# version 1 - native code
# computedLabels = []
# labelNames = list(set(realLabels))
# for p in computedOutputs:
#     probMaxPos = p.index(max(p))
#     label = labelNames[probMaxPos]
#     computedLabels.append(label)

# version 2 - by using NumPy library

    labelNames = list(set(realLabels))
    computedLabels = [labelNames[np.argmax(p)] for p in computedOutputs]
    # step2: compute the performance
    acc, prec, recall = evalClassificationV1(realLabels, computedLabels, ['spam', 'ham'])
    print('Problema 4:')
    print('acc: ', acc)
    print( ' precision: ', prec)
    print( ' recall: ', recall)

    #multi-label loss functions example
    print("cost:",log_loss(realLabels,computedOutputs) )


problem1_regression()
problem2_clasificare()
problem_binara()
problem4_probabilitati()
