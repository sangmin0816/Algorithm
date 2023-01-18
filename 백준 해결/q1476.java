package d220123;
import java.util.*;
public class q1476 { // 단순한 게 짱이야
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int E = sc.nextInt();
        int S = sc.nextInt();
        int M = sc.nextInt();

        int ans = 1;

        int e=1, s=1, m=1; 
        while(!(e==E&&s==S&&m==M)){
            ans++;
            if(e>=15) e=0;
            if(s>=28) s=0;
            if(m>=19) m=0;
            e++; s++; m++;
        }

        System.out.println(ans);

        sc.close();
    }
}
