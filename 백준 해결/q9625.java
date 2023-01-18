package d220102;

import java.util.*;

public class q9625 { // BABBA https://www.acmicpc.net/problem/9625
    public static int A=1, B=0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();
        dp(K);
        System.out.printf("%d %d\n", A, B);
        sc.close();
    }

    public static void dp(int K){
        for(int i=0; i<K; i++){
            B=B+A;
            A=B-A;
        }
    }
}