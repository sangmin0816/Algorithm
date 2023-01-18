package 풀다만문제;

import java.util.*;

public class q15881 {
    public static int ans = 0;
    public static void main(String[] args) { // https://www.acmicpc.net/problem/15881 실패하는 이유를 모르겠음.
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        String ppap = sc.next();
        dp(ppap, N);
        System.out.println(ans);

        sc.close();
    }

    public static void dp(String ppap, int N){
        for(int i=0; i<N; i++){
            if(ppap.charAt(i)=='p'){
                i++;
                if(i<N && ppap.charAt(i)=='P'){
                    i++;
                    if(i<N && ppap.charAt(i)=='A'){
                        i++;
                        if(i<N && ppap.charAt(i)=='p'){
                            ans++;
                        }
                    }
                }
            }
        }
    }
}
