package 풀다만문제;
import java.util.*;
public class q2891 { // 80퍼 정도에서 틀림
    public static void main(String[] args) { // https://www.acmicpc.net/problem/2891
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int S = sc.nextInt();
        int R = sc.nextInt();

        int kayak[] = new int[N+2];
        for(int i=0; i<S; i++) kayak[sc.nextInt()]--;
        for(int i=0; i<R; i++) {
            int remain = sc.nextInt();
            if(kayak[remain-1]==-1) {
                S--;
                kayak[remain-1]=0;
            }
            else if(kayak[remain+1]==-1) {
                S--;
                kayak[remain+1]=0;
            }
        }

        System.out.println(S);

        sc.close();
    }
}
