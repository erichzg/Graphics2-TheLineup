from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    if (x0 > x1):
        x = x1
        x1 = x0
        x0 = x
        y = y1
        y1 = y0
        y0 = y
    else:
        x = x0
        y = y0
        
    if (x1 == x0):
        if (y1 > y0):
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
            return
        while (y >= y1):
            plot(screen, color, x, y)
            y -= 1
        return
    
    A = y1-y0
    B = x0-x1

    if ((-1.0) * A/B >= 1):
        d = A + 2 * B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    elif ((-1.0) * A/B >= 0):
        d = 2 * A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    elif ((-1.0) * A/B <= -1):
        d = A - 2 * B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
            
    elif ((-1.0) * A/B < 0):
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
    
        
