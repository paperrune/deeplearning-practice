## Results
### Keras CPU
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 24, 24, 24)        624       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 12, 12, 24)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 8, 8, 48)          28848     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 4, 4, 48)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 768)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               393728    
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
=================================================================
Total params: 428,330
Trainable params: 428,330
Non-trainable params: 0
_________________________________________________________________
Train on 60000 samples, validate on 10000 samples
Epoch 1/30
60000/60000 [==============================] - 31s 521us/step - loss: 0.1498 - acc: 0.9543 - val_loss: 0.0405 - val_acc: 0.9850
Epoch 2/30
60000/60000 [==============================] - 31s 517us/step - loss: 0.0384 - acc: 0.9877 - val_loss: 0.0324 - val_acc: 0.9894
Epoch 3/30
60000/60000 [==============================] - 31s 519us/step - loss: 0.0256 - acc: 0.9919 - val_loss: 0.0331 - val_acc: 0.9894
Epoch 4/30
60000/60000 [==============================] - 31s 521us/step - loss: 0.0189 - acc: 0.9938 - val_loss: 0.0306 - val_acc: 0.9902
Epoch 5/30
60000/60000 [==============================] - 33s 549us/step - loss: 0.0133 - acc: 0.9958 - val_loss: 0.0349 - val_acc: 0.9885
Epoch 6/30
60000/60000 [==============================] - 34s 562us/step - loss: 0.0098 - acc: 0.9971 - val_loss: 0.0328 - val_acc: 0.9904
Epoch 7/30
60000/60000 [==============================] - 33s 558us/step - loss: 0.0068 - acc: 0.9979 - val_loss: 0.0278 - val_acc: 0.9918
Epoch 8/30
60000/60000 [==============================] - 34s 572us/step - loss: 0.0060 - acc: 0.9982 - val_loss: 0.0323 - val_acc: 0.9920
Epoch 9/30
60000/60000 [==============================] - 34s 563us/step - loss: 0.0044 - acc: 0.9987 - val_loss: 0.0275 - val_acc: 0.9921
Epoch 10/30
60000/60000 [==============================] - 34s 564us/step - loss: 0.0046 - acc: 0.9987 - val_loss: 0.0289 - val_acc: 0.9928
Epoch 11/30
60000/60000 [==============================] - 32s 538us/step - loss: 0.0032 - acc: 0.9991 - val_loss: 0.0342 - val_acc: 0.9919
Epoch 12/30
60000/60000 [==============================] - 31s 520us/step - loss: 0.0023 - acc: 0.9993 - val_loss: 0.0331 - val_acc: 0.9919
Epoch 13/30
60000/60000 [==============================] - 31s 522us/step - loss: 0.0024 - acc: 0.9993 - val_loss: 0.0305 - val_acc: 0.9929
Epoch 14/30
60000/60000 [==============================] - 31s 522us/step - loss: 0.0014 - acc: 0.9996 - val_loss: 0.0308 - val_acc: 0.9927
Epoch 15/30
60000/60000 [==============================] - 32s 525us/step - loss: 0.0011 - acc: 0.9997 - val_loss: 0.0375 - val_acc: 0.9918
Epoch 16/30
60000/60000 [==============================] - 32s 529us/step - loss: 0.0026 - acc: 0.9993 - val_loss: 0.0311 - val_acc: 0.9925
Epoch 17/30
60000/60000 [==============================] - 33s 555us/step - loss: 0.0012 - acc: 0.9997 - val_loss: 0.0335 - val_acc: 0.9928
Epoch 18/30
60000/60000 [==============================] - 31s 525us/step - loss: 4.4388e-04 - acc: 1.0000 - val_loss: 0.0307 - val_acc: 0.9932
Epoch 19/30
60000/60000 [==============================] - 34s 560us/step - loss: 3.4055e-04 - acc: 1.0000 - val_loss: 0.0313 - val_acc: 0.9935
Epoch 20/30
60000/60000 [==============================] - 35s 579us/step - loss: 3.2419e-04 - acc: 1.0000 - val_loss: 0.0317 - val_acc: 0.9934
Epoch 21/30
60000/60000 [==============================] - 34s 575us/step - loss: 3.1655e-04 - acc: 1.0000 - val_loss: 0.0321 - val_acc: 0.9937
Epoch 22/30
60000/60000 [==============================] - 34s 568us/step - loss: 3.0943e-04 - acc: 1.0000 - val_loss: 0.0324 - val_acc: 0.9936
Epoch 23/30
60000/60000 [==============================] - 33s 548us/step - loss: 3.0524e-04 - acc: 1.0000 - val_loss: 0.0327 - val_acc: 0.9935
Epoch 24/30
60000/60000 [==============================] - 31s 521us/step - loss: 3.0105e-04 - acc: 1.0000 - val_loss: 0.0330 - val_acc: 0.9933
Epoch 25/30
60000/60000 [==============================] - 34s 561us/step - loss: 2.9912e-04 - acc: 1.0000 - val_loss: 0.0331 - val_acc: 0.9934
Epoch 26/30
60000/60000 [==============================] - 34s 564us/step - loss: 2.9640e-04 - acc: 1.0000 - val_loss: 0.0334 - val_acc: 0.9934
Epoch 27/30
60000/60000 [==============================] - 33s 553us/step - loss: 2.9444e-04 - acc: 1.0000 - val_loss: 0.0335 - val_acc: 0.9934
Epoch 28/30
60000/60000 [==============================] - 33s 556us/step - loss: 2.9343e-04 - acc: 1.0000 - val_loss: 0.0336 - val_acc: 0.9933
Epoch 29/30
60000/60000 [==============================] - 33s 552us/step - loss: 2.9144e-04 - acc: 1.0000 - val_loss: 0.0339 - val_acc: 0.9935
Epoch 30/30
60000/60000 [==============================] - 32s 534us/step - loss: 2.9051e-04 - acc: 1.0000 - val_loss: 0.0339 - val_acc: 0.9936
```

### Tensorflow GPU
```
loss: 0.1613 / 0.0690    accuracy: 0.9503 / 0.9751    step 1  3.99 sec
loss: 0.0442 / 0.0512    accuracy: 0.9864 / 0.9832    step 2  6.66 sec
loss: 0.0287 / 0.0371    accuracy: 0.9913 / 0.9876    step 3  9.31 sec
loss: 0.0198 / 0.0411    accuracy: 0.9940 / 0.9870    step 4  11.93 sec
loss: 0.0145 / 0.0378    accuracy: 0.9957 / 0.9876    step 5  14.45 sec
loss: 0.0116 / 0.0443    accuracy: 0.9964 / 0.9882    step 6  17.01 sec
loss: 0.0094 / 0.0451    accuracy: 0.9968 / 0.9875    step 7  19.61 sec
loss: 0.0082 / 0.0453    accuracy: 0.9972 / 0.9876    step 8  22.13 sec
loss: 0.0071 / 0.0432    accuracy: 0.9978 / 0.9885    step 9  24.64 sec
loss: 0.0052 / 0.0396    accuracy: 0.9982 / 0.9898    step 10  27.09 sec
loss: 0.0045 / 0.0639    accuracy: 0.9984 / 0.9852    step 11  29.57 sec
loss: 0.0031 / 0.0418    accuracy: 0.9989 / 0.9899    step 12  32.05 sec
loss: 0.0041 / 0.0389    accuracy: 0.9986 / 0.9904    step 13  34.60 sec
loss: 0.0020 / 0.0353    accuracy: 0.9994 / 0.9912    step 14  37.10 sec
loss: 0.0027 / 0.0484    accuracy: 0.9991 / 0.9893    step 15  39.54 sec
loss: 0.0050 / 0.0499    accuracy: 0.9985 / 0.9884    step 16  41.96 sec
loss: 0.0025 / 0.0408    accuracy: 0.9994 / 0.9906    step 17  44.45 sec
loss: 0.0012 / 0.0419    accuracy: 0.9997 / 0.9913    step 18  47.07 sec
loss: 0.0014 / 0.0449    accuracy: 0.9994 / 0.9896    step 19  49.50 sec
loss: 0.0007 / 0.0377    accuracy: 0.9998 / 0.9920    step 20  52.21 sec
loss: 0.0009 / 0.0370    accuracy: 0.9997 / 0.9921    step 21  54.74 sec
loss: 0.0004 / 0.0368    accuracy: 0.9999 / 0.9928    step 22  57.30 sec
loss: 0.0007 / 0.0399    accuracy: 0.9997 / 0.9920    step 23  59.99 sec
loss: 0.0015 / 0.0382    accuracy: 0.9996 / 0.9917    step 24  62.54 sec
loss: 0.0003 / 0.0399    accuracy: 0.9999 / 0.9921    step 25  65.05 sec
loss: 0.0002 / 0.0356    accuracy: 1.0000 / 0.9931    step 26  67.55 sec
loss: 0.0000 / 0.0357    accuracy: 1.0000 / 0.9934    step 27  69.98 sec
loss: 0.0000 / 0.0360    accuracy: 1.0000 / 0.9936    step 28  72.51 sec
loss: 0.0000 / 0.0363    accuracy: 1.0000 / 0.9937    step 29  74.97 sec
loss: 0.0000 / 0.0366    accuracy: 1.0000 / 0.9936    step 30  77.56 sec
```