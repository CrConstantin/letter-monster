
 * Letter-Monster Engine Documentation *

-------------
  Contents:
-------------

 - About
 - Licence
 - Requirements
 - How to use
 - Changes
 - TODO

###############

----------
  About:
----------
 * Letter-Monster is a multi-layer text rendering engine.
    It renders letters in a very similar way to a 2D/3D engine that renders pixels.
 * Can transform images (BMP, JPG, PNG, PSD, TGA) into : ASCII Text, CSV, mono-color HTML tables, ASCII images.
 * Can create complex text shapes and text interfaces.
 * Can generate ASCII animations.
 * Can make programs that respond to user input and react to events.
 * Can be used for ASCII movies, web design, games.
    Can be embeded into command line applications, game engines like Pygame and Pyglet, web-sites,
    or can become standalone applications.
 * Letter-Monster Backpack can edit large TXT files : rotate, mirror, align, crop, resize, border, etc.
 * There will be two distinct versions of Letter-Monster : colored and non-colored.
    In colored version, each letter has a color, in non-colored version, only plain letters are used to describe shapes.
 * Letter-Monster is 100% free. No hidden costs. You can use it anywhere, anyhow, anytime.
    Letter-Monster will always be free, for home or commercial users. Please check the Licence.

------------
  Licence:
------------
  Letter-Monster Engine and Letter-Monster Logo are copyright © 2009, Cristi Constantin. All rights reserved.

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  If you redistribute this software, neither the name of "Letter Monster"
  nor the names of its contributors may be used to endorse or promote
  products derived from this software without specific prior written
  permission.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License (GPL) for more details.

  You have received a copy of the GNU General Public License along
  with this program.

-----------------
  Requirements:
-----------------
 * Python 2.5. Letter-Monster is written entirely in Python 2.5. (www.python.org)
 * Python-Numpy. All data is represented as Numpy tables; they are fast and use little memory. (numpy.scipy.org)
 * Python Image Library (PIL). Manipulates and creates images. (www.pythonware.com/products/pil)

 * (Optional) Python-Psyco. Makes Letter-Monster 2-3 times faster. It uses quite a lot of memory. (psyco.sourceforge.net)
 * (Optional) Pygame. Used to render in Pygame. (www.pygame.org)
 * (Optional) Pyglet. Used to render in Pyglet. (www.pyglet.org)

---------------
  How to use:
---------------
 * In order to access Letter-Monster classes, all you have to do is "import _letter_monster".
    Just make sure that Python can find the path to "_letter_monster.py" file. Check the examples.
    Alternatively, you can copy "_letter_monster.py" and "_classes.py" into "C:\Python25\Lib".
    This way, you will be able to import them anytime, without specifying a path.
 * A LOT of time was spent to document all modules, classes and functions in Letter-Monster, so enjoy.
 * All examples delivered with Letter-Monster work out-of-the-box. Just open them with Python:
    > c:\Python25\python.exe "... path to example file ..."
    in Windows, or
    $ python ... path to example file ...
    in Linux.

---------------------------
 Changes from version 0.1:
---------------------------
 * New overwrite engine. Multiple transparent characters are allowed and position will move the layer.
 * Tested LMGL files with Python 2.5 and 2.6 in Windows, Ubuntu and Mandriva. They are all compatible.
 * Implemented simple Spawn for : BMP, GIF, JPG, PNG.
 * Implemented simple Render : pygame, pyglet.
 * Added a lot of documentation.

--------
  TODO:
--------
 * Instructions for Macro Layers. This will allow creating/ deleting/ renaming/ changing attributes of other layers from within LMGL.
 * Fast export LMGL as PDF, PS, EPS, GIF animation, Excel animation, SWF app, etc.
 * Draw ASCII shapes: circle, rectangle, polygon, etc, with a lot of options.
 * ASCII blur, sharpen, darken, lighten.
 * More Speed for all render and export functions.
 * Make a GUI to visualize and edit LMGL files.
