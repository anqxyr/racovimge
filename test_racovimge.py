#!/usr/bin/env python3

###############################################################################
# Module Imports
###############################################################################

import racovimge
import random
import uuid
import pathlib
import subprocess

###############################################################################


titles = [
    ('Don Quixote', 'Miguel De Cervantes'),
    ('Robinson Crusoe', 'Daniel Defoe'),
    ('Tom Jones', 'Henry Fielding'),
    ('Clarissa', 'Samuel Richardson'),
    ('Tristram Shandy', 'Laurence Sterne'),
    ('Dangerous Liaisons', 'Pierre Choderlos De Laclos'),
    ('Emma', 'Jane Austen'),
    ('Frankenstein', 'Mary Shelley'),
    ('Nightmare Abbey Thomas', 'Love Peacock'),
    ('The Black Sheep', 'Honoré De Balzac'),
    ('The Charterhouse of', 'Parma Stendhal'),
    ('The Count of Monte Cristo', 'Alexandre Dumas'),
    ('Sybil', 'Benjamin Disraeli'),
    ('David Copperfield', 'Charles Dickens'),
    ('Wuthering Heights', 'Emily Brontë'),
    ('Jane Eyre', 'Charlotte Brontë'),
    ('Vanity Fair', 'William Makepeace Thackeray'),
    ('The Scarlet Letter', 'Nathaniel Hawthorne'),
    ('Moby-Dick', 'Herman Melville'),
    ('Madame Bovary', 'Gustave Flaubert'),
    ('The Woman in White', 'Wilkie Collins'),
    ('Little Women', 'Louisa M. Alcott'),
    ('The Way We Live Now', 'Anthony Trollope'),
    ('Анна Каренина', 'Лев Толстой'),
    ('Daniel Deronda', 'George Eliot'),
    ('Братья Карамазовы', 'Фёодр Достоевский'),
    ('The Portrait of a Lady', 'Henry James'),
    ('Huckleberry Finn', 'Mark Twain'),
    ('The Strange Case of Dr Jekyll and Mr Hyde', 'Robert Louis Stevenson'),
    ('Three Men in a Boat', 'Jerome K. Jerome'),
    ('The Picture of Dorian Gray', 'Oscar Wilde'),
    ('The Diary of a Nobody', 'George Grossmith'),
    ('Jude the Obscure', 'Thomas Hardy'),
    ('The Riddle of the Sands', 'Erskine Childers'),
    ('The Call of the Wild', 'Jack London'),
    ('Nostromo', 'Joseph Conrad'),
    ('The Wind in the Willows', 'Kenneth Grahame'),
    ('In Search of Lost Time', 'Marcel Proust'),
    ('The Good Soldier Ford', 'Madox Ford'),
    ('The Thirty-Nine Steps', 'John Buchan'),
    ('Ulysses', 'James Joyce'),
    ('Mrs Dalloway', 'Virginia Woolf'),
    ('A Passage to India', 'EM Forster'),
    ('The Trial', 'Franz Kafka'),
    ('Men Without Women', 'Ernest Hemingway'),
    ('Journey to the End of the Night Louis', 'Ferdinand Celine'),
    ('As I Lay Dying', 'William Faulkner'),
    ('Brave New World', 'Aldous Huxley'),
    ('The Big Sleep', 'Raymond Chandler'),
    ('The Pursuit Of Love', 'Nancy Mitford'),
    ('The Plague', 'Albert Camus'),
    ('Nineteen Eighty-Four', 'George Orwell'),
    ('Malone Dies', 'Samuel Beckett'),
    ('Lucky Jim', 'Kingsley Amis'),
    ('Lord of the Flies', 'William Golding'),
    ('The Space Merchants', ('Frederik Pohl', 'Cyril M. Kornblut')),
    ('Inferno', ('Larry Niven', 'Jerry Pournelle')),
    ('Freedom Beach', ('James Patrick Kelly', 'John Kessel')),
    ('A Time Odyssey', ('Arthur C. Clarke', 'Stephen Baxter')),
]


def save_png(svgdata):
    name = 'testout/{}'.format(uuid.uuid4())
    svgfile = pathlib.Path(name + '.svg')
    with svgfile.open('w') as file:
        file.write(svgdata)
    subprocess.run([
        '/usr/bin/inkscape', '-z', name + '.svg', '-e', name + '.png'])
    svgfile.unlink()


def test_everything():
    for file in pathlib.Path('testout/').glob('*'):
        file.unlink()
    for template in racovimge.templates:
        for colors in racovimge.color_schemes:
            title, author = random.choice(titles)
            image = racovimge.cover(title, author, template, colors)
            save_png(image)
