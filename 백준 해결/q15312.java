package d220102;

import java.util.*;

public class q15312 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String A = sc.next();
        String B = sc.next();

        int alp[] = {3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1};

        int AB[] = new int[A.length()*2];
        for(int i=0; i<A.length(); i++){
            AB[2*i]=alp[(int)A.charAt(i)-'A'];
            AB[2*i+1]=alp[(int)B.charAt(i)-'A'];
        }

        dp(AB);
        System.out.printf("%d%d", AB[0], AB[1]);

        sc.close();
    }

    public static void dp(int AB[]){
        for(int i=AB.length-1; i>1; i--){
            for(int j=0; j<i; j++){
                AB[j]=(AB[j]+AB[j+1])%10;
            }
        }
    }
}
