package c1124;
import java.util.*;

public class q17197 {
    public static int parent[];
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt()+1;
        int M = sc.nextInt()+1;
        parent = new int[N];
        int[][] coo = new int[N][2];
        
        for(int i=1; i<N; i++){
            coo[i][0]=sc.nextInt();
            coo[i][1]=sc.nextInt();
        }
            
        for(int i=1; i<M; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(Find(a)!=Find(b))
                Union(a, b);
        }

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
}
