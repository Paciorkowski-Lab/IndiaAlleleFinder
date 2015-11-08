#sets in python
set1 = set()                   # A new empty set
set1.add("cat")                # Add a single member
set1.update(["dog", "mouse"])  # Add several members
if "cat" in set1:              # Membership test
  set1.remove("cat")
#set1.remove("elephant") - throws an error
print set1
for item in set1:              # Iteration AKA for each element
  print item
print "Item count:", len(set1) # Length AKA size AKA item count
isempty = len(set1) == 0       # Test for emptiness
set1 = set(["cat", "dog"])     # Initialize set from a list
set2 = set(["dog", "mouse"])
set3 = set1 & set2             # Intersection
set4 = set1 | set2             # Union
set5 = set1 - set3             # Set difference
set6 = set1 ^ set2             # Symmetric difference
issubset = set1 <= set2        # Subset test
issuperset = set1 >= set2      # Superset test
set7 = set1.copy()             # A shallow copy
set7.remove("cat")
set8 = set1.copy()
set8.clear()                   # Clear AKA empty AKA erase
print set1, set2, set3, set4, set5, set6, set7, set8, issubset, issuperset

#therefore, check this out:

def computeCH(snvFather, snvMother, indelFather, indelMother):
	snvFatherSet = set(snvFather.keys())
	snvMotherSet = set(snvMother.keys())

	indelFatherSet = set(indelFather.keys())
	indelMotherSet = set(indelMother.keys())

	snvCHSet = snvFatherSet & snvMotherSet 
	#basically.
	#caveat: the above works on sets whose gene hashes do not have variants that both mother and father have.
	#should be handled compileParentHash (which works on 1 gene at a time)

	indelCHSet = indelFatherSet & indelMotherSet
	#probably the same caveat as above

	indelSNVSet = (snvFatherSet & indelMotherSet) | (snvMotherSet & indelFatherSet)
	#however, for this to work, the sets must be derived from geneHashes which

