package d220123;
import java.util.*;

public class q1292 { // 무식한게 정답이다.
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1292
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt();
        int B = sc.nextInt();
        int ans = 0;

        int arr[] = new int[1001];
        int x = 1;
        int y = 1;
        for(int i=1; i<B+1; i++){
            arr[i]=x;
            if(x==y){
                x++;
                y=0;
            }
            y++;
        }
        
        for(int i=A; i<B+1; i++) ans+=arr[i];
        System.out.println(ans);

        sc.close();
    }
}


/*
int A = sc.nextInt();
        int B = sc.nextInt();
        int ans = 0;

        int ax = (int)Math.sqrt(2*A);
        
        int ay = 0;
        if(ax!=1) ay = ax*(ax-1)/2;
        ay = A-ay;

        int x = ax;
        int y = ay;
        
        for(int i=0; i<=B-A; i++){
            ans+=x;
            if(x==y){
                x++;
                y=0;
            }
            y++;
        }

        System.out.println(ans);

*/