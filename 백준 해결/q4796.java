package d220130;
import java.util.*;

public class q4796 { // https://www.acmicpc.net/problem/4796 캠핑
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int i=1;
        while(true){
            int L = sc.nextInt();
            int P = sc.nextInt();
            int V = sc.nextInt();
            if(L==0 && P==0 && V==0) break;

            int ans = V/P*L;
            if(V%P>=L) ans+=L; // 이 부분에서 틀림. 그래도 생각보다 간단한 문제
            else ans+=V%P;

            System.out.printf("Case %d: %d\n", i, ans);

            i++;
        }

        sc.close();
    }   
}
