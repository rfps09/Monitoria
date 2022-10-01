from tabnanny import verbose
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

X1 = np.array([1,1,0,0])
X2 = np.array([1,0,1,0])
X = np.stack((X1,X2),axis=1)
Y = np.array([1,1,1,0])
Y = to_categorical(Y)

def create_model(numInputs):
    model = Sequential()
    model.add(Dense(numInputs,input_dim=numInputs))
    model.add(Dense(10,activation='relu'))
    model.add(Dense(2,activation='softmax'))
    model.compile('Adam','categorical_crossentropy',metrics=['categorical_accuracy'])
    return model

model = create_model(2)

history = model.fit(X,Y,epochs=500,verbose=2)

resp = model.predict(X)

print(resp)