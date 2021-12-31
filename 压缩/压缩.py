import cv2

input_name = 'ym.jpg'
output_name = input_name[:-4]+'_res.jpg'

print(output_name)
img = cv2.imread(input_name, 1)
cv2.imwrite(output_name, img, [cv2.IMWRITE_JPEG_QUALITY, 50])