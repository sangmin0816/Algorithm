package d220123;
import java.util.*;
public class q2609 { // https://www.acmicpc.net/problem/2609
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        int gcommonfactor = 1;

        int minnum = A;
        if(A>B) minnum = B;

        for(int i=1; i<=minnum; i++){
            if((A%i==0)&&(B%i==0)) gcommonfactor = i;
        }

        int lcommonmultiple = gcommonfactor*(A/gcommonfactor)*(B/gcommonfactor);

        System.out.printf("%d\n%d", gcommonfactor, lcommonmultiple);

        sc.close();
    }
}
