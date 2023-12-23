import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io


# Do NOT modifify the function names

def my_resize(img, height, width):
    # TODO_C1
    new_h, new_w = np.meshgrid(np.arange(height) , np.arange(width) , indexing='ij')
    new_h = new_h *img.shape[0]/height
    new_w = new_w * img.shape[1]/width
    h_int = (new_h).astype(int)
    w_int = (new_w).astype(int)    
    u = new_h - h_int
    v = new_w - w_int
    #Prevent crossing
    h_int = np.clip(h_int, 0, img.shape[0] - 2)
    w_int= np.clip(w_int, 0, img.shape[1] - 2)                    
    top_left = img [h_int, w_int]
    top_right=img[h_int,w_int+1]
    down_left=img[h_int+1,w_int]
    down_right=img[h_int+1,w_int+1]
    new_img = (1 - u) * (1 - v) * top_left + (1 - v)*u * down_left + v * (1 - u) * top_right + u*v * down_right
    return new_img
def my_rotation(img, angle):
    # TODO_C2
    theta = np.radians(angle)
    new_height = int(np.clip(img.shape[0] * np.sqrt(2), 0, img.shape[0]))
    new_width = int(np.clip(img.shape[1] * np.sqrt(2), 0, img.shape[1]))
    rotate_img = np.zeros((new_height , new_width))
    for i in range(new_height):
        for j in range(new_width):
            y = (i - new_height/2)*np.cos(theta) + (j - new_width/2)*np.sin(theta) + img.shape[0] / 2
            x = -(i - new_height/2)*np.sin(theta) +(j - new_width/2)*np.cos(theta) +  img.shape[1] / 2
            if 0 <= y < img.shape[0] and 0<=x<img.shape[1]:
                rotate_img[i,j] = img[int(y), int(x)]
    return rotate_img



# You are incouraged to test your program in the main function

def main():
    cat = io.imread('cat.png' ,as_gray=True)
    g = skimage.transform. resize(cat , (300,300))
    print(g.shape)
    plt.subplot(2,2,1)
    plt.imshow(g,cmap='gray')
    
    re = my_resize(cat ,20,20)
    print(re.shape)
    plt.subplot(2,2,2)
    plt.imshow(re,cmap='gray')
    
    
    plt.subplot(2,2,3)
    plt.imshow(g,cmap='gray')
    
    ro = my_rotation(cat,30)
    plt.subplot(2,2,4)
    plt.imshow(ro ,cmap= 'gray')
    print(ro.shape)
    
    
    plt.show()
    pass


if __name__ == "__main__":
    main()


