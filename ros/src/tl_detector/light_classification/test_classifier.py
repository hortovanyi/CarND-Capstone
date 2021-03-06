from tl_classifier import TLClassifier
from matplotlib import pyplot as plt

classifier = TLClassifier(True)  #run in sim mode == False
import cv2
image = cv2.imread('data/test_images_real/left0140.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 8))
plt.imshow(image)
plt.show()

result = classifier.get_classification(image)
print('result: ', result)

