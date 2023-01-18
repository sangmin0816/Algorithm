package d1121;
import java.util.*;

public class q9237 { // 이장님 초대 https://www.acmicpc.net/problem/9237
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt(); // 묘목 갯수
        Integer[] t = new Integer[N]; // 묘목별 자라는 시간(0이 되어야 다 자람)
        int ans = 1; // 첫날부터 심음

        for(int i=0; i<N; i++) t[i]=sc.nextInt();        
        Arrays.sort(t, Collections.reverseOrder()); // 내림차순으로 시간 배열 정렬

        // 오래 걸리는 묘목부터 심어야 함
        // 하루에 하나씩 심으므로 i번째 묘목은 t[i]+i+1 소요. +1하여 0으로 맞춰줌
        for(int i=0; i<N; i++) t[i]+=(i+1);
        Arrays.sort(t, Collections.reverseOrder()); // 내림차순 시간 배열 정렬

        ans+=t[0]; // 가장 오래 걸리는 값이 답

        System.out.println(ans);
        sc.close();
    }
}

// Arrays.sort(int[], Collections.reverseOrder());에서 int는 Integer[] 배열이어야 한다.