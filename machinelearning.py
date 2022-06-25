def ml_imageprediction(inputimage):
    def trainmodel():
        from keras.datasets import fashion_mnist
        from keras.utils import to_categorical
        from keras.layers import Dense
        from keras.layers import Flatten
        from keras.optimizers import SGD
        from keras.models import Sequential
        from keras.layers import Conv2D
        from keras.layers import MaxPooling2D

        def dataset():
        	(trainX, trainY), (testX, testY) = fashion_mnist.load_data()
        	trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
        	testX = testX.reshape((testX.shape[0], 28, 28, 1))
        	trainY = to_categorical(trainY)
        	testY = to_categorical(testY)
        	return trainX, trainY, testX, testY

        def preparepixels(train, test):
        	train_norm = train.astype('float32')
        	test_norm = test.astype('float32')
        	train_norm = train_norm / 255.0
        	test_norm = test_norm / 255.0
        	return train_norm, test_norm

        def definemodel():
        	model = Sequential()
        	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        	model.add(MaxPooling2D((2, 2)))
        	model.add(Flatten())
        	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
        	model.add(Dense(10, activation='softmax'))
        	opt = SGD(lr=0.01, momentum=0.9)
        	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
        	return model

        def run_test_harness():
        	trainX, trainY, testX, testY = dataset()
        	trainX, testX = preparepixels(trainX, testX)
        	model = definemodel()
        	model.fit(trainX, trainY, epochs=10, batch_size=32, verbose=0)
        	model.save('clothesmodel.h5')

        run_test_harness()

    def evaluate():
        from keras.datasets import fashion_mnist
        from keras.models import load_model
        from keras.utils import to_categorical

        def load_dataset():
        	(trainX, trainY), (testX, testY) = fashion_mnist.load_data()
        	trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
        	testX = testX.reshape((testX.shape[0], 28, 28, 1))
        	trainY = to_categorical(trainY)
        	testY = to_categorical(testY)
        	return trainX, trainY, testX, testY

        def prep_pixels(train, test):
        	train_norm = train.astype('float32')
        	test_norm = test.astype('float32')
        	train_norm = train_norm / 255.0
        	test_norm = test_norm / 255.0
        	return train_norm, test_norm

        trainX, trainY, testX, testY = load_dataset()
        trainX, testX = prep_pixels(trainX, testX)
        model = load_model('clothesmodel.h5')
        _, acc = model.evaluate(testX, testY, verbose=0)
        accura = '> %.3f' % (acc * 100.0)
        print(accura)

    def predictimage(imgname):
        from keras.models import load_model
        from keras.utils import load_img
        from keras.utils import img_to_array
        import numpy as np
        def load_image(filename):
        	img = load_img(filename, color_mode = "grayscale", target_size=(28, 28)) #grayscale=True
        	img = img_to_array(img)
        	img = img.reshape(1, 28, 28, 1)
        	img = img.astype('float32')
        	img = img / 255.0
        	return img

        img = load_image(str(imgname))
        model = load_model('clothesmodel.h5')
        predicted = np.argmax(model.predict(img),axis=1)
        #print(predicted[0])
        return predicted[0]

    #trainmodel()
    #evaluate()
    #predictimage('sample_image.png')

    def classify(modelprediction):
        if modelprediction == 0:
            return "t-shirt"
        if modelprediction == 1:
            return "trousers"
        if modelprediction == 2:
            return "pullover shirt"
        if modelprediction == 3:
            return "dress"
        if modelprediction == 4:
            return "coat"
        if modelprediction == 5:
            return "sandal"
        if modelprediction == 6:
            return "shirt"
        if modelprediction == 7:
            return "sneakers"
        if modelprediction == 8:
            return "bag/backpack"
        if modelprediction == 9:
            return "boots"

    def aipredict(inputimage):
        result = classify(predictimage(inputimage))
        print(result)
        return result


    return aipredict(inputimage)
#ml_imageprediction("sample_image.png")
