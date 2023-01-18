package d220116;
import java.util.*;
public class q1817 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1817
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();

        int ans = 1;
        int now = 0;

        int books[] = new int[N];
        
        for(int i=0; i<N; i++) {
            books[i] = sc.nextInt();
            if((books[i]+now) <= M) now+=books[i];
            else{
                now=books[i];
                ans++;
            }
        }
        if(N==0){ // 이 경우 너무 쪼잔하다
            System.out.println(0);    
        }
        else System.out.println(ans);
        sc.close();
    }
}
