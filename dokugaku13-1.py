class Rectangle:
    def __init__(self,v,w):
        self.vertical=v
        self.width=w
    def calculate_perimeter(self):
        return (self.vertical+self.width)*2

class Square:
    def __init__(self,l):
        self.line=l
    def calculate_perimeter(self):
        return self.line*4
    
print("長方形の縦と横の長さを入力してね")
rectangle=Rectangle(int(input("縦:")),int(input("横:")))
print("周りの長さは…")
print(rectangle.calculate_perimeter())

print("")

print("正方形の1辺の長さを入力してね")
square=Square(int(input("1辺:")))
print("周りの長さは…")
print(square.calculate_perimeter())

