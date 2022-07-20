## problem  
There are n military planes in the sky.  
each plane can target other planes infront and below itself.  
the number of planes that each plane can target is called strategic number.  
calculate sum of strategic number of all planes.  

## solve using binary search tree  
We need to maintain a sorted list to find values lower than a certain number.  
BST tree can address this problem, but there is an issue,  
How should we count numbers smaller than a certain number in a tree?  

## custom BST  
by adding a new attribute called left_count to each node of the tree, we can count smaller numbers efficiently.  
left_count is the total number of nodes that exist on the left side of the node.  
the value of left_count should be updated by each new insert,  
if the new node traverses through left side of a node, the value of the left_count will be increamented by 1.  
now we can use this new attribute to count numbers smaller than a specific number,  
while searching for the node,  
every time we traverse through right side of a node, we have to add node.attribute to sum of lower numbers count.  
