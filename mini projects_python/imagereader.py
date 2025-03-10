from PIL import Image, ImageFilter
img = Image.open("D:\\python_scripts\\my_img.JPG")  #this program is to make the image turn into grey scale
filtered = img.convert("L")
filtered.save("grey.png","png")
filtered.show()


#the below program shows how to resize the image


# from PIL import Image, ImageFilter
# img = Image.open("D:\\python_scripts\\my_img.JPG","r")
# filtered = img.convert("L")
# resized = filtered.resize((250,250))
# resized.save("me_resized.png","png")
# resized.show()

#below program shows how you can crop the images

# from PIL import Image
# img = Image.open("D:\\python_scripts\\my_img.JPG","r")
# filtered = img.convert("L")
# size = (150,150,450,450)
# new_img = filtered.crop(size)
# new_img.save("cropped_me.png","png")
# new_img.show()



#to change the size of the image without wihout interrupting the aspect ratio we can use the method called
# new_img.thumbnail note : this modifies the previous variable so no need to declare a new variable
