import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

def create_model(numInput):
  model = Sequential()
  model.add(Dense(4,activation='relu',input_dim=numInput))
  model.add(Dense(2,activation='softmax'))
  model.compile('RMSprop', 'categorical_crossentropy', metrics=['categorical_accuracy'])

  return model

model = create_model(2)

X_gym = np.array([[0,0],[0,1],[1,0],[1,1]])
Y_gym = np.array([0,1,1,0])

X_game = np.array([[0,0],[0,1],[1,0],[1,1]])
Y_game = np.array([0,1,1,0])

Y_gym = to_categorical(Y_gym)
Y_game = to_categorical(Y_game)

model.fit(X_gym,Y_gym,epochs=500)

y_pred = model.predict(X_game)
print(y_pred)
y = y_pred.argmax(axis=1)
print(y)
