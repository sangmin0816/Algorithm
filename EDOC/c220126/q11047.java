package c220126;

import java.util.*; 
// 아니 이게 맞으면 안 될 것 같은데... 테스트 케이스가 잘못 되어있나...?? --> A_i+1이 배수라는 조건 있어서 가능
// K = 80, money = {1, 40, 45}

public class q11047 { // https://www.acmicpc.net/problem/11047 동전
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 동전 종류
        int K = sc.nextInt(); // 만들어야 하는 돈
        int money[] = new int[N]; // 동전 값 배열
        for(int i=0; i<N; i++) money[i] = sc.nextInt();

        int ans = 0;
        
        int i = N-1; // 가장 값이 큰 동전부터
        while(K>0){ 
            ans = ans + K/money[i]; // K를 동전[i]로 나누기
            K = K%money[i]; // K 값을 빼기
            i--; // 더 작은 동전으로
        }

        System.out.println(ans);
        sc.close();
    }
}