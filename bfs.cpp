#include<bits/stdc++.h>
using namespace std;

void bfs_shortestPath(int source, int destination, vector<vector<int>> &graph, vector<int> &dist, vector<int> &parent)
{
	queue<int> q;
	q.push(source);
	dist[source] = 0;
	parent[source] = -1;

	while(!q.empty())
	{
		int u = q.front();
		q.pop();

		for(int i : graph[u])
		{
			if(dist[i] == INT_MAX)
			{
				dist[i] = dist[u] + 1;
				parent[i] = u;
				q.push(i);

				if(i == destination) return;
			}
		}
	}
}

void printPath(int source, int destination, vector<int> &parent)
{
	vector<int> path;
	for(int node = destination; node != -1; node = parent[node])
		path.push_back(node);

	reverse(path.begin(), path.end());
	cout << "Path from " << source << " to " << destination << ":\n";
	for(int i: path)
		cout << i << " ";
	cout << endl;
}

int main()
{
	int nodes, edges;
	cout << "Enter the number of nodes: ";
	cin >> nodes;

	vector<vector<int>> graph(nodes);
	vector<int> dist(nodes, INT_MAX);
    vector<int> parent(nodes, -1);

	cout << "Enter the number of edges: ";
	cin >> edges;

	cout << "Enter the edges (u v) where there is an edge from node u to node v:\n";
	for(int i = 0; i < edges; ++i)
	{
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);  // assuming it's an undirected graph
	}

	int source, destination;
	cout << "Enter the source node: ";
	cin >> source;
	cout << "Enter the destination node: ";
	cin >> destination;

	bfs_shortestPath(source, destination, graph, dist, parent);
	printPath(source, destination, parent);

	return 0;
}
