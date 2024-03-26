import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.io.BufferedReader;
import java.util.Comparator;
import java.io.InputStream;
import java.util.*;

import java.util.ArrayList;
import java.util.List;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main4 {

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(in, out);
        out.close();
    }
 
    static class TaskA {


        static class Pair {
            int node;
            int cost;
    
            Pair(int node, int cost) {
                this.node = node;
                this.cost = cost;
            }
        }

        public long shortestPath(List<List<Pair>> graph, int source, int dest) {
            int n = graph.size(); // Number of nodes in the graph
            long[] dist = new long[n]; // Array to store the shortest distance from source to each node
            Arrays.fill(dist,Long.MAX_VALUE); // Initialize the distance to all nodes to infinity
            dist[source] = 0; // The distance from source to itself is 0

            // Priority queue to store the nodes to visit
            PriorityQueue<Pair> pq = new PriorityQueue<>(Comparator.comparingLong(p -> p.cost));
            pq.add(new Pair(source, 0)); // Add the source node to the priority queue
            /* 
            
            for(int i=0; i<graph.size(); i++){
                for(int j=0; j<graph.get(i).size(); j++){
                    pq.add(new Pair(i, graph.get(i).get(j).cost));
            }
            */
            Pair p; // Current node
            int vertex  = 0; // Current vertex
            int neigh = 0; // Neighbor of the current vertex
            int weight = 0; // Weight of the edge between the current vertex and its neighbor
            while(!pq.isEmpty()){
                p = pq.poll(); // Get the node with the smallest distance
                vertex = p.node; // Get the vertex of the node
                if(vertex == dest) 
                    return dist[vertex]; // If we reached the destination, return the distance
                for(Pair pair : graph.get(vertex)){
                    neigh = pair.node; // Get the neighbor of the vertex
                    weight = pair.cost; // Get the weight of the edge between the vertex and its neighbor
                    if(dist[vertex] + weight < dist[neigh]){
                        dist[neigh] = dist[vertex] + weight; // Update the distance to the neighbor
                        pq.add(new Pair(neigh, (int)dist[neigh])); // Add the neighbor to the priority queue
                    }
                }

            }
            // Your solution here
            return -1; //If there is no path from s to t.
        }

        public void solve(InputReader in, PrintWriter out) {

            int n = in.nextInt();
            int m = in.nextInt();
    
            // Initialize the adjacency list with pairs (node, cost)
            List<List<Pair>> adj = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                adj.add(new ArrayList<>());
            }
    
            // Read m lines with u, v, and cost, and construct the adjacency list
            for (int i = 0; i < m; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                u--;
                v--;
                int cost = in.nextInt(); // Assuming the cost of the edge is given
                adj.get(u).add(new Pair(v, cost)); // Assuming the graph is directed
            }
    
            // Now you can call shortestPath with the adjacency list and source and target nodes
            // For example:
            int s = in.nextInt();
            int t = in.nextInt();
            s--;
            t--;
            long shortestPathCost = shortestPath(adj, s, t);
            System.out.println(shortestPathCost);
        }

    }
 
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;
 
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
 
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

 
        public int nextInt() {
            return Integer.parseInt(next());
        }
 
        public long nextLong() {
            return Long.parseLong(next());
        }
 

    }
}