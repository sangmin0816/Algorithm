package d220109;

import java.util.*;

public class q22864 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/22864
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int M = sc.nextInt();

        if(A>M){
            System.out.println(0);
            System.exit(0);
        }

        int ans = 0;
        int fatigue = 0;

        for(int i=0; i<24; i++){
            if(fatigue+A>M){
                fatigue-=C;
                if(fatigue<0)   fatigue=0;
            }
            else {
                fatigue+=A;
                ans+=B;
            }
        }

        System.out.println(ans);

        sc.close();
    }
}
