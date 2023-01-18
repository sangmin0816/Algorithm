package c1117;
import java.util.*;

class Edge{
    int A;
    int B;
    int C;
}

public class q1197 { // https://www.acmicpc.net/problem/1197 동아리
    public static int parent[];
    public static double ans = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int V = sc.nextInt();
        int E = sc.nextInt();
        
        ArrayList<Edge> graph = new ArrayList<Edge>();
        parent = new int[V+1];

        for(int i=0; i<E; i++){
            Edge temp = new Edge();
            temp.A = sc.nextInt();
            temp.B = sc.nextInt();
            temp.C = sc.nextInt();
            graph.add(temp);
        }

        kruskal(graph, V, E);

        System.out.printf("%.0f", ans);

        sc.close();   
    }

    static int Find(int C){
        if(parent[C]==0)
            return C;
        return Find(parent[C]); 
    }

    static void Union(int A, int B){
        int rootA = Find(A);
        int rootB = Find(B);
        if(rootA!=rootB)
            parent[rootA]=rootB;
    }

    static void kruskal(ArrayList<Edge> graph, int V, int E){
        int edge_accepted = 0;
        int uset, vset;
        Edge temp = new Edge();
        Comparator<Edge> wComparator = new Comparator<Edge>() {
            public int compare(Edge e1, Edge e2){
                return e1.C-e2.C;
            }
        };
        Collections.sort(graph, wComparator);

        int i=0;
        while(edge_accepted < E-1){
            temp=graph.get(i);
            uset = Find(temp.A);
            vset = Find(temp.B);
            if(uset!=vset){
                edge_accepted++;
                ans+=temp.C;
                Union(uset, vset);
            }
            i++;
        }
    }
}
