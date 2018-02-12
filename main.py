from display import *
from draw import *

def selectColor(x0, y0, x1, y1):
    return [(x1-x0)%128 + 128, (y1-y0)%128 + 128, (x0-y0)%128 + 128]

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(250, 250, 500, 400, screen, selectColor(250, 250, 500, 400)) #OCT 1
draw_line(250, 250, 500, 500, screen, selectColor(250, 250, 500, 500)) #OCT 1-2
draw_line(250, 250, 400, 500, screen, selectColor(250, 250, 400, 500)) #OCT 2
draw_line(250, 250, 250, 500, screen, selectColor(250, 250, 250, 500)) #OCT 2-3 UNDEF
draw_line(250, 250, 100, 500, screen, selectColor(250, 250, 100, 500)) #OCT 3
draw_line(250, 250, 0, 500, screen, selectColor(250, 250, 0, 500)) #OCT 3-4
draw_line(250, 250, 0, 400, screen, selectColor(250, 250, 0, 400)) #OCT 4
draw_line(250, 250, 0, 250, screen, selectColor(250, 250, 0, 250)) #OCT 4-5
draw_line(250, 250, 0, 100, screen, selectColor(250, 250, 0, 100)) #OCT 5
draw_line(250, 250, 0, 0, screen, selectColor(250, 250, 0, 0)) #OCT 5-6
draw_line(250, 250, 100, 0, screen, selectColor(250, 250, 100, 0)) #OCT 6
draw_line(250, 250, 250, 0, screen, selectColor(250, 250, 250, 0)) #OCT 6-7 UNDEF
draw_line(250, 250, 400, 0, screen, selectColor(250, 250, 400, 0)) #OCT 7
draw_line(250, 250, 500, 0, screen, selectColor(250, 250, 500, 0)) #OCT 7-8
draw_line(250, 250, 500, 100, screen, selectColor(250, 250, 500, 100)) #OCT 8
draw_line(250, 250, 500, 250, screen, selectColor(250, 250, 500, 250)) #OCT 8-1

display(screen)
save_extension(screen, 'img.png')
