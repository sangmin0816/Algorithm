package 풀다만문제;


import java.util.*;

public class q2748 { // 계속 2% 대에서 틀림 왤까
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double ans = Fibonacci(n);
        System.out.printf("%.0f",ans);

        sc.close();
    }
    public static double Fibonacci(int n){
        if(n==0)
            return 0;
        else if(n==1)
            return 1;
        else{
            double f1=0, f2=1;
            for(int i=2; i<=n; i++){
                f2=f2+f1;
                f1=f2-f1;
            }
            return f2;
        }     
    }
}