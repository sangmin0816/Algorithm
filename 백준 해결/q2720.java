package d1114;

import java.util.*; 

public class q2720 { // 거스름돈
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스
        int[] QDNP={25, 10, 5, 1}; // 쿼터, 다임, 니켈, 페니

        for(int i=0; i<T; i++){
            int C = sc.nextInt(); // 거스름돈
            for(int j=0; j<4; j++){
                System.out.printf("%d ", C/QDNP[j]); // 동전 갯수
                if(C!=0)
                    C%=QDNP[j];
            }
            System.out.println();
        }
        sc.close();
    }
    
}