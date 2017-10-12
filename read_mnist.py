#!/usr/bin/env python3

import struct
import gzip
import sys
import numpy as np
import matplotlib.pyplot as plt

def draw_heatmap(data, min_value, max_value):
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues, vmin=min_value, vmax=max_value)
    ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)    
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    plt.show()

def read_mnist():
    with gzip.open("train-labels-idx1-ubyte.gz", "rb") as f:
        data     = struct.unpack_from(">2i60000B", f.read(), offset=0)
        magic    = data[0]
        ndata    = data[1]
        labels   = np.array(data[2:])
        if ndata != len(labels):
            print("ndata:", ndata, "len(labels):", len(labels))
            sys.exit(-1)

    with gzip.open("train-images-idx3-ubyte.gz", "rb") as f:
        data     = struct.unpack_from(">4i47040000B", f.read(), offset=0) # 47040000 = 60000 * 28 * 28
        magic    = data[0]
        ndata    = data[1]
        nrows    = data[2]
        ncols    = data[3]
        images   = np.array(data[4:], dtype=np.uint8).reshape((ndata, nrows, ncols))
        if ndata != len(labels):
            print("ndata:", ndata, "len(labels):", len(labels))
            sys.exit(-1)

    return {"labels":labels, "images":images}

def main():
    argv = sys.argv
    argc = len(argv)
    if argc == 1:
        img_no = 0
    else:
        img_no = int(sys.argv[1])

    labels = "labels"
    images = "images"

    train_data = read_mnist()
        
    print("answer: ", train_data[labels][img_no])
    draw_heatmap(train_data[images][img_no,:,:], 0.0, 1.0)
    
if __name__ == "__main__":
    main()
