package d220102;
import java.util.*;

public class q1246 { //https://www.acmicpc.net/problem/1246 온라인 판매
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int P[] = new int[M];
        int PCost[] = new int[M];

        for(int i=0; i<M; i++){
            P[i]=sc.nextInt();
        }

        Arrays.sort(P);
        
        if(M<N) N=M;

        int max=0;
        int index = M;
        for(int i=M-N, j=N; i<M; i++){
            PCost[i]=j*P[i];
            if(PCost[i]>max){
                max=PCost[i];
                index = i;
            }
            j--;
        }

        System.out.printf("%d %d", P[index], PCost[index]);

        sc.close();
    }
}
