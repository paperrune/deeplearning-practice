## Results
### Keras CPU
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 512)               401920    
_________________________________________________________________
dense_2 (Dense)              (None, 512)               262656    
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 10)                5130      
=================================================================
Total params: 669,706
Trainable params: 669,706
Non-trainable params: 0
_________________________________________________________________
Train on 60000 samples, validate on 10000 samples
Epoch 1/50
60000/60000 [==============================] - 4s 74us/step - loss: 0.6927 - acc: 0.7676 - val_loss: 0.2573 - val_acc: 0.9184
Epoch 2/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.1567 - acc: 0.9535 - val_loss: 0.1187 - val_acc: 0.9628
Epoch 3/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.1002 - acc: 0.9703 - val_loss: 0.1200 - val_acc: 0.9610
Epoch 4/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0749 - acc: 0.9778 - val_loss: 0.0792 - val_acc: 0.9772
Epoch 5/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0564 - acc: 0.9834 - val_loss: 0.0735 - val_acc: 0.9785
Epoch 6/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0464 - acc: 0.9862 - val_loss: 0.0747 - val_acc: 0.9783
Epoch 7/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0370 - acc: 0.9889 - val_loss: 0.0695 - val_acc: 0.9812
Epoch 8/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0310 - acc: 0.9901 - val_loss: 0.0666 - val_acc: 0.9805
Epoch 9/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0271 - acc: 0.9917 - val_loss: 0.0710 - val_acc: 0.9807
Epoch 10/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0213 - acc: 0.9932 - val_loss: 0.0726 - val_acc: 0.9821
Epoch 11/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0179 - acc: 0.9946 - val_loss: 0.0707 - val_acc: 0.9802
Epoch 12/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0150 - acc: 0.9951 - val_loss: 0.0758 - val_acc: 0.9818
Epoch 13/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0118 - acc: 0.9964 - val_loss: 0.0780 - val_acc: 0.9802
Epoch 14/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0120 - acc: 0.9961 - val_loss: 0.0841 - val_acc: 0.9796
Epoch 15/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0089 - acc: 0.9975 - val_loss: 0.0729 - val_acc: 0.9823
Epoch 16/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0077 - acc: 0.9978 - val_loss: 0.0715 - val_acc: 0.9836
Epoch 17/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0059 - acc: 0.9983 - val_loss: 0.0792 - val_acc: 0.9826
Epoch 18/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0071 - acc: 0.9979 - val_loss: 0.0817 - val_acc: 0.9812
Epoch 19/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0094 - acc: 0.9972 - val_loss: 0.0805 - val_acc: 0.9818
Epoch 20/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0061 - acc: 0.9983 - val_loss: 0.0774 - val_acc: 0.9829
Epoch 21/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0054 - acc: 0.9986 - val_loss: 0.0827 - val_acc: 0.9818
Epoch 22/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0057 - acc: 0.9983 - val_loss: 0.0804 - val_acc: 0.9830
Epoch 23/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0041 - acc: 0.9988 - val_loss: 0.0825 - val_acc: 0.9837
Epoch 24/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0039 - acc: 0.9990 - val_loss: 0.0753 - val_acc: 0.9847
Epoch 25/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0037 - acc: 0.9990 - val_loss: 0.0796 - val_acc: 0.9831
Epoch 26/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0031 - acc: 0.9993 - val_loss: 0.0819 - val_acc: 0.9832
Epoch 27/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0032 - acc: 0.9992 - val_loss: 0.0792 - val_acc: 0.9841
Epoch 28/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0035 - acc: 0.9991 - val_loss: 0.0836 - val_acc: 0.9834
Epoch 29/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0029 - acc: 0.9993 - val_loss: 0.0805 - val_acc: 0.9843
Epoch 30/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0028 - acc: 0.9993 - val_loss: 0.0790 - val_acc: 0.9844
Epoch 31/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0015 - acc: 0.9997 - val_loss: 0.0857 - val_acc: 0.9833
Epoch 32/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0030 - acc: 0.9993 - val_loss: 0.0864 - val_acc: 0.9825
Epoch 33/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0018 - acc: 0.9996 - val_loss: 0.0799 - val_acc: 0.9840
Epoch 34/50
60000/60000 [==============================] - 4s 70us/step - loss: 0.0018 - acc: 0.9995 - val_loss: 0.0783 - val_acc: 0.9848
Epoch 35/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0011 - acc: 0.9998 - val_loss: 0.0808 - val_acc: 0.9852
Epoch 36/50
60000/60000 [==============================] - 4s 69us/step - loss: 7.6074e-04 - acc: 0.9999 - val_loss: 0.0824 - val_acc: 0.9852
Epoch 37/50
60000/60000 [==============================] - 4s 69us/step - loss: 7.4901e-04 - acc: 0.9999 - val_loss: 0.0793 - val_acc: 0.9858
Epoch 38/50
60000/60000 [==============================] - 4s 69us/step - loss: 8.1797e-04 - acc: 0.9999 - val_loss: 0.0810 - val_acc: 0.9852
Epoch 39/50
60000/60000 [==============================] - 4s 70us/step - loss: 8.4137e-04 - acc: 0.9999 - val_loss: 0.0833 - val_acc: 0.9849
Epoch 40/50
60000/60000 [==============================] - 4s 69us/step - loss: 8.6784e-04 - acc: 0.9998 - val_loss: 0.0850 - val_acc: 0.9854
Epoch 41/50
60000/60000 [==============================] - 4s 69us/step - loss: 6.8015e-04 - acc: 1.0000 - val_loss: 0.0819 - val_acc: 0.9855
Epoch 42/50
60000/60000 [==============================] - 4s 69us/step - loss: 5.5333e-04 - acc: 1.0000 - val_loss: 0.0843 - val_acc: 0.9851
Epoch 43/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0012 - acc: 0.9997 - val_loss: 0.0842 - val_acc: 0.9847
Epoch 44/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0017 - acc: 0.9997 - val_loss: 0.0839 - val_acc: 0.9847
Epoch 45/50
60000/60000 [==============================] - 4s 69us/step - loss: 9.8619e-04 - acc: 0.9998 - val_loss: 0.0831 - val_acc: 0.9857
Epoch 46/50
60000/60000 [==============================] - 4s 69us/step - loss: 0.0012 - acc: 0.9998 - val_loss: 0.0809 - val_acc: 0.9851
Epoch 47/50
60000/60000 [==============================] - 4s 69us/step - loss: 5.9557e-04 - acc: 1.0000 - val_loss: 0.0820 - val_acc: 0.9856
Epoch 48/50
60000/60000 [==============================] - 4s 70us/step - loss: 4.8731e-04 - acc: 1.0000 - val_loss: 0.0815 - val_acc: 0.9855
Epoch 49/50
60000/60000 [==============================] - 4s 69us/step - loss: 7.2984e-04 - acc: 0.9999 - val_loss: 0.0825 - val_acc: 0.9850
Epoch 50/50
60000/60000 [==============================] - 4s 69us/step - loss: 5.1572e-04 - acc: 1.0000 - val_loss: 0.0829 - val_acc: 0.9853
```

### Tensorflow GPU
```
loss: 0.6770 / 0.3056	accuracy: 0.7716 / 0.9055	step 1  1.51 sec
loss: 0.1482 / 0.1583	accuracy: 0.9558 / 0.9486	step 2  2.73 sec
loss: 0.0977 / 0.1090	accuracy: 0.9711 / 0.9669	step 3  3.94 sec
loss: 0.0707 / 0.0871	accuracy: 0.9788 / 0.9741	step 4  5.16 sec
loss: 0.0538 / 0.0904	accuracy: 0.9837 / 0.9726	step 5  6.38 sec
loss: 0.0413 / 0.0750	accuracy: 0.9874 / 0.9777	step 6  7.60 sec
loss: 0.0332 / 0.0783	accuracy: 0.9900 / 0.9765	step 7  8.83 sec
loss: 0.0270 / 0.0869	accuracy: 0.9913 / 0.9745	step 8  10.03 sec
loss: 0.0225 / 0.0904	accuracy: 0.9931 / 0.9749	step 9  11.23 sec
loss: 0.0177 / 0.0720	accuracy: 0.9945 / 0.9807	step 10  12.45 sec
loss: 0.0144 / 0.0783	accuracy: 0.9956 / 0.9810	step 11  13.66 sec
loss: 0.0129 / 0.0827	accuracy: 0.9961 / 0.9788	step 12  14.86 sec
loss: 0.0108 / 0.0760	accuracy: 0.9967 / 0.9815	step 13  16.11 sec
loss: 0.0095 / 0.0683	accuracy: 0.9970 / 0.9828	step 14  17.31 sec
loss: 0.0074 / 0.0745	accuracy: 0.9978 / 0.9818	step 15  18.53 sec
loss: 0.0067 / 0.0809	accuracy: 0.9982 / 0.9814	step 16  19.73 sec
loss: 0.0066 / 0.0818	accuracy: 0.9980 / 0.9813	step 17  20.95 sec
loss: 0.0057 / 0.0846	accuracy: 0.9983 / 0.9805	step 18  22.17 sec
loss: 0.0058 / 0.0853	accuracy: 0.9984 / 0.9815	step 19  23.41 sec
loss: 0.0049 / 0.0792	accuracy: 0.9987 / 0.9827	step 20  24.64 sec
loss: 0.0046 / 0.0827	accuracy: 0.9987 / 0.9806	step 21  25.84 sec
loss: 0.0029 / 0.0835	accuracy: 0.9993 / 0.9816	step 22  27.03 sec
loss: 0.0022 / 0.0773	accuracy: 0.9996 / 0.9835	step 23  28.26 sec
loss: 0.0025 / 0.0768	accuracy: 0.9994 / 0.9832	step 24  29.48 sec
loss: 0.0023 / 0.0842	accuracy: 0.9994 / 0.9822	step 25  30.69 sec
loss: 0.0017 / 0.0799	accuracy: 0.9996 / 0.9835	step 26  31.88 sec
loss: 0.0011 / 0.0830	accuracy: 0.9998 / 0.9838	step 27  33.13 sec
loss: 0.0014 / 0.0742	accuracy: 0.9997 / 0.9846	step 28  34.32 sec
loss: 0.0014 / 0.0812	accuracy: 0.9998 / 0.9844	step 29  35.56 sec
loss: 0.0020 / 0.0772	accuracy: 0.9996 / 0.9844	step 30  36.75 sec
loss: 0.0030 / 0.0908	accuracy: 0.9992 / 0.9823	step 31  37.96 sec
loss: 0.0015 / 0.0802	accuracy: 0.9996 / 0.9838	step 32  39.19 sec
loss: 0.0007 / 0.0810	accuracy: 1.0000 / 0.9841	step 33  40.37 sec
loss: 0.0007 / 0.0775	accuracy: 0.9999 / 0.9855	step 34  41.64 sec
loss: 0.0005 / 0.0811	accuracy: 1.0000 / 0.9849	step 35  42.83 sec
loss: 0.0003 / 0.0810	accuracy: 1.0000 / 0.9850	step 36  44.05 sec
loss: 0.0003 / 0.0780	accuracy: 1.0000 / 0.9855	step 37  45.28 sec
loss: 0.0004 / 0.0840	accuracy: 1.0000 / 0.9847	step 38  46.47 sec
loss: 0.0007 / 0.0865	accuracy: 0.9998 / 0.9847	step 39  47.69 sec
loss: 0.0004 / 0.0843	accuracy: 1.0000 / 0.9849	step 40  48.92 sec
loss: 0.0002 / 0.0846	accuracy: 1.0000 / 0.9851	step 41  50.11 sec
loss: 0.0003 / 0.0829	accuracy: 1.0000 / 0.9847	step 42  51.35 sec
loss: 0.0004 / 0.0843	accuracy: 1.0000 / 0.9854	step 43  52.58 sec
loss: 0.0002 / 0.0836	accuracy: 1.0000 / 0.9858	step 44  53.80 sec
loss: 0.0004 / 0.0857	accuracy: 1.0000 / 0.9847	step 45  55.01 sec
loss: 0.0024 / 0.1060	accuracy: 0.9993 / 0.9805	step 46  56.25 sec
loss: 0.0030 / 0.0804	accuracy: 0.9990 / 0.9845	step 47  57.48 sec
loss: 0.0012 / 0.0837	accuracy: 0.9997 / 0.9846	step 48  58.70 sec
loss: 0.0004 / 0.0853	accuracy: 1.0000 / 0.9851	step 49  59.95 sec
loss: 0.0002 / 0.0854	accuracy: 1.0000 / 0.9851	step 50  61.16 sec
```

### Neural_Networks CPU
```
loss: 0.6632 / 0.2505	accuracy: 0.9194 / 0.9174	step 1  90.32 sec
loss: 0.1473 / 0.1299	accuracy: 0.9647 / 0.9604	step 2  179.77 sec
loss: 0.0958 / 0.0949	accuracy: 0.9773 / 0.9725	step 3  269.01 sec
loss: 0.0714 / 0.0840	accuracy: 0.9827 / 0.9744	step 4  358.29 sec
loss: 0.0534 / 0.0792	accuracy: 0.9868 / 0.9767	step 5  447.69 sec
loss: 0.0412 / 0.1029	accuracy: 0.9830 / 0.9703	step 6  537.05 sec
loss: 0.0328 / 0.0824	accuracy: 0.9900 / 0.9761	step 7  626.08 sec
loss: 0.0282 / 0.0798	accuracy: 0.9920 / 0.9781	step 8  715.52 sec
loss: 0.0234 / 0.0831	accuracy: 0.9929 / 0.9774	step 9  805.44 sec
loss: 0.0188 / 0.0741	accuracy: 0.9949 / 0.9804	step 10  895.31 sec
loss: 0.0162 / 0.0832	accuracy: 0.9948 / 0.9789	step 11  985.07 sec
loss: 0.0144 / 0.0839	accuracy: 0.9947 / 0.9784	step 12  1074.79 sec
loss: 0.0111 / 0.0797	accuracy: 0.9976 / 0.9803	step 13  1164.29 sec
loss: 0.0087 / 0.0776	accuracy: 0.9982 / 0.9810	step 14  1254.27 sec
loss: 0.0105 / 0.0843	accuracy: 0.9972 / 0.9796	step 15  1343.74 sec
loss: 0.0074 / 0.0828	accuracy: 0.9969 / 0.9815	step 16  1433.36 sec
loss: 0.0057 / 0.0794	accuracy: 0.9988 / 0.9830	step 17  1522.54 sec
loss: 0.0050 / 0.0790	accuracy: 0.9986 / 0.9827	step 18  1611.81 sec
loss: 0.0052 / 0.0856	accuracy: 0.9977 / 0.9812	step 19  1701.17 sec
loss: 0.0240 / 0.0891	accuracy: 0.9916 / 0.9752	step 20  1790.53 sec
loss: 0.0111 / 0.0734	accuracy: 0.9987 / 0.9814	step 21  1879.86 sec
loss: 0.0056 / 0.0755	accuracy: 0.9994 / 0.9833	step 22  1969.41 sec
loss: 0.0034 / 0.0717	accuracy: 0.9996 / 0.9837	step 23  2058.72 sec
loss: 0.0026 / 0.0756	accuracy: 0.9999 / 0.9848	step 24  2148.12 sec
loss: 0.0040 / 0.0761	accuracy: 0.9995 / 0.9831	step 25  2237.63 sec
loss: 0.0029 / 0.0731	accuracy: 0.9998 / 0.9842	step 26  2326.94 sec
loss: 0.0027 / 0.0794	accuracy: 0.9997 / 0.9842	step 27  2416.16 sec
loss: 0.0026 / 0.0818	accuracy: 0.9999 / 0.9837	step 28  2505.87 sec
loss: 0.0013 / 0.0788	accuracy: 1.0000 / 0.9843	step 29  2596.49 sec
loss: 0.0014 / 0.0820	accuracy: 1.0000 / 0.9830	step 30  2686.10 sec
loss: 0.0015 / 0.0798	accuracy: 1.0000 / 0.9846	step 31  2776.11 sec
loss: 0.0014 / 0.0815	accuracy: 0.9998 / 0.9840	step 32  2865.58 sec
loss: 0.0013 / 0.0851	accuracy: 0.9999 / 0.9828	step 33  2954.96 sec
loss: 0.0008 / 0.0813	accuracy: 1.0000 / 0.9839	step 34  3044.26 sec
loss: 0.0006 / 0.0831	accuracy: 1.0000 / 0.9833	step 35  3133.88 sec
loss: 0.0006 / 0.0849	accuracy: 1.0000 / 0.9834	step 36  3223.59 sec
loss: 0.0003 / 0.0842	accuracy: 1.0000 / 0.9834	step 37  3313.08 sec
loss: 0.0004 / 0.0823	accuracy: 1.0000 / 0.9843	step 38  3402.85 sec
loss: 0.0016 / 0.0855	accuracy: 0.9999 / 0.9841	step 39  3492.52 sec
loss: 0.0007 / 0.0859	accuracy: 1.0000 / 0.9843	step 40  3582.15 sec
loss: 0.0004 / 0.0834	accuracy: 1.0000 / 0.9847	step 41  3671.59 sec
loss: 0.0010 / 0.0869	accuracy: 0.9999 / 0.9844	step 42  3761.18 sec
loss: 0.0012 / 0.0831	accuracy: 1.0000 / 0.9841	step 43  3850.63 sec
loss: 0.0011 / 0.0898	accuracy: 0.9998 / 0.9832	step 44  3940.59 sec
loss: 0.0012 / 0.0809	accuracy: 1.0000 / 0.9847	step 45  4030.42 sec
loss: 0.0006 / 0.0828	accuracy: 1.0000 / 0.9845	step 46  4120.07 sec
loss: 0.0004 / 0.0902	accuracy: 1.0000 / 0.9840	step 47  4209.33 sec
loss: 0.0003 / 0.0832	accuracy: 1.0000 / 0.9846	step 48  4298.55 sec
loss: 0.0003 / 0.0836	accuracy: 1.0000 / 0.9844	step 49  4387.98 sec
loss: 0.0002 / 0.0837	accuracy: 1.0000 / 0.9850	step 50  4477.58 sec
```