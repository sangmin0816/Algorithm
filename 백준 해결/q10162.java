package d1114;
import java.util.*; 

public class q10162 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt(); // 요리 시간
        int[] ABC = {300, 60, 10}; // 시간조절 버튼
        int [] ans = new int[3];

        if(T%10!=0) // 시간 정확히 맞출 수 없는 경우
            System.out.println(-1);
        else{
            int i=0;
            while(T!=0){ // 최소 버튼 조작
                ans[i]=T/ABC[i];
                T%=ABC[i];
                i++;
            }
            System.out.printf("%d %d %d", ans[0], ans[1], ans[2]);
        }
        sc.close();
    }
}

// 어려운 점: A의 5분을 5초로 잘못봐서 한참을 고쳤다.