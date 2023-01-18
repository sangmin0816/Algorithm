package d1114;

import java.util.*;

public class q1434 { // 책 정리
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 상자 갯수
        int M = sc.nextInt(); // 책 갯수
        int A = 0; // 총 상자 크기
        int B = 0; // 총 책 크기

        for(int i=0; i<N; i++)
            A+=sc.nextInt();
        
        for(int i=0; i<M; i++)
            B+=sc.nextInt();

        // 박스 안에 책이 모두 들어간다는 조건이 있으므로 A-B로 간단히 해결 가능
        // 원한 건 아마 이게 아니였을 듯
        System.out.println(A-B);

        sc.close();
    }
}
