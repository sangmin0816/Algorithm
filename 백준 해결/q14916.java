package d220116;
import java.util.*;
public class q14916 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // https://www.acmicpc.net/problem/14916 거스름돈

        int n = sc.nextInt();

        int five = n/5;
        
        while(five>=0){
            int two = (n-five*5)/2;
            if(five*5+two*2==n){
                System.out.println(five+two);
                System.exit(0);
            }
            five--;
        }
        System.out.println(-1);

        sc.close();
    }
}
