import cv2 

img = cv2.imread("butterfly.jpg")
cv2.imshow("Imagem em exibicao", img)
#print(img)
imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem em exibicao", imgGray)
print(imgGray)
cv2.waitKey(0)















