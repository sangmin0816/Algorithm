package d220123;
import java.util.*;
public class q1312 { // 무식한게 답이다.
    public static void main(String[] args) { //https://www.acmicpc.net/problem/1312
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int N = sc.nextInt();
        
        for(int i=0; i<N-1; i++){
            A*=10;
            A=A%B;
        }

        System.out.println((A*10/B)%10);

        sc.close();
    }
}
