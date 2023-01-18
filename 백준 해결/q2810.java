package d1114;

import java.util.*; 

public class q2810 { // 컵홀더
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt(); // 좌석 수
        String seats = sc.next();
        int L = 0;

        char[] seatC = seats.toCharArray();
        Arrays.sort(seatC); // L->S 순으로 정렬

        while(seatC[L]=='L'){
            L++; // L의 갯수
        }

        int S = N-L; // S의 갯수
        L/=2; // 커플석은 좌석 하나와 마찬가지

        if(N>L+S+1) // 컵홀더 갯수 = 좌석수(커플석은 /2) + 1
            System.out.println(L+S+1);
        else
            System.out.println(N); // 컵홀더 갯수 넉넉할 때

        sc.close();
    }
}
