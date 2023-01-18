package c1117;
// 동아리 문제 (선택 여부는 아직 모름)
import java.util.*;

public class q11256 { // 사탕 acmicpc.net/problem/11256
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스
        for(int i=0; i<T; i++){
            int J = sc.nextInt(); // 사탕 갯수
            int N = sc.nextInt(); // 상자 갯수
            int[] arr = new int[N];
            int ans = 0;

            for(int j=0; j<N; j++){
                //상자 가로 세로 크기
                int R = sc.nextInt();
                int C = sc.nextInt();
                arr[j]=R*C; // 각 상자별 넓이를 배열에 추가
            }
            
            Arrays.sort(arr); // 오름차순 정렬
            
            for(int j=N-1; j>=0; j--){ // 넓이가 큰 상자부터 집어넣기
                J-=arr[j];
                ans++;
                if(J<=0){
                    System.out.println(ans);
                    break;
                }
            }
        }

        sc.close();
    }
}

// 어려웠던 점. 문제 이해를 못해서 각 상자별로 N개씩 주어지는 줄 알았다.