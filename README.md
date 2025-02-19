# world-builder  
TKinter based gui, to assist with world building. Final product will connect with a local sqlite database. intent is to build the program on top of a Notebook Widget with four components:  
- text editor
- character viewer
- cork-board style display with either text only excerpts or world building notes
- canvas where ideas can be drawn

## Intended Modules
- information_gui
	holds all functions where program will interact with the underlying database
- menu_gui
	Standard menu gui elements and ways to export the individual tabs to other file types
	Interaction with the canvas and the cork-board components
- textManipulation
	Functions specifically to manipulate large amounts of text. *Might get collapsed into menu_gui*  
- world_building
	All of the classes that make up components of a world. Including but not limited to the characters, locations, schools, etc.
	
## The Why
- I'm writing a book and needed a way to easily preview substitutions of character information throughout the text in an instant. Also the amount of detail for each character started getting misplaced, and I realized a database would be a significantly easier way to store the information. 

## Extras
- Documentation of the modules as I finish testing the functions
- Tests for each module. Updated as the versions to maintain functionality
