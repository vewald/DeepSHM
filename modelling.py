import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import keras
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, LeakyReLU, GlobalAveragePooling2D
from keras import backend as K
from matplotlib import pyplot as plt
from IPython.display import clear_output

img_width, img_height = 3201, 193
# Variable window length for multiple scenarios:
    #101,7 #151,10 #201,13 #251,16 #301,19 #401,25 #501,31 #601,37 #801,49 
    #1001,61 #1201,73 #1601,97 #2001,121 #3201,193
train_data_dir = 'data/multiple_scene1/3200/sensor1/training'
validation_data_dir = 'data/multiple_scene1/3200/sensor1/validation'

num_classes = 6
nb_train_samples = num_classes*70
nb_validation_samples = num_classes*20
epochs = 50
batch_size = 32

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

class PlotLearning(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        self.acc = []
        self.val_acc = []
        self.fig = plt.figure()
        
        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        
        self.logs.append(logs)
        self.x.append(self.i)
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.acc.append(logs.get('categorical_accuracy'))
        self.val_acc.append(logs.get('val_categorical_accuracy'))
        self.i += 1
        
        clear_output(wait=True)
        color1 = 'tab:red'
        color2 = 'tab:blue'
        fig, ax1 = plt.subplots(figsize=(10, 6))
        ax1.set_xlabel('Epoch',size=24)
        ax1.set_ylabel('Loss',color=color1,size=24)
        ax1.plot(self.x, self.losses, label="tr_loss",color=color1,linestyle='dashed')
        ax1.plot(self.x, self.val_losses, label="val_loss",color=color1)
        ax1.tick_params(axis='x', labelsize = 16)
        ax1.tick_params(axis='y', labelcolor=color1, labelsize = 14)
        ax1.legend(loc='center right',fontsize=16,bbox_to_anchor=(0.4, 1.1),ncol = 2)
        ax1.set_ylim([0, 1.05])
        ax2 = ax1.twinx()
        ax2.set_ylabel('Accuracy',color=color2,size=24)
        ax2.plot(self.x, self.acc, label="tr_accuracy",color=color2,linestyle='dashed')
        ax2.plot(self.x, self.val_acc, label="val_accuracy",color=color2)
        ax2.tick_params(axis='y', labelcolor=color2, labelsize = 16)
        ax2.legend(loc='center right',fontsize=16, bbox_to_anchor=(1.1, 1.1),ncol = 2)
        ax2.set_ylim([0, 3])
        fig.tight_layout()
        
        plt.show();
        
#plot_losses = PlotLearning()

x_filter = 3
y_filter = 3
stride = 1
x_pool = 2
y_pool = 2
do_rate = 0.50

model = Sequential()

model.add(Conv2D(8, (x_filter, y_filter), strides = (stride, stride), activation='relu', padding='same',kernel_initializer='random_uniform', input_shape=input_shape))
model.add(MaxPooling2D((x_pool, y_pool), padding='same'))
model.add(Dropout(do_rate))
model.add(Conv2D(16, (x_filter, y_filter), strides = (stride, stride), activation='relu', padding='same'))
model.add(MaxPooling2D((x_pool, y_pool), padding='same'))
model.add(Dropout(do_rate)) 
model.add(Conv2D(32, (x_filter, y_filter), strides = (stride, stride), activation='relu', padding='same'))
model.add(MaxPooling2D((x_pool, y_pool), padding='same'))
model.add(Dropout(do_rate))
model.add(Flatten())
#model.add(GlobalAveragePooling2D())
model.add(Dense(128, activation='relu'))
model.add(Dropout(do_rate))
model.add(Dense(16, activation='relu'))
model.add(Dropout(do_rate))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['categorical_accuracy'])
model.summary()

train_datagen = ImageDataGenerator(rescale = 1. / 255)#, width_shift_range = 0.1)
test_datagen = ImageDataGenerator(rescale = 1. / 255)#, width_shift_range = 0.1)

train_generator = train_datagen.flow_from_directory(
    train_data_dir, target_size=(img_width, img_height),
    batch_size=batch_size, color_mode='rgb', class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir, target_size=(img_width, img_height),
    batch_size=batch_size, color_mode='rgb', class_mode='categorical')

model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    #callbacks=[plot_losses],
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
#model.save("F://Spyder/Perception_Modelling/src")
#print("Saved model to disk")