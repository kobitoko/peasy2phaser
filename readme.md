# Peasy to Phaser P2 converter

[Peasy2Phaser.py](https://github.com/kobitoko/peasy2phaser/blob/master/Peasy2Phaser.py)  
This python script converts a Peasy json output so that Phaser P2 Physics can use it.  
Peasy2Phaser.py < JSON file to convert > < optional:Argument2 is density, 3 is friction, 4 is bounce, 5 is categoryBits, 6 is maskBits >  
  
To be used with Phaser CE, an open source HTML5 game framework. https://github.com/photonstorm/phaser-ce  

Peasy is a free polygonal hull generator found at https://yadu.itch.io/peasy

Note that each image needs a 1px transparent border for Peasy to work.
Also peasy currently names all objects as "shape" as seen in [PeasyBoxHole.json](https://github.com/kobitoko/peasy2phaser/blob/master/example/PeasyBoxHole.json).
So you'd need to manually change the name, and paste it into a big collection json file containing all your physics shapes.
If you look in [spritesPhaserExample.json](https://github.com/kobitoko/peasy2phaser/blob/master/example/spritesPhaserExample.json) it's at line 2 and renamed as BoxHole.

Edited demo in the example folder.  
BlockDonut is the addition into the example.  

It uses this phaser example https://phaser.io/examples/v2/p2-physics/body-click  

Tried also converting the output from the Physics Body Editor from [Box2D Editor](https://github.com/MovingBlocks/box2d-editor)  
Both box2d versions use the python PIL library to find out the height and width of the image.  
This script works except that the shape is vertically flipped, thus to get it correct using Physics Body Editor one can have the image upside down and export it like that from the editor for it to work in phaser the right side up:   
[Peasy+Box2d2Phaser.py](https://github.com/kobitoko/peasy2phaser/blob/master/Peasy%2BBox2d2Phaser.py)  
This version gets the shape correctly, but phaser p2 physics does not detect this shape for some reason:  
[Peasy+Box2dshapes2Phaser.py](https://github.com/kobitoko/peasy2phaser/blob/master/Peasy%2BBox2dshapes2Phaser.py)  
