#include <iostream>
#include <vector>
#include <limits>
#include <cmath>
using namespace std;
const int V = 7;
const double INF = numeric_limits<double>::infinity();
struct Location
{
    string name;
    double lat, lon;
};
double euclideanDistance(double lat1, double lon1, double lat2, double lon2)
{
    return sqrt(pow(lat2 - lat1, 2) + pow(lon2 - lon1, 2));
}
void bellmanFord(vector<vector<double>> &graph, int source)
{
    vector<double> dist(V, INF);
    dist[source] = 0;
    for (int i = 0; i < V - 1; ++i)
    {
        for (int u = 0; u < V; ++u)
        {
            for (int v = 0; v < V; ++v)
            {
                if (graph[u][v] != INF && dist[u] + graph[u][v] < dist[v])
                {
                    dist[v] = dist[u] + graph[u][v];
                }
            }
        }
    }
    for (int u = 0; u < V; ++u)
    {
        for (int v = 0; v < V; ++v)
        {
            if (graph[u][v] != INF && dist[u] + graph[u][v] < dist[v])
            {
                cout << "Graph contains negative weight cycle!" << endl;
                return;
            }
        }
    }
    cout << "\nShortest distances from Zero Mile (Node " << source << "):\n";
    for (int i = 0; i < V; ++i)
    {
        cout << "To Node " << i << ": " << dist[i] << " units\n";
    }
}
int main()
{
    vector<Location> locations = {
        {"Zero Mile", 21.1480, 79.1010},
        {"Nagpur Railway Station", 21.1500, 79.0849},
        {"Sitabuldi Fort", 21.1498, 79.0906},
        {"Ambazari Lake", 21.1283, 79.0416},
        {"MIHAN IT Park", 21.0380, 79.0241},
        {"Nagpur Airport", 21.0922, 79.0472},
        {"Seminary Hills", 21.1705, 79.0705}};
    vector<vector<double>> graph(V, vector<double>(V, INF));
    for (int i = 0; i < V; ++i)
    {
        for (int j = 0; j < V; ++j)
        {
            if (i != j)
            {
                graph[i][j] = euclideanDistance(locations[i].lat, locations[i].lon,

                                                locations[j].lat, locations[j].lon);
            }
            else
            {
                graph[i][j] = 0;
            }
        }
    }
    bellmanFord(graph, 0);
    return 0;
}
