import cv2
import label_image

def load_image(image):
    text = label_image.main(image)
    img = cv2.imread(image)
    return img, text

img,text = load_image('./tes/tes1.jpg')
cv2.put_text(img,'Makanannya adalah: '+ text, (40,20),cv2.FONT_HERSHEY_PLAIN)
cv2.imshow('Prediksi',img)
cv2.waitKey(0)