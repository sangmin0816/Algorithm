package 풀다만문제;
import java.util.*;

public class q8394 { // 피보나치로 푸는 문제라고 한다... 흑흑
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double ans = 0;

        if(n==2) ans = 1;
        else{
            int prev = 1;
            int now = 2;
            for(int i=2; i<n; i++){
                now=now+prev;
                prev=now-prev;
            }
            ans=now;
        }

        System.out.println(ans%10);

        sc.close();
    }   
}
