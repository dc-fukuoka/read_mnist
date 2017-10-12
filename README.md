read_mnist - read the MNIST training data by python.
===
requirements: numpy, matplotlib  
the data format is explained in http://yann.lecun.com/exdb/mnist/  
how to use:  
~~~
$ wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
$ wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
$ ./read_mnist.py 1 # <-- show the 1st data, from 0 to 59999
answer:  0
~~~
![Alt text](./mnist1.png?raw=true "mnist 1")
