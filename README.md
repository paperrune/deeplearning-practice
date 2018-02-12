# Neural-Networks

- To classify MNIST handwritten digits, following files are required from http://yann.lecun.com/exdb/mnist/
  - train-images.idx3-ubyte
  - train-labels.idx1-ubyte
  - t10k-images.idx3-ubyte
  - t10k-labels.idx1-ubyte

- The network structure is determined by following variables in the main.cpp.

  ```C++
  string type_layer[] = {"MNIST", "Cbn", "Pmax", "Cbn,dw", "Cbn", "Pmax", "Cbn", "Lce,sm"};
  int map_width[]     = {28, 24, 12,  8,  8,  4,   1,  1};
  int map_height[]    = {28, 24, 12,  8,  8,  4,   1,  1};
  int number_maps[]   = { 1, 24, 24, 24, 48, 48, 192, 10};
  int time_step       = 1;
  ```  
  - There is no type for input layer. "MNIST" is a comments.
  - Type start with 'C(connection/convolution)' and 'P(pooling)' is for hidden layer.  
  
  	```
    C(connection/convolution)
    > Activation Function
    "ls"   : Logistic Sigmoid
    "ht"   : Hyperbolic Tangent
    ""     : default is ReLU
    
    > Property
    "dw"     : depthwise separable convolution
    "ksm,n"  : set kernel width to m and height to n  [default kernel size : (|map_width[i - 1] - map_width[i]| + 1)*(|map_height[i - 1] - map_height[i]| + 1)]
    "ksm"    = "ksm,m"
    "stm,n"  : set stride width to m and height to n  [default stride size : 1*1]
    "stm"    = "stm,m"
    "rc"     : vanilla recurrent
    "lstm"   : Long Short-Term Memory

    > Regularization
    "bn"   : Batch Normalization
    ----------------------------------------------------------------------------------------------------
    P(pooling)
    > Type
    "avg"  : Average Pooling
    "max"  : Max Pooling
    
    > Property
    "ksm,n" : set pooling width to m and height to n [default pooling size : (max(length_map[i - 1], length_map[i]) / min(length_map[i - 1], length_map[i]))^2]
    "ksm"   = "ksm,m"
    "stm,n" : set stride width to m and height to n  [default stride size : (max(length_map[i - 1], length_map[i]) / min(length_map[i - 1], length_map[i]))^2]
    "stm"   = "stm,m" 
	  ```
   - Type start with 'L(loss)' is for output layer.
   
	 ```
	 > Loss Function
	 "ce"  : Cross Entropy
	 "mse" : Mean Squared Error
	 
	 > Activation Function for "ce"
	 "sm"  : Softmax
	 ""    : default is Logistic Sigmoid

	 > Activation Function for "mse"
	 "ht"  : Hyperbolic Tangent
	 "ia"  : Identity Activation f(x) = x
	 ""    : default is Logistic Sigmoid
	 ```
</br>

## MNIST classification results
Multilayer Perceptron</br>
![MLP_result](/result/MLP.png)
</br></br>Convolutional Neural Networks</br>
![CNN_result](/result/CNN.png)
</br></br>Recurrent Neural Networks</br>
![RNN_result](/result/RNN.png)
</br></br>LSTM Recurret Neural Networks</br>
![LSTM_RNN_result](/result/LSTM.png)
