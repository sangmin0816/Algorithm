package d220102;
import java.util.*;

public class q1417 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1417
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt()-1; // 후보의 수
        int Nvotes[] = new int[N];
        int dasom = sc.nextInt();
        for(int i=0; i<N; i++) Nvotes[i]=sc.nextInt();
        int ans = 0;

        Arrays.sort(Nvotes);

        while(N!=0 && dasom<=Nvotes[N-1]){
            Nvotes[N-1]--;
            dasom++;
            ans++;
            Arrays.sort(Nvotes);
        }

        System.out.println(ans);

        sc.close();
    }
}
