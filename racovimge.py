#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import jinja2
import random as rand
import pathlib

###############################################################################
# Jinja2 setup
###############################################################################

env = jinja2.Environment(loader=jinja2.PackageLoader('racovimge'))

###############################################################################
# Templates and Color Schemes
###############################################################################

templates = pathlib.Path(__file__).parent / 'templates'
templates = [i.stem for i in templates.glob('*.svg')]
color_schemes = [
    ('#d3dcf2', '#829fe4', 'pink', 'pink', '#00305a'),
]

###############################################################################
# Covers
###############################################################################


def random(
        title, author, templates=templates, schemes=color_schemes, png=True):
    template = rand.choice(templates)
    colors = rand.choice(schemes)
    return cover(title, author, template, colors, png)


def cover(title, author, template, colors):
    authors = [author] if isinstance(author, str) else author
    clr1, clr2, clr3, clr4, clr5 = colors
    image = env.get_template(template + '.svg').render(
        title=title, authors=authors,
        color1=clr1, color2=clr2, color3=clr3, color4=clr4, color5=clr5)
    return image
