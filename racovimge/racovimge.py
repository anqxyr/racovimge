#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import base64
import jinja2
import os.path
import pathlib
import random as rand
import shutil
import subprocess
import tempfile
import textwrap

###############################################################################
# Helper Functins
###############################################################################


def to_rgb(color):
    color = color.lstrip('#')
    r, g, b = map(lambda x: int(x, 16), [color[:2], color[2:4], color[4:]])
    return 'rgb({},{},{})'.format(r, g, b)


def copy_fonts(*fonts):
    """
    Copy the fonts to the home directory.

    Necessary in order to use the fonts durring the png conversion.
    """
    root = pathlib.Path(os.path.expanduser('~')) / '.fonts/racovimge'
    if not root.exists():
        root.mkdir(parents=True)

    for font in fonts:
        new_path = root / font.split('/')[-1]
        if not new_path.exists():
            shutil.copy(font, str(new_path))


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


def wrap(text, width):
    if not isinstance(text, str):
        return text
    return textwrap.wrap(
        text, break_long_words=False, break_on_hyphens=False, width=width)


###############################################################################
# Jinja2 setup
###############################################################################

env = jinja2.Environment(loader=jinja2.PackageLoader('racovimge'))
env.filters['wrap'] = wrap
env.filters['rgb'] = to_rgb

###############################################################################
# Templates and Color Schemes
###############################################################################

ROOT = pathlib.Path(__file__).parent

templates = [i.stem for i in (ROOT / 'templates').glob('*.svg')]

with (ROOT / 'colors.txt').open() as file:
    color_schemes = [i.split() for i in file.read().split('\n')]

fonts = ROOT / 'fonts'
fonts = [i for i in fonts.glob('*.*') if i.suffix in ('.ttf', '.otf')]
fonts = [str(i.resolve()) for i in fonts]


###############################################################################
# Covers
###############################################################################


def random(
        title, author, *,
        templates=templates, schemes=color_schemes, fonts=fonts,
        font_size=120, font_size_author=70):
    template = rand.choice(templates)
    colors = rand.choice(schemes)
    font = rand.choice(fonts)
    return cover(
        title, author, template=template, colors=colors, font=font,
        font_size=font_size, font_size_author=font_size_author)


def cover(
        title, author, *, template, colors, font,
        font_size=120, font_size_author=70):
    authors = [author] if isinstance(author, str) else author
    authors = authors[:3] if authors else []
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
        color1=clr1, color2=clr2, color3=clr3, color4=clr4, color5=clr5,
        font_size=font_size, font_size_author=font_size_author)
    return image


def png_random(*args, **kwargs):
    copy_fonts(*kwargs.get('fonts', fonts))
    return to_png(random(*args, **kwargs))


def png_cover(*args, **kwargs):
    copy_fonts(kwargs['font'])
    return to_png(cover(*args, **kwargs))
