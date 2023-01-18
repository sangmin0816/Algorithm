package d1114;

import java.util.*; 

public class q14471 { // 포인트 카드
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 경품 위한 최소 갯수
        int M = sc.nextInt(); // 카드 갯수
        ArrayList<Integer> lacks = new ArrayList<Integer>(); // 부족한 카드의 당첨 갯수
        int win = 0; // 경품 갯수
        int ans = 0; // 필요한 돈
        
        for(int i=0; i<M; i++){
            int A=sc.nextInt(); // 당첨 갯수
            int B = sc.nextInt(); // A+B=N이므로 사실 필요 없음
            if(A>=N || B<=N){ // 당첨 갯수 충족 시 경품 획득
                win++;
                continue;
            }
            lacks.add(A); // 당첨 갯수 미달 시 lacks에 추가
        }

        if(win<M-1){ // 경품 갯수가 모자라면
            Collections.sort(lacks, Collections.reverseOrder()); // 내림차순 정렬
            while(win<M-1){
                int lacksi = lacks.remove(0); // 당첨 많은 순으로 pop
                ans+=(N-lacksi); // N까지 필요한 돈 더하기
                win++; // 경품 추가
            }
        }

        System.out.println(ans);

        sc.close();
    }
}

// 어려웠던 점: Arrayslist는 Array.sort가 아닌 Collections.sort를 써야 한다.