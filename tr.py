
def tr(G):						# Transpose (rev. edges of) G
	GT = {}
	for u in G: GT[u] = set()	# Get all the nodes in there
	for u in G:
		for v in G[u]:
			GT[v].add(u)		# Add all reverse edges
	return GT