import numpy as np
import cv2
import os
import time
def decrypt_function(x, y, img_path):
    start_time = time.time()
    x_array = []
    x_array.append(x)

    #create array matrix with parameter from keyboard
    for i in range(0, 10000):
        result = x_array[i]*y*(1-x_array[i])
        x_array.append(result)
    for i in range(0, len(x_array)):
        x_array[i] = float.hex(x_array[i])

    #get value of key with hexa value
    S = []
    for i in range(0, len(x_array)):
        s = x_array[i]
        s = s[5:7]
        S.append(s)

    key1D = []
    key1D.append(int(S[0], 16))
    for i in range(0, len(S)):
        count = 0
        for j in range(0, len(key1D)):
            if S[i] == key1D[j]:
                count = 1

        if count == 0:
            S[i] = int(S[i], 16)
            key1D.append(S[i])
                

        if len(key1D) == 256:
            break
    
    img = cv2.imread(img_path, 0)
    w, h = img.shape
    img = img.ravel()
    img = np.asarray(img)
    N = len(img)
    data1 = N % 256
    if data1 != 0:
        data1 = 256 - data1
        data_add = np.ones((data1))*255
        img1 = np.hstack((img, data_add))

    zeros = np.zeros((len(img1)))
    key1D = np.asarray(key1D, dtype=np.int64)
    img1.astype(np.int64)
    for i in range(0, len(img1)-256, 256):
        for j in range(i, i+256):
            temp = j % 256
            temp1 = key1D[temp]
            img1[j] = int(img1[j]) ^ temp1


    for i in range(0, len(img1)-256, 256):
        for j in range(i, i+256):
            temp = j % 256
            temp1 = key1D[temp]
            zeros[i+temp1] = img1[j]

    p = 0-data1
    img_decrypt = zeros[: p]
    img_decrypt = np.reshape(img_decrypt, (w, h))
    print("--- %s seconds ---" % (time.time() - start_time))
    return img_decrypt
    '''baseName = os.path.basename(img_path)
    imgName = 'decrypt_' + baseName
    cv2.imwrite(imgName, img_encrypt)'''