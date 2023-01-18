package 풀다만문제;
import java.util.*;

public class q1059 { // https://www.acmicpc.net/problem/1059 1퍼에서 막힘 아니 왜
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int L = sc.nextInt();
        int set[] = new int[L+1];
        for(int i=0; i<L; i++) set[i]=sc.nextInt();
        int n = sc.nextInt();

        if(Arrays.binarySearch(set, n)>=0){
            System.out.println(0);
            System.exit(0);
        }

        set[L]=n;
        Arrays.sort(set);

        int index = Arrays.binarySearch(set, n);
        
        int prev = 1;
        if(index!=0) prev = set[index-1];
        int next = set[index+1];

        int ans = (n-prev-1)*(next-n) + (next-n-1);

        System.out.println(ans);
        

        sc.close();
    }
}
