import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class NumberOfShortestPaths {

    static class Graph{
        public List<List<Integer>> adjList;
        int numVerices;

        Graph(int numVerices){
            this.numVerices = numVerices;
            adjList = new ArrayList<>(numVerices);
            for(int i = 0; i < numVerices; i++){
                adjList.add(new ArrayList<>());
            }
        }

        public void addEdge(int u, int v){
            adjList.get(u).add(v);
            adjList.get(v).add(u);
        }

    }
    
    public static int[] countShortestPaths(Graph graph, int source){
        int[] distance = new int[graph.numVerices]; // distance from source to all other vertices
        int[] pathCount = new int[graph.numVerices]; // number of shortest paths from source to all other vertices 
        Arrays.fill(distance, -1);                   // initially all distances are -1
        Queue<Integer> queue = new LinkedList<>();   // queue to perform BFS

        distance[source] = 0; // distance from source to source is 0
        pathCount[source] = 1; // number of shortest paths from source to source is 1
        queue.add(source);    // add source to queue

        int u = 0;  // current vertex
        while(queue.isEmpty() == false){
            u = queue.poll(); // remove the front of the queue
            for(int v : graph.adjList.get(u)){
                if(distance[v] == -1){ // if v is not visited
                    distance[v] = distance[u] + 1; // distance from source to v is distance from source to u + 1
                    pathCount[v] = pathCount[u]; // number of shortest paths from source to v is number of shortest paths from source to u
                    queue.add(v); // add v to queue
                }else if(distance[v] == distance[u] + 1){ // if v is visited and distance from source to v is distance from source to u + 1
                    pathCount[v] += pathCount[u]; // number of shortest paths from source to v is incremented by number of shortest paths from source to u
                }
            }
        }

        return pathCount;

    }

    public static void main(String[] args) {
        // Your code here
    }
}
