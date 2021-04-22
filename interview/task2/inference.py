import numpy as np
import keras
from keras.preprocessing import image

img = image.load_img('dataset/images_new/0_1.jpg',target_size=(64,64,3))                       
img = image.img_to_array(img)                       
img = img/255

model = keras.models.load_model("my_h5_model.h5")

classes = np.array(train.columns[1:])
proba = model.predict(img.reshape(1,64,64,3))
plt.imshow(img)
for i in range(2):
  print("{}".format(classes[i])+" ({:.3})".format(proba[0][i]))