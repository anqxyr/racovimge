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
    # 1
    ('#d3dcf2', '#829fe4', '#447AB6', '#205B90', '#00305a'),
    # 2
    ('#e8d9ac', '#c7b07b', '#ffe28c', '#d8ab22', '#382d1a'),
    # 3
    ('#d8edb5', '#abc8a4', '#b1d17b', '#90a868', '#183128'),
    # 4
    ('#e6f1f5', '#aab3b6', '#84bace', '#80aaba', '#3b3e40'),
    # 5
    ('#069e2d', '#02601a', '#058e27', '#037720', '#fefffe'),
    # 6
    ('#eaa8d3', '#996185', '#ccbbc6', '#b2a0ac', '#493843'),
    # 7
    ('#f9ffe2', '#dceaa6', '#eeffad', '#d4e58e', '#92977e'),
    # 8 more contrast on 5
    ('#d3c0b8', '#72391e', '#bc8b74', '#c6a08f', '#463730'),
    # 9
    ('#ea4141', '#ba1212', '#260101', '#da0000', '#fffcfc'),
    # 10
    ('#892323', '#fffcfc', '#f20202', '#da0000', '#020000'),
    # 11
    ('#fcb0b0', '#f7a0a0', '#d67e7e', '#773535', '#0a0505'),
    # 12 This one is pretty cool. Unusual, but cool.
    ('#2ab7ca', '#fed766', '#cfffb3', '#fe4a49', '#330c2f'),
    # 13 4th color needs fixing.
    ('#fde8e9', '#e3bac6', '#bc9ec1', '#596475', '#1f2232'),
    # 14
    ('#fbfffe', '#faa916', '#6d676e', '#96031a', '#1b1b1e'),
    # 15
    ('#48beff', '#43c59e', '#3dfaff', '#3d7068', '#14453d'),
    # 16
    ('#452103', '#690500', '#210f04', '#934b00', '#bb6b00')]

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
    authors = authors[:2]
    clr1, clr2, clr3, clr4, clr5 = colors
    image = env.get_template(template + '.svg').render(
        title=title, authors=authors, font=font,
        color1=clr1, color2=clr2, color3=clr3, color4=clr4, color5=clr5)
    return image
