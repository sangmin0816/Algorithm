package d220109;
import java.util.*;

public class q14659 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/14659
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int peaks[] = new int[N];
        for(int i=0; i<N; i++) peaks[i]=sc.nextInt();

        int high = 0;
        int cnt=0;
        int max = 0;

        for(int i=0; i<N; i++){
            if(peaks[i]>high){
                high=peaks[i];
                cnt=0;
            }
            else    cnt++;
            if(cnt>max)    max=cnt;
        }

        System.out.println(max);

        sc.close();
    }
}
