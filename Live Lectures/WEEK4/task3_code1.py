from rembg import remove
import cv2 

input_path = 'cat.jpeg'
output_path = 'cat_2.jpeg'

input = cv2.imread(input_path)

output = remove(input)

cv2.imwrite(output_path, output)