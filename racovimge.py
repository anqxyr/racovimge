#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import jinja2
import random as rand
import pathlib
import textwrap

###############################################################################
# Helper Functins
###############################################################################


def to_rgb(color):
    color = color.lstrip('#')
    r, g, b = map(lambda x: int(x, 16), [color[:2], color[2:4], color[4:]])
    return f'rgb({r},{g},{b})'


###############################################################################
# Jinja2 setup
###############################################################################

env = jinja2.Environment(loader=jinja2.PackageLoader('racovimge'))
env.filters['wrap'] = textwrap.wrap
env.filters['rgb'] = to_rgb

###############################################################################
# Templates and Color Schemes
###############################################################################

templates = pathlib.Path(__file__).parent / 'templates'
templates = [i.stem for i in templates.glob('*.svg')]

color_schemes = [
    ('#d3dcf2', '#829fe4', '#447AB6', '#205B90', '#00305a'),
    ('#e8d9ac', '#c7b07b', '#ffe28c', '#d8ab22', '#382d1a'),
    ('#d8edb5', '#abc8a4', '#b1d17b', '#90a868', '#183128'),
    ('#e6f1f5', '#aab3b6', '#84bace', '#80aaba', '#3b3e40'),
]

fonts = [
    'Liberation Serif',
]

###############################################################################
# Covers
###############################################################################


def random(
        title, author,
        templates=templates, schemes=color_schemes, fonts=fonts):
    template = rand.choice(templates)
    colors = rand.choice(schemes)
    font = rand.choice(fonts)
    return cover(title, author, template, colors, font)


def cover(title, author, template, colors, font):
    authors = [author] if isinstance(author, str) else author
    clr1, clr2, clr3, clr4, clr5 = colors
    image = env.get_template(template + '.svg').render(
        title=title, authors=authors, font=font,
        color1=clr1, color2=clr2, color3=clr3, color4=clr4, color5=clr5)
    return image
