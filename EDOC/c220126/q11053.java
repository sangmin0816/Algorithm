package c220126;

import java.util.*;

public class q11053 { // https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 수열 크기
        int arr[] = new int[N]; // 수열 배열
        for(int i=0; i<N; i++) arr[i] = sc.nextInt();

        int dparr[] = new int[N]; // 수열 길이(원래는 1로 초기화 해야하지만 그냥 마지막에 1 더해주는 걸로)

        for(int i=1; i<N; i++){ // 수열 배열을 돌면서
            for(int j=i; j>=0; j--){ // 수열 i 이전 수열에서
                if(arr[i]>arr[j]){ // i보다 작은 값이 있다면
                    if(dparr[i]<dparr[j]+1) dparr[i]=dparr[j]+1; // 수열 i의 길이와 수열 j의 길이+1 중 더 큰 값을 수열 i에 대입
                }
            }
        }   

        Arrays.sort(dparr); // 수열 길이를 오름차순 정렬하여 가장 큰 마지막 값

        System.out.println(dparr[N-1]+1); // 기본적으로 수열 길이는 1보다 큰 값이므로 1을 더해줌

        sc.close();
    }
}
