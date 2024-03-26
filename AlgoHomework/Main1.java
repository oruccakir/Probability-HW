import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.InputStream;
import java.util.*;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main1 {

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


        public int[] numberOfShortestPaths(List<List<Integer>> adjList,int source) {
            int[] distance = new int[adjList.size()]; // distance from source to all other vertices
            int[] pathCount = new int[adjList.size()]; // number of shortest paths from source to all other vertices 
            Arrays.fill(distance, -1);                   // initially all distances are -1
            Queue<Integer> queue = new LinkedList<>();   // queue to perform BFS

            distance[source] = 0; // distance from source to source is 0
            pathCount[source] = 1; // number of shortest paths from source to source is 1
            queue.add(source);    // add source to queue

            int u = 0;  // current vertex
            while(queue.isEmpty() == false){
                u = queue.poll(); // remove the front of the queue
                for(int v : adjList.get(u)){
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

        public void solve(InputReader in, PrintWriter out) {

            int n = in.nextInt();
            int m = in.nextInt();
    
            // Initialize the adjacency list
            List<List<Integer>> adj = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                adj.add(new ArrayList<>());
            }
    
            // Read m lines with u and v, and construct the adjacency list
            for (int i = 0; i < m; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                u--;
                v--;
                adj.get(u).add(v);
                adj.get(v).add(u);
            }

            int s = in.nextInt();
            s--;

            int[] costs = numberOfShortestPaths(adj,s);

            for (int i = 0 ; i < costs.length ; i++) {
                System.out.print(costs[i] + " ");
            }
            System.out.println();
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