package d1114;

import java.util.*; 

public class q2930 { // 가위바위보
    public static int score(char A, char B){ // 점수 계산
        if(A==B)
            return 1;
        switch(A){
            case 'R':
                if(B=='S')
                    return 2;
                else
                    return 0;
            case 'S':
                if(B=='R')
                    return 0;
                else
                    return 2;
            case 'P':
                if(B=='R')
                    return 2;
                else
                    return 0;
        }
        return -1;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int R = sc.nextInt(); // 라운드
        String roundS = sc.next(); // 상근이 픽
        int N = sc.nextInt(); // 친구 수
        String[] roundF = new String[N]; // 친구 픽
        int ans=0; // 상근이 픽 결과
        int maxans=0; // best 픽 결과

        for(int i=0; i<N; i++){
            roundF[i] = sc.next();
        }


        for(int i=0; i<R; i++){
            char Ri=roundS.charAt(i); // 상근이의 픽
            int[] maxif = new int[3]; // 베스트 경우
            for(int j=0; j<N; j++){
                char Ni=roundF[j].charAt(i); // 각 친구별 픽
                ans+=score(Ri, Ni); // 각 친구별 가위바위보 결과
                
                // 각 라운드마다 R, S, P를 냈을 때 score 계산
                maxif[0]+=score('R', Ni);
                maxif[1]+=score('S', Ni);
                maxif[2]+=score('P', Ni);
            }
            Arrays.sort(maxif); // 각 경우 점수 정렬
            maxans+=maxif[2]; // best 픽 했을 경우 최댓값 저장
        }

        System.out.println(ans);
        System.out.println(maxans);

        sc.close();
    }
}
