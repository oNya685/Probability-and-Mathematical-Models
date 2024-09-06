from PIL import Image  
  
image = Image.open('task_1\c547c6eca99620768b73a53c8dc5d4f1.jpg')  
  
width, height = image.size  

yellow_count = 0  
other_count = 0  

for x in range(width):  
    for y in range(height):  
        # 获取当前像素的RGB值  
        r, g, b = image.getpixel((x, y))  
        if r > 150 and g > 150 and b < 150:  
            yellow_count += 1  
        else:  
            other_count += 1  

if other_count != 0:  
    yellow_ratio = round(yellow_count / other_count, 5)  
    print(f"{yellow_ratio:.5f}")