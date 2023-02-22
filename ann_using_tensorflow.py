from PIL import Image
from tensorflow.python.keras import datasets, layers, models
import matplotlib.pyplot as plt, numpy as np, random, tensorflow as tf

# training_images_lst = []
# training_labels_lst = []

# for i in range(0, 3, 2):
#     for j in range(102):
#         im = Image.open(f"ai_dataset/category_{i}_formatted/category_{i}_formatted_img_{j}.png", 'r')

#         pixels_arr = np.array(list(im.getdata()))
#         img_size = im.size
#         pixels_arr.resize(img_size[1], img_size[0], 3)
#         training_images_lst.append(pixels_arr)

#         training_labels_lst.append(np.array([i // 2])) # "category 0 "'s label is "0" and "category 2"'s label is "1"

# random.seed(10)
# random.shuffle(training_images_lst)
# random.seed(10)
# random.shuffle(training_labels_lst)

# training_images_arr = np.array(training_images_lst) / 255.0
# training_labels_arr = np.array(training_labels_lst)

class_names = ["category 0", "category 2"]

test_images_lst = []

for i in range(20):
    im = Image.open(f"ai_dataset/test_images_formatted/test_img_{i}_category_{int(4 < i < 15)}.png", 'r')

    pixels_arr = np.array(list(im.getdata()))
    img_size = im.size
    pixels_arr.resize(img_size[1], img_size[0], 3)
    test_images_lst.append(pixels_arr)

test_images_arr = np.array(test_images_lst) / 255.0
test_labels_arr = np.array([np.array(int(4 < i < 15)) for i in range(20)])

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# history = model.fit(training_images_arr, training_labels_arr, epochs=50, batch_size=32,
#                     validation_data=(test_images_arr, test_labels_arr))

# model.save_weights('./checkpoints/my_checkpoint')

# plt.plot(history.history["accuracy"], label="training")
# plt.plot(history.history["val_accuracy"], label="test")
# plt.ylim(0, 1)
# plt.legend()
# plt.show()

test_loss, test_acc = model.evaluate(test_images_arr,  test_labels_arr, verbose=2)
print(test_acc)

model.load_weights('./checkpoints/my_checkpoint')

test_loss, test_acc = model.evaluate(test_images_arr,  test_labels_arr, verbose=2)
print(test_acc)

# predictions = model.predict(test_images_arr)

# for i in range(len(test_images_lst)):
#     print(i, int(4 < i < 15), np.argmax(predictions[i]))
# print(len([1 for i in range(len(test_images_lst)) if np.argmax(predictions[i]) == int(4 < i < 15)]) / len(test_images_lst))