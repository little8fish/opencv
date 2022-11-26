import matplotlib.pyplot as plt
import cv2 as cv


def show_img(img, mode=None, figsize=None):
    if figsize:
        plt.figure(figsize=figsize)
    plt.imshow(img[:,:,::-1], cmap=mode)
    plt.axis('off')


def show_more_img(row_col, *imgs):
    fig, axs = plt.subplots(*row_col, figsize=(20, 16))
    for i, img in enumerate(imgs):
        try:
            axs[i].imshow(img[:, :, ::-1])
        except:
            axs[i].imshow(img)


def cv_show(*imgs):
    for i, img in enumerate(imgs):
        print(img.shape)
        cv.imshow(str(i), img)
    cv.waitKey()

