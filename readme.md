Peasy to Phaser P2 converter  
  
This python script converts a Peasy json output so that Phaser P2 Physics can use it.  

Using Phaser CE, an open source HTML5 game framework. https://github.com/photonstorm/phaser-ce  
  
Peasy is a free polygonal hull generator found at https://yadu.itch.io/peasy   
  
Note that each image needs a 1px transperant border for Peasy to work.  
Also peasy currently names all objects as "shape" as seen in PeasyBoxHole.json.   
So you'd need to manually change the name, and paste it into a big collection json file containing all your physics shapes.  
If you look in spritesPhaserExample.json it's at line 2 and renamed as BoxHole.  

Edited demo at https://kobitoko.github.io/peasy2phaser/  

It uses this phaser example https://phaser.io/examples/v2/p2-physics/body-click  
