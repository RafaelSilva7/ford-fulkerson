from collections import defaultdict
from tr import tr
from bfs_aug import bfsAug

def fordFulkerson(G, s, t, aug=bfsAug):	# Max flow s to t
	H, f = tr(G), defaultdict(int)			# Transpose and flow
	while True:								# While we can improve things
		P, c = aug(G, H, s, t, f)			# Aug. path and capacity/slack
		#print('p', P, 'c', c)
		if c == 0: return f 				# No augm. path found? Done!
		u = t 								# Start augmentation
		while u != s:						# Backtrack to s
			u, v = P[u], u 					# Shift on step
			if v in G[u]:	f[u,v] += c 	# Forward edge? Add slack
			else:			f[v,u] -= c 	# Backward edge? Cancel slack