
package 풀다만문제;
import java.util.*;
import java.lang.*;

public class q2729 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=0; i<T; i++){
            String A = sc.next();
            String B = sc.next();
            
            if(A.length()>B.length())sumall(A, B);
            else sumall(B, A);

            System.out.printf("\n");
        }

        sc.close();
    }

    public static void sumall(String big, String small){
        ArrayList<Character> sumAB = new ArrayList<Character>();
        int up = 0;
        for(int j=small.length()-1;j>=0; j--){
            int smalli = small.charAt(j) - '0';
            int bigi = big.charAt(j) - '0';
            switch(smalli+bigi+up){
                case 2:
                    sumAB.add('0');
                    up=1;
                    break;
                case 3:
                    sumAB.add('1');
                    up=0;
                    break;
                default:
                    char temp = (char)(smalli + bigi + up) ;
                    sumAB.add(temp);
            }
        }
        for(int j=small.length(); j<big.length(); j++) sumAB.add(big.charAt(j));
        while(!sumAB.isEmpty()) {
            System.out.print(sumAB.remove(0));
        }
    }
}
