package d220109;

import java.util.*;

public class q5585 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/5585
        Scanner sc = new Scanner(System.in);

        int N = 1000 - sc.nextInt();

        int ans = 0;
        int changes[] = {500, 100, 50, 10, 5, 1};
        int i=0;

        while(N>0){
            ans+=N/changes[i];
            N%=changes[i];
            i++;
        }

        System.out.println(ans);

        sc.close();
    }
}
