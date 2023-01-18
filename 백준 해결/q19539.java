package d1121;
import java.util.*;

public class q19539 { // 수정 필요
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt(); 
        Integer[] h = new Integer[N]; 
        int sum=0;

        for(int i=0; i<N; i++) {
            h[i]=sc.nextInt();
            sum+=h[i];
        }
        
        if(sum%3!=0){
            System.out.println("NO");
            System.exit(0);
        }

        int res = 0;
        for(int i=0; i<N; i++){
            res = (h[i] + res)%3;
        }

        if(res==0)
            System.out.println("YES");
        else
            System.out.println("NO");

        sc.close();
    }
}
