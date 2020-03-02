# Grace Keane - G00359990
# Bsc in Computing in Software Development
# Demonstrating the use of classes using python and Thompsons construction

class thompson_classes:
    # Every state has 0, 1 or 2 edges
    # None = 0
    
    edges = []

    # Label for arrows, none means epsilon
    label1 = None

    # Creating a constructor for the class
    def __init__(self, label=None, edges=[]):

        # Instances
        self.edges = edges
        self.label = label

# Fragments are a combination of states
class NFA_Fragments:

    # Member variabes

    # Start state of NFA fragment
    start = None
    # Accept state of NFA fragment
    accept = None

    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

myinstance = thompson_classes(label='a', edges=[])
myinstancetwo = thompson_classes(edges=[myinstance])

myfragment = NFA_Fragments(myinstance, myinstancetwo)

# Print to screen
print(myinstance.label)
print(myinstancetwo.edges[0])

# Should print out a memory address of where myfragment is located
print(myfragment)






