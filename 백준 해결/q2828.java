package d1121;
import java.util.*;

public class q2828 {
    public static void main(String[] args) { // https://www.acmicpc.net/submit/2828/35617397
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt()-1;
        int J = sc.nextInt();
        int ans = 0;
        
        int lp = 1;
        int rp = lp+M;

        for(int i=0; i<J; i++){
            int apple = sc.nextInt();
            if(apple<=rp && apple>=lp)
                continue;
            if(Math.abs(apple-lp)<Math.abs(apple-rp)){
                ans+=Math.abs(apple-lp);
                rp+=apple-lp;
                lp+=apple-lp; // lp 먼저 대입하면 rp 값에 영향 주니 뒤로 주의
            }
            else{
                ans+=Math.abs(apple-rp);
                lp+=(apple-rp);
                rp+=(apple-rp);
            }
        }
        
        System.out.println(ans);
        sc.close();
    }
}
