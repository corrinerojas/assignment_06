class Point(object):
    def __init__(self,x,y,mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    def check_coincident(self,point2):
        check_this_point = (self.x,self.y)
        return check_coincident(point1, point2)
 
    def shift_point(self, x_shift, y_shift):
        point = (self.x, self.y)
 	self.x, self.y = shift_point(point, x_shift, y_shift)
