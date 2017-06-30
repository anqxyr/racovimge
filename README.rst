racovimge
=========

**racovimge** is a minimalistic library for generating random
placeholder book covers. It allows generating svg or png covers, and can
be used as a python library or as a command line utility.

Installation
~~~~~~~~~~~~

::

    pip install --user racovimge

Basic Usage
~~~~~~~~~~~

.. code:: python

    import racovimge

    # generate random svg cover
    cover = racovimge.random('As I Lay Dying', 'William Faulkner')

    # generate specific cover and write it to a file
    with open('cover.svg', 'w') as stream:
        stream.write(racovimge.cover(
            title='The Ambassadors',
            # note that author is optional.
            # Multiple authors can be passed as a non-str iterator as well.
            author='Henry James',
            template='Simple Dark',
            colors=['#d3dcf2', '#829fe4', '#6692c3', '#4878a4', '#00305a'],
            font='/path/to/otf/or/ttf/file',
            font_size=120,  # Used for the title of the book.
            font_size_author=70  # Used for the authors.
            ))

    # Passing non-str iterable as title allows for explicit line breaks,
    # which is useful for longer titles
    cover = racovimge.random(['Strange Case', 'of Dr. Jekyll', 'and Mr. Hyde'], 'Robert Louis Stevenson')

    # generate random png file and write it to file
    # note that unlike for svg, the file must be opened in binary mode
    with open('cover.png', 'wb') as stream:
        # font sizes can be set explicitly even for random covers
        stream.write(racovimge.png_random('The Odyssey', 'Homer', font_size=200))


    # specifying keyword arguments for random generators enables limiting the output results
    cover = racovimge.random(
        'The Killer Angels',
        'Michael Shaara',
        templates=['Blocks', 'Simple Dark', 'Tiles'],
        fonts=racovimge.fonts[:4],
        schemes=racovimge.color_schemes[2:8])

Using as Command Line Utility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate a random cover:

::

    racovimge One Flew Over the Cuckoo's Nest --authors "Ken Kesey"

Note that unlike titles author names must be quoted. Multiple
space-separated authors can be supplied.

To generate a png cover:

::

    racovimge --png A Moveable Feast -a "Ernest Hemingway"

To generate multipe covers with a given prefix:

::

    racovimge The War of the Worlds -a "H. G. Wells" --output war --count 10 --png

This will create files war01.png, war02.png, ... war10.png in the
current directory. You can also specify an absolute path:

::

    racovimge The Chronicles of Narnia -o /home/user/books/narnia/cover -c 5

Limitations
~~~~~~~~~~~

The cover templates, color schemes, and fonts, have been carefully
selected to work in combination with each other. Despite of that, some
combinations of various parameters will still produce aesthetically
unpleasing covers. In particular, some of the fonts combined with longer
book titles do not fit completely within some of the cover templates.
This can be ammended by decreasing the font size, explicitly specifying
linebreak points in the titles, or by just generating a different random
cover. Thankfully, **racovimge** makes the later process quite easy, and
it can be repeated multiple times until you get a cover you're a
satisfied with.

Generating png covers requires **rsvg** to be installed on Linux system.
On Windows and MacOS, it is untested and unlikely to work.

The current version of **racovimge** is 0.9, and should be considered a
beta. The core functionality is complete, but it still contains a number
of rough edges. The documentation can be improved, particularly in
regards to the command line utility. The API for some of the optional
parameters can be changed to accomodate non-default values better. Minor
fixes to existing color schemes and cover templates can be made, as well
as more schemes, templates, and fonts can be added to the library.
Unfortunately, the author of the library does not have time to do any of
these things, and so **racovimge** will remain in its current state for
an as of yet undetermined amount of time.

Acknowledgements
~~~~~~~~~~~~~~~~

**racovimge** is inspired by the cover-generator found in the excellent
`calibre <https://github.com/kovidgoyal/calibre>`__ e-book manager.
**racovimge** also borrows some color schemes and svg elements from it.

The following free fonts are bundled with **racovimge**: `Alex
Brush <https://fontlibrary.org/en/font/alex-brush>`__,
`Bellota <https://fontlibrary.org/en/font/bellota>`__, `Bradley
Gratis <https://fontlibrary.org/en/font/bradley-gratis>`__,
`Caladea <https://fontlibrary.org/en/font/caladea>`__,
`Crimson <https://fontlibrary.org/en/font/crimson>`__,
`Gidole <https://github.com/larsenwork/Gidole>`__, `Glacial
Indifference <https://fontlibrary.org/en/font/glacial-indifference>`__,
`Great Vibes <https://fontlibrary.org/en/font/rebecca>`__,
`Horta <https://fontlibrary.org/en/font/horta>`__, `Liberation
Serif <https://fontlibrary.org/en/font/liberation-serif>`__, `Libre
Baskerville <https://fontlibrary.org/en/font/libre-baskerville>`__,
`Orkney <https://fontlibrary.org/en/font/orkney>`__, `Petit Formal
Script <https://fontlibrary.org/en/font/petit-formal-script>`__,
`Sofia <https://fontlibrary.org/en/font/sofia>`__, and
`Unique <https://fontlibrary.org/en/font/unique>`__.

The cover templates used by **racovimge** include svg elements taken
from the following design collections:

-  `Decorative Floral
   Elements <http://all-free-download.com/free-vector/download/vector-set-of-decorative-floral-elements-for-design_570139.html>`__
   by `webdesignhot <http://www.webdesignhot.com/>`__
-  `Vintage Frame Border
   Elements <http://all-free-download.com/free-vector/download/vintage-design-element-set-frame-border-floral-label_6815728.html>`__
   by `BSGStudio <http://buysellgraphic.com/>`__
-  `Border Decoration
   Elements <http://all-free-download.com/free-vector/download/vector-border-decoration-design-elements_148134.html>`__
   by `webdesignhot <http://www.webdesignhot.com/>`__

