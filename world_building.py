###!!!!!! Upon reflection. Larger generalization with the names of the classes could allow more use without having to remaked essentially the same classes.

### Rename classes for use as a container for more information ###

# /*
    # So if a variable is added that allows for students and professors to be listed within the subjects, division, and school. 
    # That would make it easier to see which teachers should be where
    # To view the information within the charaacter boards. uses SQL to search the databases for ID of intended person
    
    # Would need to generalize the summary outputs for wide range of uses. 
    #Students would need to be duplicated b/c being in a class doesn't imply its your specialization field
    
# */


#Collection of classes for binding classes/subjects to a school.
# Use Cases:
    # High School
        # Use only school and division, where divisions will act as the individual classes as most classes have a uniform time
    # College/University
        # Division will act as the 'major' and subject will act as individual class titles
    
        
#individual classes
    #Name, summary, completetionTime
class Subject:
    def __init__(self, name, summary, completionTime):
        self.name = name
        self.summary = summary
        self.completionTime = completionTime
        self.professors = []
        self.students = []
        
    #Returns all variables in subject
    def summary(self):
        sum = f''
        sum+= (f'{self.name} \n\tCompletion Time: {self.completionTime} \n\tSummary: {self.summary}\n')
        sum+= f'Professors:\n'
        for i in self.professors:
            sum += f'\t{i.formal_address}\n'
        sum+= f'Students\n'    
        for x in self.students:
            sum +=f'{x.name}
    
        return sum
    
    #Returns only variables entered in initialization
    def __str__(self):
        return (f'{self.name} \n\tCompletion Time: {self.completionTime} \n\tSummary: {self.summary}\n')

#Broader Field
    #Classess are specifically as  the main use case of this iem, but other items are possible with **kwargs
class Division:
    def __init__(self, name, details,**kwargs):
        self.name = name
        self.details = details
        self.classes = []
        self.attributes = kwargs

    def addClass(self, subject):
        self.classes.append(subject)
 
    def summary(self):
        combined = ''
        combined += f'{self.name} \n{self.details}\n'
        for i in self.classes:
            combined+= i   
        for key, value in self.attributes.items():
            combined += f'\t{key}: \n{value}\n'
        return print(combined)

    def __str__(self):
        return f'{self.name} \n{self.details} \n{self.attributes}'

#School class includes
    #name, location, graudation requirements, divisions/majors, and classes
    ##!! Includes variable for staff, students, etc.
class School:
    def __init__(self,name, location,**kwargs):
        self.name = name
        self.location = location
        self.reqs = []
        self.divisions = []
        
    def addReqs(self, requirement):
        self.reqs.append(requirement)

    def addDivision(self, division):
        self.divisions.append(division)
        
    def __repr__(self):
        return f'self.name'

    def __str__(self):
        combined = ''
        combined+=f'School: {self.name} \n{self.location} \nReqs:\n'
        for i in self.reqs:
            combined += f'\t{i} \n'
        combined+= '\n'
        for i in self.divisions:
            combined+=f'{i.summary()}\n'
        return combined
        
# Make a character Class for work in progress. To be updated anytime that wiould allow python to fill as required
class Character:
	def __init__(self, name, title, pronouns, personality):
		    self.name = name
			self.title = title
			self.pns = pronouns[0] #pronoun subjective he she they
			self.pno = pronouns[1] #pronoun objective  him her them 
			self.pnp = pronouns[2] #pronoun possessive his hers theirs
			self.personality = personality #summary of the character
			self.formal_address= f'{self.title} {self.name}'
		
		
	# use
	#	MG = Characters('Jackie', 'Illusion Master', ['she','her','hers'])
	#	MG.name
	       