import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import multilabel_confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report

data = np.genfromtxt('train.csv', delimiter=',')
data = np.delete(data,0,axis=0)
classe = data[:,-1]
data = np.delete(data,-1,axis=1)

data_treino,data_teste,classe_treino,classe_teste = train_test_split(data,classe,test_size=0.2,random_state=123)
classe_treino_onehot = to_categorical(classe_treino)

def create_model(numInputs, numClasses):
  model = Sequential()
  model.add(Dense(20,activation='elu',input_dim=numInputs))
  model.add(Dense(20,activation='elu'))
  model.add(Dense(20,activation='elu'))
  model.add(Dense(20,activation='elu'))
  model.add(Dense(20,activation='elu'))
  model.add(Dense(numClasses, activation='softmax'))
  model.compile('Adam', 'categorical_crossentropy', metrics=['categorical_accuracy'])
  return model

model = create_model(20,4)

history = model.fit(data_treino,classe_treino_onehot, validation_split=0.1, epochs=500, verbose=2)

plot_model(model,
          show_shapes=True,
          show_layer_names=False,
          rankdir="LR",
          dpi=80)

classe_predita_onehot = model.predict(data_teste)
classe_predita = classe_predita_onehot.argmax(axis=1)

matriz_confusao = confusion_matrix(classe_teste, classe_predita, labels=range(4))
print(matriz_confusao)

print('Precision or positive predictive: %.3f' % precision_score(classe_teste,classe_predita,average='weighted',zero_division=1))
print('Recall or Sensitivity: %.3f' % recall_score(classe_teste, classe_predita,average='weighted',zero_division=1))
print('Accuracy: %.3f' % accuracy_score(classe_teste, classe_predita))
print('F1 Score: %.3f' % f1_score(classe_teste, classe_predita,average='weighted',zero_division=1))
print('Precision Recall F1-Score Support for each class:')
#print(precision_recall_fscore_support(lista_classes_originais, lista_classes_preditas,average='weighted',labels=[0,1,2,3]))
precision, recall, fscore, support = precision_recall_fscore_support(classe_teste, classe_predita,
    zero_division=1)
print('precision or positive predictive: {}'.format(precision))
print('recall or sensitivity: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))

#The diagonal entries are the accuracies of each class
matriz_confusao = matriz_confusao.astype('float') / matriz_confusao.sum(axis=1)[:, np.newaxis]
acuracia_classes = matriz_confusao.diagonal()
print('Accuracy for each class:')
print(acuracia_classes)

print(classification_report(classe_teste, classe_predita, zero_division=1))

def plot_metrics(history):
  fig, axes = plt.subplots(2,1,figsize=(8,12))

  #  "Accuracy"
  axes[0].plot(history.history['categorical_accuracy'])
  axes[0].set_title('Acurácia')
  # "Loss"
  axes[1].plot(history.history['loss'])
  axes[1].set_title('Erro')

  if 'val_loss' in history.history.keys():
    axes[0].plot(history.history['val_categorical_accuracy'])
    axes[1].plot(history.history['val_loss'])
    axes[0].legend(['Treino', 'Validação'])
    axes[1].legend(['Treino', 'Validação'])

  plt.xlabel('Épocas')

  plt.show()

plot_metrics(history)