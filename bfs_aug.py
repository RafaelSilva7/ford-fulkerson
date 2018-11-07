from collections import deque
inf = float('inf')

def bfsAug(G, H, s, t, f):
	P, Q, F = {s: None}, deque([s]), {s: inf}	#Tree, queue, flow label
	def label(inc):								# Flow increase at v from u?
		if v in P or inc <= 0: return 			# Seen? Unreachable? Ignore
		F[v], P[v] = min(F[u], inc), u 			# Max flow here? From where?
		Q.append(v)								# Discovered -- visit later
	while Q:									# Discovered, unvisited
		u = Q.popleft()							# Get one (FIFO)
		if u == t: return P, F[t]				# Reached t? Augmenting path!
		try:
			for v in G[u]: label(G[u][v] - f[u,v])	# Label along out-edges
			for v in H[u]: label(f[v,u])			# Label along in-edges
		except Exception as e:
			raise e
	return None, 0								# No augmenting path found

