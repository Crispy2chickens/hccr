import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint

from densenet import DenseNet121
from resnet import ResNet101

num_classes = 200
input_shape = (64, 64, 3)
train_data_dir = 'datasets/new-trn'
val_data_dir = 'datasets/new-val'
test_data_dir = 'datasets/new-tst'

epochs = 40

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(64, 64),
    batch_size=128,
    class_mode='categorical',
    color_mode='rgb'
)

val_generator = test_datagen.flow_from_directory(
    val_data_dir,
    target_size=(64, 64),
    batch_size=128,
    class_mode='categorical',
    color_mode='rgb'
)

# Start of DenseNet

# base_model = DenseNet121(
#     include_top=False,
#     weights='imagenet',
#     input_shape=input_shape,
#     pooling='max',
#     classes=num_classes,
#     attention_module='cbam_block'
# )

# x = base_model.output
# predictions = Dense(num_classes, activation='softmax')(x)

# model = Model(inputs=base_model.input, outputs=predictions)

# End of DenseNet

# Start of ResNet

base_model = ResNet101(
    include_top=False,
    weights='imagenet',
    input_shape=input_shape,
    pooling='max',
    classes=num_classes,
    attention_module='cbam_block'
)

x = base_model.output
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# End of ResNet

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

model.summary()

checkpoint = ModelCheckpoint('resnet_cbam.keras', monitor='val_loss', save_best_only=True, verbose=1)

history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=val_generator,
    callbacks=[checkpoint]
)

val_loss = history.history['val_loss']

optimal_epoch = val_loss.index(min(val_loss)) + 1

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(64, 64),
    batch_size=128,
    class_mode='categorical',
    color_mode='rgb'
)

final_score = model.evaluate(test_generator, verbose=0)
print('Test loss after {} epochs:'.format(epochs), final_score[0])
print('Test accuracy after {} epochs:'.format(epochs), final_score[1])

model.load_weights('resnet_cbam.keras')

optimal_score = model.evaluate(test_generator, verbose=0)
print(f'Test loss at optimal epoch ({optimal_epoch}):', optimal_score[0])
print(f'Test accuracy at optimal epoch ({optimal_epoch}):', optimal_score[1])

train_loss = history.history['loss']
epochs_range = range(1, len(train_loss) + 1)

plt.plot(epochs_range, train_loss, label='Train Loss')
plt.plot(epochs_range, val_loss, label='Val Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.axvline(epochs_range[val_loss.index(min(val_loss))], color='r', linestyle='--', label='Optimal Epoch')
plt.legend()
plt.savefig('resnet_cbam.png')
plt.show()