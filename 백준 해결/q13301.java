package d220102;
import java.util.*;

public class q13301 { // 타일 장식물 https://www.acmicpc.net/problem/13301
    public static long W=1, H=1;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        dp(N);
        long ans=2*(W+H);
        System.out.println(ans);
        sc.close();
    }
    public static void dp(int N){
        for(int i=1; i<N; i++){
            W+=H;
            H=W-H;
        }
    }
}

// long은 되고, double은 안 됐다. 오차 범위가 있어서 였을까? 어쨌든 long으로 해서 정수형 64비트를 써봤다.