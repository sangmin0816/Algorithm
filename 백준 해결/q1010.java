package d220116;
import java.util.*;

public class q1010 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1010 다리놓기
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int t=0; t<T; t++){
            int M = sc.nextInt();
            int N = sc.nextInt();

            int den = 1;
            int num = 1;

            for(int i=N; i>(N-M); i--){
                num=num*i/den;
                den++;
            }

            System.out.println(num);
        }
        
        sc.close();
    }    
}
