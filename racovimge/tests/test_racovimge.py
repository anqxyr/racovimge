#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import racovimge
import random
import pathlib

###############################################################################

with open('racovimge/tests/books.txt') as file:
    titles = file.read().split('\n')
    titles = [i.split(' || ') for i in titles]

for file in pathlib.Path('output/').glob('*'):
    file.unlink()


def test_templates():
    for template in racovimge.templates:
        title, author = random.choice(titles)
        cover = racovimge.png_random(title, author, templates=[template])
        with open('output/T - {}.png'.format(template), 'wb') as file:
            file.write(cover)


def test_colors():
    for color in racovimge.color_schemes:
        title, author = random.choice(titles)
        cover = racovimge.png_random(title, author, schemes=[color])
        color_index = racovimge.color_schemes.index(color) + 1
        with open('output/C - {:02d}.png'.format(color_index), 'wb') as file:
            file.write(cover)


def test_fonts():
    for font in racovimge.fonts:
        title, author = random.choice(titles)
        cover = racovimge.png_random(title, author, fonts=[font])
        font_name = font.split('/')[-1].split('.')[0]
        with open('output/F - {}.png'.format(font_name), 'wb') as file:
            file.write(cover)


def test_template_color_combinations():
    for template in racovimge.templates:
        for color in racovimge.color_schemes:
            title, author = random.choice(titles)
            font = random.choice(racovimge.fonts)
            cover = racovimge.png_cover(
                title, author,
                template=template, colors=color, font=font)
            color_index = racovimge.color_schemes.index(color) + 1
            path = 'output/A - {} - {:02d} - {}.png'.format(
                template, color_index, pathlib.Path(font).stem)
            with open(path, 'wb') as file:
                file.write(cover)
