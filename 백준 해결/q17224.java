package d220109;
import java.util.*;

public class q17224 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/17224
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int L = sc.nextInt();
        int K = sc.nextInt();
        int easy = 0;
        int diff = 0;
        int ans = 0;

        for(int i=0; i<N; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(a<=L) easy++;
            if(b<=L) diff++;
        }

        if(diff>=K) ans=140*K;
        else if(diff<K){
            if(K>easy) ans=140*diff+100*(easy-diff);
            else ans=140*diff+100*(K-diff);
        }

        System.out.println(ans);

        sc.close();
    }
}
