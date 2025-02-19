//Upon reflection. LArger generalization with the names of the classes could allow more use without having to remaked essentially the same classes

# Code Documentation #
## world_building Module ##
	Module for adding various components into a fictional world.  
	Intended to assist with story boarding for artists with unfinished ideas.  
	Interface allows for easy testing and substitution.
---
## For Schools and other similiar instituitions
### Subject(name, summary, completionTime) *class*  ###
Can be used for individual course names, (i.e. math, georgraphy).  
Course names should be unique within a **division**  
**example of use:**
``` python
	>>> hand2hand = Subject('Hand to Hand', 'Fluidity in weaponless martial arts', '3 months')  
	>>> print(hand2hand)  
	>>>	Class: Hand to Hand  
					Completion Time: 3 months  
					Summary: Fluidity in weaponless martial arts
```
#### Available Functions ####
**.sum()**  
Returns a f-string summary of the class

### Division(name, detailsOfContents) *class*  ###
Similiar to a major designtiton. Should be the over arching connector between a group of subjects. Or can be used as a singular  unique class.

**Use Cases**
	Individual class within a major

	example for use a single class:
	>>> combat = Division('Combat', 'Various forms of combat both augemented and otherwise.')
	>>>	combat
	>>> Combat
		Various forms of combat both augemented and otherwise.

	with divisions:
	>>> combat.addClass(hand2hand)
	>>> print(combat.summay)`
	>>>	Division: Combat
		Various forms of combat both augemented and otherwise.
			Class: Hand to Hand
			Completion Time: 3 months
			Summary: Fluidity in martial arts
	**Available Functions**
	.summary()
		Returns an f-string summary the division title and associated details, plus a summary of all classes currently in the division.
	.addClass(class)
		Used to bind classes to a division. Classes can be bound to multiple divisions.

	**Available variables**
- division.name
- .details
- .classes 	*(classes are **not** added at initialization)*

	**Use Cases**
	- General overarching purpose within classes
	- A class if no majors or divisions exist
	- Holder for graduation Requirements

## School
