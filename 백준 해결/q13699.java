package d220130;
import java.util.*;

public class q13699 { // https://www.acmicpc.net/problem/13699 점화식
    public static long arr[] = new long[36]; // double 소수점 때문에 부정확할 수 있음 주의!
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        arr[0]=1; arr[1] = 1;
        dp(n);

        System.out.println(arr[n]);

        sc.close();
    }

    public static void dp(int n){
        if(n==0 || n==1) {
            return;
        }
        for(int i=2; i<n+1; i++){
            for(int j=0; j<i; j++){
                arr[i]+=(arr[j]*arr[i-j-1]);
            }
        }
    }
}
