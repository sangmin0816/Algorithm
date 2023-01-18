package d1114;

import java.util.*; 

public class q14487 { // 욱제는 효도쟁이야
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); // 섬 갯수
        int[] v = new int[n]; // 이동 비용
        int ans = 0; // 최소 이동 비용

        for(int i=0; i<n; i++)
            v[i]=sc.nextInt();

        Arrays.sort(v); 
        // 원형의 길에서 좌우로만 이동한다면, 최소 이동거리는 최대 이동 길을 뺀 나머지 거리 합

        for(int i=0; i<n-1; i++) // 가장 비용이 큰 길 제외하고 더함
            ans+=v[i];

        System.out.println(ans);

        sc.close();
    }
}
