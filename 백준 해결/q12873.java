package d220102;

import java.util.*;

public class q12873 {
    public static void main(String[] args) { // 막대기 https://www.acmicpc.net/problem/17608
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int arr[] = new int[N];
        for(int i=0; i<N; i++)
            arr[i]=sc.nextInt();
        
        int ans = 1;
        int standard = arr[N-1];
        for(int i=N-2; i>=0; i--){
            if(arr[i]>standard){
                ans++;
                standard=arr[i];
            }
        }

        System.out.println(ans);

        sc.close();
    }
}
