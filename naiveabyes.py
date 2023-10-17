import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import nltk
nltk.download('punkt')
#X_train
#X_test
#y_train
#y_test

def model_Evaluate(model):
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred)) 
#Precision: ratio of true positives to the total number of predicted positives
#Recall: ratio of true positives to the total number of actual positives
#F1-Score: mean of precision and recall
#Support: number of occurrences of each class in the true labels (y_test).


#confuion matrix, TP,TN, FP, FN
cf_matrix = confusion_matrix(y_test, y_pred) 
#TP,TN, FP, FN in %%%% 
group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]


BNBmodel = BernoulliNB()
BNBmodel.fit(X_train, y_train) #train model using training data
model_Evaluate(BNBmodel)
y_pred1 = BNBmodel.predict(X_test) #predict on new data


#plot ROC CURVE
from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred1)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC CURVE')
plt.legend(loc="lower right")
plt.show()