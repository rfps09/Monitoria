import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

def create_model(numInput):
  model = Sequential()
  model.add(Dense(4,activation='relu', input_dim=numInput))
  model.add(Dense(3,activation='softmax'))
  model.compile('adam','categorical_crossentropy', metrics=['categorical_accuracy'])

  return model


#Carregando os dados
X = np.genfromtxt('drive/MyDrive/TensorFlow/DataSets/iris.data', delimiter=',')
X = np.delete(X,4,1)
Y = np.array([0,1,2])
Y = np.repeat(Y,50)

#Separando os dados
X_gym, X_game, Y_gym, Y_game = train_test_split(X,Y,test_size=0.2)

Y_gym = to_categorical(Y_gym,num_classes = 3)

model = create_model(4)

model.fit(X_gym,Y_gym,epochs=500)

y_pred = model.predict(X_game)
print(y_pred)
y = y_pred.argmax(axis=1)
print(y)
print(str(Y_game))
