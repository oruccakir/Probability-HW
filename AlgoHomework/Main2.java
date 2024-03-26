import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.InputStream;
import java.util.*;

import javax.swing.text.html.StyleSheet;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main2 {

    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskA solver = new TaskA();
        solver.solve(in, out);
        out.close();
    }

    static class Node{
        public int data;
        public Node parent;
        public boolean visited;
        public ArrayList<Node> children;
        public int discoveryTime;
        public ArrayList<Node> adjList;
        public Node(int data){
            this.data = data;
            this.visited = false;
            this.children = new ArrayList<>();
            this.adjList = new ArrayList<>();
        }
        
        public String toString(){
            /*
            String string = "Node data" + this.data;
            if(parent == null)
                string += " Parent null "+"\n";
            else
                string += " Parent "+ parent.data +"\n";

            
            StringBuilder str = new StringBuilder();
            for (Node child : children)
                str.append(" "+child.data);
                
            return string + str.toString()+"\n";
            */
            String str = "";
            str += data+" Adjs ";
            for(Node v: adjList)
                str += " "+v.data;
            return str;
        }
        

    }
 
    static class TaskA {


        public int[] articulationPoints(List<List<Integer>> adj) {
            List<Node> adjL = new ArrayList<>();
            Node z  = null;
            Node y = null;
            for(int i=0; i<adj.size(); i++){
                z = new Node(i+1);
                adjL.add(z);
                for (int j = 0; j < adj.get(i).size(); j++) {
                    y = new Node(adj.get(i).get(j)+1);
                    adjL.get(i).adjList.add(y);
                }
                for(int k=0; k<z.adjList.size(); k++){
                    z.adjList.get(k).adjList.add(z);
                }
                
            }


            // Tarjan's algorithm to find articulation points in a graph
            boolean[] visited = new boolean[adj.size()];    // visited[i] = true if i has been visited
            int[] discoveryTime = new int[adj.size()];      // discoveryTime[i] = discovery time of vertex i
            int[] low = new int[adj.size()];                // low[i] = low[i] = min(discoveryTime[j]) where j is a descendant of i
            int[] parent = new int[adj.size()];
            Arrays.fill(parent, -1);                                    // initially all vertices have no parent
            PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o.data)); // priority queue to store articulation points
            int time = 0; 
            Node u = null;                                      // time variable to store discovery time
            Stack<Node> stack = new Stack<>();                    // stack to store vertices in current DFS
            int children = 0;                                        // number of children of a vertex
            boolean isFound = false;
            Node newNode = null;
            for(int i=0; i<adjL.size(); i++){
                newNode = adjL.get(i);
                if(newNode.visited == false){
                    stack = new Stack<>();
                    stack.push(newNode);
                    while(stack.isEmpty() == false){
                        u = stack.peek();
                        if(u.visited == false){
                            u.visited = true;
                            System.out.println("Disc"+ u.data);
                        }
                        isFound = false;
                        for(Node v : u.adjList){
                            if(v.visited == false){
                                stack.push(v);
                                u.children.add(v);
                                v.parent = u;
                                isFound = true;
                                v.visited = true;
                                break;
                            }
                        }

                        if(isFound == false){
                            stack.pop();                    
                        }
                } 
                
            }
        }

            for(Node e : adjL){
                if(e.parent == null && e.children.size()>1)
                    pq.add(e);
                else if(e.parent != null) {
                    for(Node g : e.children){
                        if(g.adjList.contains(e.parent) == false){
                            pq.add(e);
                            break;
                        }
                    }
                }
   
            }

            int[] articPoints = new int[pq.size()];
            for(int i=0; i<articPoints.length; i++){
                articPoints[i] = pq.poll().data;
            }
            // Your solution here
            return articPoints; //return your articulation points sorted in ascending order.
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

            int[] points = articulationPoints(adj);

            System.out.println(points.length);
            for (int i = 0 ; i < points.length ; i++) {
                System.out.print((points[i] + 1) + " ");
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