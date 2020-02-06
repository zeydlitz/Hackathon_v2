import cv2
import re
import numpy as np
import copy
class Data:
    def __init__(self):
        with open(r'Testers\tester_1\WorkFile.txt', 'r') as f:
            self.polygon(f.readline())
            self.rgb(f.readline())
            self.culture = f.readline()
            self.path = f.readline()
        self.img=cv2.imread(self.path)

    def polygon(self, str):
        self.coordinates = []
        result = re.findall(r'\d{1,4}', str)
        while result:
            self.coordinates.append([int(result[i]) for i in range(2)])
            result = result[2:]

    def rgb(self, str):
        self.RGB1, self.RGB2 = [], []
        result = re.findall(r'\d{1,3}', str)
        self.RGB1 = [int(result[i]) for i in range(3)]
        self.RGB2 = [int(result[i]) for i in range(3, 6)]


    def domask(self,color):
        mask = np.ones(self.test.shape, np.uint8)
        mask.fill(255)
        cv2.fillPoly(mask, np.array([self.coordinates], dtype=np.int32), color)
        mask1 = np.ones(self.test.shape, np.uint8)
        mask1.fill(255)
        cv2.bitwise_and(self.test, mask, mask1)
        cv2.imwrite(r'Testers\tut\tut_v\1.jpg',mask1)

    def doblur(self):
        self.img=cv2.GaussianBlur(self.img,(5,5),cv2.BORDER_DEFAULT)
        cv2.imwrite(r'Testers\tut\tut_v\blur.jpg',self.img)

    def docut(self):
        self.test=copy.deepcopy(self.img)
        test = copy.deepcopy(self.img)
        mask= np.zeros(self.img.shape, np.uint8)
        cv2.fillPoly(mask, np.array([self.coordinates], dtype=np.int32), (255, 255, 255))
        cv2.rectangle(self.img, (0, 0), (self.img.shape[1], self.img.shape[0]), (0, 255, 0), -1)
        cv2.copyTo(test,mask,self.img)
        cv2.imwrite(r'Testers\tut\tut_v\cut.jpg', self.img)


    def dofind(self):
        check=self.img[0,0]
        counterW,counterB=0,0
        OutputImage=cv2.inRange(self.img,tuple(self.RGB1),tuple(self.RGB2))
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                if list(self.img[i,j])!=list(check):
                    if OutputImage[i,j]==255:
                        counterW+=1
                    else:
                        counterB+=1
                        OutputImage[i][j]=120
        cv2.imwrite(r'Testers\tut\tut_v\OutputImage.jpg', OutputImage)
        result=float(counterB/(counterB+counterW))*100
        print(f"Result: {int(result)}% damage!\n")
        if result>50:
            self.domask((0,20,255))
        elif result<30: self.domask((0,255,0))
        else: self.domask((0,216,255))




    def makework(self):
        self.doblur()
        self.docut()
        self.dofind()

    def __str__(self):
        print(f"Coordinates : \n {self.coordinates}")
        print(f"Color range from {self.RGB1} to {self.RGB2}")
        print(f"Culture : {self.culture}")
        with open(r'Testers\tut\tut_v\WorkFile.txt', 'w') as f:
            f.write(str(self.coordinates))
            f.write(str(self.RGB1 + self.RGB2))
            f.write(str(self.culture))
        return "Fine"
if __name__ == "__main__":
    da=Data()
    da.makework()
    print(da)

