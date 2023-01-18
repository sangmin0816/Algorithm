package 풀다만문제;
import java.util.*;

public class q12981 { // https://www.acmicpc.net/problem/12981
    public static void main(String[] args) { // 계속 틀리는데 솔직히 모르겠음
        Scanner sc = new Scanner(System.in);

        int R = sc.nextInt();
        int G = sc.nextInt();
        int B = sc.nextInt();

        int ans = R/3 + G/3 + B/3;
        R = R%3; 
        G = G%3; 
        B = B%3;

        while(R>0 && G>0 && B>0) {
            ans++; R--; G--; B--;
        }
        ans = ans + (R+2)/3 + (G+2)/3 + (B+2)/3;

        System.out.println(ans);
        sc.close();
    }
}
