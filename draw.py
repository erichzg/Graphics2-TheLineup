from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = (y1-y0)/(x0-x1)
    B = 1
    C = -1 * x0 * A - y0

    if (x0 > x1):
        x = x1
        x1 = x0
        y = y1
        y1 = y0
    else:
        x = x0
        y = y0
    
    if ((x1-x0)/(y1-y0) > 1):
        d = 2A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y++
                d += 2B
            x++
            d += 2A

    elif ((x1-x0)/(y1-y0) > 0):
        d = A + 2B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x++
                d += 2A
            y++
            d += 2B

    elif ((x1-x0)/(y1-y0) < -1):
        d = 2A - B
        while (x <= x0):
            plot(screen, color, x, y)
            if (d > 0):
                y--
                d += 2B
            x++
            d += 2A
    elif ((x1-x0)/(y1-y0) < 0):
        d = 2B - A
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x--
                d += 2A
            y++
            d += 2B
    
        
