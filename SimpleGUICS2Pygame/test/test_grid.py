#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw points, lines and polygons. (December 13, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version
    from pygame.version import ver as pygame_version
    from SimpleGUICS2Pygame import _VERSION as GUI_VERSION

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + pygame_version
    GUI_VERSION = 'SimpleGUICS2Pygame ' + GUI_VERSION
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'


TEST = 'test grid'

WIDTH = 400
HEIGHT = 300

SIZE = 80


state_colors = True
state_method = 0


def draw(canvas):
    """
    Draw grid with 3 methods.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    if state_colors:
        color1 = 'White'
        color2 = 'Gray'
        color3 = 'Yellow'
    else:
        color1 = color2 = color3 = 'White'

    if state_method == 0:
        draw_grid1(canvas, 0, color1)
        draw_grid2(canvas, HEIGHT//3, color2)
        draw_grid3(canvas, HEIGHT*2//3, color3)
    elif state_method == 1:
        draw_grid3(canvas, 0, color3)
        draw_grid1(canvas, HEIGHT//3, color1)
        draw_grid2(canvas, HEIGHT*2//3, color2)
    else:
        draw_grid2(canvas, 0, color2)
        draw_grid3(canvas, HEIGHT//3, color3)
        draw_grid1(canvas, HEIGHT*2//3, color1)


def draw_grid1(canvas, y_offset, color):
    """
    Draw grid with points.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    :param y_offset: int or float >= 0
    :param color: str
    """
    s = 'points'
    width = frame.get_canvas_textwidth(s, SIZE)

    canvas.draw_text(s, ((WIDTH - width)//2, y_offset + (HEIGHT/3 + SIZE/4)/2),
                     SIZE, color)

    for y in range(0, HEIGHT//3, 20):
        y += y_offset
        for x in range(0, WIDTH):
            canvas.draw_point((x, y), color)

    for x in range(0, WIDTH, 40):
        for y in range(y_offset, y_offset + HEIGHT):
            canvas.draw_point((x, y), color)


def draw_grid2(canvas, y_offset, color):
    """
    Draw grid with lines.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    :param y_offset: int or float >= 0
    :param color: str
    """
    s = 'lines'
    width = frame.get_canvas_textwidth(s, SIZE)

    canvas.draw_text(s, ((WIDTH - width)//2, y_offset + (HEIGHT/3 + SIZE/4)/2),
                     SIZE, color)

    for y in range(0, HEIGHT//3, 20):
        y += y_offset
        canvas.draw_line((0, y), (WIDTH - 1, y), 1, color)

    for x in range(0, WIDTH, 40):
        canvas.draw_line((x, y_offset), (x, y_offset + HEIGHT//2 - 1),
                         1, color)


def draw_grid3(canvas, y_offset, color):
    """
    Draw grid with polygons (rectangles).

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    :param y_offset: int or float >= 0
    :param color: str
    """
    s = 'rectangles'
    width = frame.get_canvas_textwidth(s, SIZE)

    canvas.draw_text(s, ((WIDTH - width)//2, y_offset + (HEIGHT/3 + SIZE/4)/2),
                     SIZE, color)

    for y in range(0, HEIGHT//3, 20):
        y += y_offset
        for x in range(0, WIDTH, 40):
            canvas.draw_polygon(((x, y), (x + 40, y),
                                 (x + 40, y + 20), (x, y + 20)),
                                1, color)


def switch_color():
    """
    Switch between 3 different colors and all in white.
    """
    global state_colors

    state_colors = not state_colors


def switch_method():
    """
    Switch position of the 3 methods.
    """
    global state_method

    state_method = (state_method + 1) % 3


# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
frame.add_button('Switch color', switch_color)
frame.add_button('Switch method', switch_method)
frame.add_label('')
frame.add_button('Quit', frame.stop)

frame.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        frame._save_canvas_and_stop(argv[1])


frame.start()
