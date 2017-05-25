#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import base64
import jinja2
import random as rand
import pathlib
import textwrap
import tempfile
import subprocess

###############################################################################
# Helper Functins
###############################################################################


def to_rgb(color):
    color = color.lstrip('#')
    r, g, b = map(lambda x: int(x, 16), [color[:2], color[2:4], color[4:]])
    return 'rgb({},{},{})'.format(r, g, b)


def to_png(image):
    _, path = tempfile.mkstemp(suffix='.svg')
    with open(path, 'w') as file:
        file.write(image)
    outpath = path.replace('.svg', '.png')
    subprocess.call(['rsvg', path, outpath])
    with open(outpath, 'rb') as file:
        data = file.read()
    pathlib.Path(path).unlink()
    pathlib.Path(outpath).unlink()
    return data


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
    ('#d3dcf2', '#829fe4', '#6692c3', '#4878a4', '#00305a'),  # 01
    ('#e8d9ac', '#c7b07b', '#ffe28c', '#d8ab22', '#382d1a'),  # 02
    ('#d8edb5', '#abc8a4', '#b1d17b', '#90a868', '#183128'),  # 03
    ('#e6f1f5', '#aab3b6', '#a1bac4', '#6a7275', '#3b3e40'),  # 04
    ('#eaa8d3', '#996185', '#c964a6', '#d897c1', '#49223b'),  # 05
    ('#d3c0b8', '#917569', '#bc8b74', '#72391e', '#332923'),  # 06
    ('#fffcfc', '#892323', '#c42121', '#2d2727', '#020000'),  # 07
    ('#fcb0b0', '#d67e7e', '#f7a0a0', '#773535', '#0a0505'),  # 08
    ('#2ab7ca', '#fed766', '#cfffb3', '#fe4a49', '#330c2f'),  # 09
    ('#fde8e9', '#e3bac6', '#bc9ec1', '#596475', '#1f2232'),  # 10
    ('#ffffff', '#f9e316', '#faa916', '#96031a', '#000000'),  # 11
    ('#452103', '#690500', '#210f04', '#934b00', '#bb6b00'),  # 12
]

fonts = pathlib.Path(__file__).parent / 'fonts'
fonts = [i for i in fonts.glob('*.*') if i.suffix in ('.ttf', '.otf')]
fonts = [str(i.resolve()) for i in fonts]


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
    authors = authors[:3]
    clr1, clr2, clr3, clr4, clr5 = colors

    font_mimetypes = dict(
        otf='font/opentype',
        ttf='application/x-font-ttf')

    font = pathlib.Path(font)
    with font.open('rb') as file:
        font_data = file.read()
        font_data = base64.b64encode(font_data).decode('utf-8')
    font_name = font.stem
    font_type = font_mimetypes[font.suffix.lstrip('.')]

    image = env.get_template(template + '.svg').render(
        title=title, authors=authors,
        font=font_name, font_type=font_type, font_data=font_data,
        color1=clr1, color2=clr2, color3=clr3, color4=clr4, color5=clr5)
    return image


def png_random(*args, **kwargs):
    return to_png(random(*args, **kwargs))


def png_cover(*args, **kwargs):
    return to_png(cover(*args, **kwargs))
