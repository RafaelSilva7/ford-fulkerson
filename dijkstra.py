from heapq import heappush, heappop
inf = float('inf')

def dijkstra(G,s):
	D, P, Q, S = {s:0}, {}, [(0,s)], set()
	while Q:
		_, u = heappop(Q)
		if u in S: continue
		S.add(u)
		for v in G[u]:
			relax(G, u, v, D, P)
			heappush(Q, (D[v], v))
	return D, P


def relax(W, u, v, D, P):
	d = D.get(u,inf) + W[u][v]
	if d < D.get(v,inf):
		D[v], P[v] = d, u 
		return True