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
import java.util.Arrays;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main5 {

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
        public int match(int [] M,int[] W,int k) {
        Arrays.sort(M);
        Arrays.sort(W);
        int i = 0, j = 0, matches = 0;

        while (i < M.length && j < W.length) {
            if (Math.abs(M[i] - W[j]) <= k) {
                // Found a match
                matches++;
                i++;
                j++;
            } else if (M[i] < W[j]) {
                // Move to the next man
                i++;
            } else {
                // Move to the next woman
                j++;
            }
        }
        return matches;
        } 
        
        public void solve(InputReader in, PrintWriter out) {
            int n = in.nextInt();
            int k = in.nextInt();
            int[] M = new int[n];
            int[] W = new int[n];
            for (int i = 0 ; i < n ; i++)
                M[i] = in.nextInt();
            for (int i = 0 ; i < n ; i++)
                W[i] = in.nextInt();                
            int maxMatch = match(M,W,k);
            out.println(maxMatch);            
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