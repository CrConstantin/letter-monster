
  Letter-Monster Engine Documentation

-------------
  Contents:
-------------

 - About
 - Requirements
 - How to use

###############

----------
  About:
----------
 * Letter-Monster is a text rendering engine.
    It renders letters in a very similar way to a 2D/3D engine that renders pixels.
 * Can transform images (JPG, PNG, BMP) into : ASCII Text, mono-color Excel tables, mono-color HTML tables.
 * Can create complex text shapes and text interfaces.
 * Can make mono-color ASCII animations.
 * Can generate programs that respond to user input and react to events.
 * Can be used for ASCII movies, web design, or games.
    Can be embeded into websites, or can become standalone applications.
 * There will two distinct versions of Letter-Monster : colored and non-colored.
    In colored version, each letter has a color, in non-colored version, only plain letters are used to describe shapes.
 * Letter-Monster Backpack can edit large TXT files : rotate, mirror, align, crop, resize, border, etc.
 * Letter-Monster is 100% free. No hidden costs. You can use it anywhere, anyhow, anytime.
    Letter-Monster will always be free, for home or commercial users. Please check Licence.

-----------------
  Requirements:
-----------------
 * Python 2.5. Letter-Monster is written entirely in Python 2.5. (www.python.org)
 * Numpy. All data is represented as Numpy tables; they are fast and use little memory. (numpy.scipy.org)
 * Psyco. Makes Letter-Monster 2 times faster. It uses a lot of memory. (psyco.sourceforge.net)
 * Python Image Library (PIL). Manipulates images. Used to transform images into ASCII. (www.pythonware.com/products/pil)

---------------
  How to use:
---------------
 * In order to use Letter-Monster, all you have to do is "import _letter_monster".
    Just make sure that Python can find the path to "_letter_monster.py" file.
    Or, you can copy "_letter_monster.py" and "_classes.py" into "C:\Python25\Lib", to be able to import them anytime.
 * All functions from LetterMonster and Backpack classes are well documented.
 * All examples delivered with Letter-Monster work out-of-the-box. Just open them with Python:
    c:\Python25\python.exe "... path to example file ..."
    You can double click any example, if you installed Python 2.5 as default program that openes ".py" files.
