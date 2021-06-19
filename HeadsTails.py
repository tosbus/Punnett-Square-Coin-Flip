import random

def coinflip():
	if random.randint(1,2) == 1:
		return 'Tails'
	else:
		return 'Heads'

def genotype():
	if coinflip() == 'Heads':
		g1 = 'A'
	else:
		g1 = 'a'
	if coinflip() == 'Heads':
		g2 = 'A'
	else:
		g2 = 'a'

	return (g1+g2)
 
def test(iterations):
	AA, Aa, aa = 0, 0, 0
	for m in range(iterations):
		if (genotype() == 'AA'):
			AA += 1
		if (genotype() == 'Aa'):
			Aa += 1
		if (genotype() == 'aA'):
			Aa += 1
		if (genotype() == 'aa'):
			aa += 1

	print ("Counts: ", "\nAA:",AA,"\tAa:", Aa,"\taa:", aa) 
	# Counts - number of genotype in total number of genotypes produced (iterations)
	print ("\nPercentages:   ", "\nAA:",AA/iterations, "\tAa:",Aa/iterations, "\taa:",aa/iterations,"\n") # Percentages - the likelihood a genotype will be produced

test(100000) # In this line, 100000 represents the number of genotypes produced. 