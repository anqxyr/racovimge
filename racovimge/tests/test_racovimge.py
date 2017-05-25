#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import racovimge
import random
import pathlib
import subprocess

###############################################################################

titles = [
    ('A Passage to India', 'EM Forster'),
    ('A Time Odyssey', ('Arthur C. Clarke', 'Stephen Baxter')),
    ('As I Lay Dying', 'William Faulkner'),
    ('Brave New World', 'Aldous Huxley'),
    ('Clarissa', 'Samuel Richardson'),
    ('Dangerous Liaisons', 'Pierre Choderlos De Laclos'),
    ('Daniel Deronda', 'George Eliot'),
    ('David Copperfield', 'Charles Dickens'),
    ('Don Quixote', 'Miguel De Cervantes'),
    ('Emma', 'Jane Austen'),
    ('Frankenstein', 'Mary Shelley'),
    ('Freedom Beach', ('James Patrick Kelly', 'John Kessel')),
    ('Huckleberry Finn', 'Mark Twain'),
    ('In Search of Lost Time', 'Marcel Proust'),
    ('Inferno', ('Larry Niven', 'Jerry Pournelle')),
    ('Jane Eyre', 'Charlotte Brontë'),
    ('Journey to the End of the Night', 'Louis Ferdinand Celine'),
    ('Jude the Obscure', 'Thomas Hardy'),
    ('Little Women', 'Louisa M. Alcott'),
    ('Lord of the Flies', 'William Golding'),
    ('Lucky Jim', 'Kingsley Amis'),
    ('Madame Bovary', 'Gustave Flaubert'),
    ('Malone Dies', 'Samuel Beckett'),
    ('Men Without Women', 'Ernest Hemingway'),
    ('Moby-Dick', 'Herman Melville'),
    ('Mrs Dalloway', 'Virginia Woolf'),
    ('Nightmare Abbey', 'Thomas Love Peacock'),
    ('Nineteen Eighty-Four', 'George Orwell'),
    ('Nostromo', 'Joseph Conrad'),
    ('Robinson Crusoe', 'Daniel Defoe'),
    ('Sybil', 'Benjamin Disraeli'),
    ('The Big Sleep', 'Raymond Chandler'),
    ('The Black Sheep', 'Honoré De Balzac'),
    ('The Call of the Wild', 'Jack London'),
    ('The Count of Monte Cristo', 'Alexandre Dumas'),
    ('The Diary of a Nobody', 'George Grossmith'),
    ('The Picture of Dorian Gray', 'Oscar Wilde'),
    ('The Plague', 'Albert Camus'),
    ('The Portrait of a Lady', 'Henry James'),
    ('The Pursuit Of Love', 'Nancy Mitford'),
    ('The Riddle of the Sands', 'Erskine Childers'),
    ('The Scarlet Letter', 'Nathaniel Hawthorne'),
    ('The Space Merchants', ('Frederik Pohl', 'Cyril M. Kornblut')),
    ('The Strange Case of Dr Jekyll and Mr Hyde', 'Robert Louis Stevenson'),
    ('The Thirty-Nine Steps', 'John Buchan'),
    ('The Trial', 'Franz Kafka'),
    ('The Way We Live Now', 'Anthony Trollope'),
    ('The Wind in the Willows', 'Kenneth Grahame'),
    ('The Woman in White', 'Wilkie Collins'),
    ('Three Men in a Boat', 'Jerome K. Jerome'),
    ('Tom Jones', 'Henry Fielding'),
    ('Tristram Shandy', 'Laurence Sterne'),
    ('Ulysses', 'James Joyce'),
    ('Vanity Fair', 'William Makepeace Thackeray'),
    ('Wuthering Heights', 'Emily Brontë'),
    ('Анна Каренина', 'Лев Толстой'),
    ('Братья Карамазовы', 'Фёодр Достоевский'),
]


def generate_permutations():
    #for template in racovimge.templates:
    for template in ['Blocks']:
        for color in racovimge.color_schemes:
            for font in racovimge.fonts:
                yield template, color, font


def save_image(template, color, font):
    color_id = racovimge.color_schemes.index(color) + 1
    font_name = pathlib.Path(font).stem
    filename = 'output/{template} - {color_id:02d} - {font_name}.png'.format(
        template=template, color_id=color_id, font_name=font_name)
    with open(filename, 'wb') as file:
        title, author = random.choice(titles)
        file.write(racovimge.png_cover(title, author, template, color, font))


def dump_all():
    for file in pathlib.Path('output/').glob('*'):
        file.unlink()
    for args in generate_permutations():
        save_image(*args)


def test_racovimge():
    dump_all()
