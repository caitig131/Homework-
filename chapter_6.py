import math
# area of the surface of a sphere 4pir

def area_sphere(radius):
    result = 4 * math.pi * radius
    return result

def dist_3d(x1,y1,z1,x2,y2,z2):
    #sq_root (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
    distx = x2-x1
    disty = y2-y1
    distz = z2-z1
    result = (distx**2 + disty**2 + distz**2)**5
    #print(distx,disty,distz)
    return 0.0

def abs_val(num):
    if num >= 0:
        return num
    else:
        return -num
    
wlist = ["hello","hellothere","goodbye","later"]
def first2letters(wlist):
    for i in wlist:
        if len(i) == 2:
            return i
    return ""
word = first2letters(wlist)


test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)

    
def to_secs(hours,minutes,seconds):
    """converts hours, minutes, and seconds to a total number of seconds"""
    sec_hour = hours * 60 * 60
    sec_minutes = minutes * 60
    return sec_hour + sec_minutes + seconds
        