import cv2
def resizeImg(imgLnk,scaleInPercent):
    src = cv2.imread(imgLnk, cv2.IMREAD_UNCHANGED)
    new_width = int(src.shape[1]*scaleInPercent/100)
    new_height = int(src.shape[0]*scaleInPercent/100)
    # resize image
    output = cv2.resize(src, (new_width, new_height))
    #cv2.imshow('Resized image',output)
    cv2.imwrite('new_img.jpg', output)
    print('succussfuly Resized')
    
    #cv2.waitKey(0)
#print(src.shape)
#src.reshape(2000,2000,1)
def inputData():
    global img,scale_percent
    img=input('please provide us image : ')
    scale_percent=int(input('how mach size you want in percent : '))
if __name__=='__main__':
    img=None
    scale_percent=None
    inputData()
    #print(img,scale_percent)
    resizeImg(img,scale_percent)
    
