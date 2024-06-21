#!/usr/bin/env python
# coding: utf-8

# # Midterm Question - 21

# __int()__: Constructor that takes as input a pair of Point objects that represent the ends points of the line segment
# 
# Length():: returns the length if the segment 
# 
# Slope() returns the slope of the segment of none if the slope is unbounded 

# In[9]:


# Answer - 21

class P:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        
class S:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    # Calculate distance between 2 points
    def length(self):
        return ((self.p2.a - self.p1.a)**2 + (self.p2.b - self.p1.b)**2)**0.5
    
    def slope(self):
        if self.p2.a == self.p1.a:
            return None
        else:
            return (self.p2.b - self.p1.b)/(self.p2.a - self.p1.a)
        
Point1 = P(3, 4)
Point2 = P()

Segment = S(Point1,Point2)
length = Segment.length()
slope = Segment.slope()

print("Length of the segment is:" , length)
print("Slope of the segment is: ", slope)     

