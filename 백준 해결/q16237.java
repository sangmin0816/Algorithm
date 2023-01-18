package d220130;
import java.util.*;

public class q16237 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int ABCD[] = new int[4];
        for(int i=0; i<4; i++) ABCD[i] = sc.nextInt();
        int ans = sc.nextInt(); // E는 그대로 더하기
        
        ans += ABCD[3]; // D 그래도 더하되, A 영향
        if(ABCD[3]>ABCD[0]) ABCD[0] = 0;
        else ABCD[0]-=ABCD[3];

        ans += ABCD[2]; // C 그대로 더하되, A나 B에 영향
        if(ABCD[2]>ABCD[1]){
            ABCD[2]-=ABCD[1];
            ABCD[1] = 0;
            if(ABCD[2]>ABCD[0]/2) ABCD[0]=0;
            else ABCD[0]-=ABCD[2]*2;
        }
        else{
            ABCD[1]-=ABCD[2];
        }


        ans+= ABCD[1] /2;
        if(ABCD[1]/2 > ABCD[0]) ABCD[0] = 0;
        else ABCD[0]-=ABCD[1]/2;

        if(ABCD[1]%2 == 0) ans+=(4+ABCD[0])/5;
        else{
            ans++;
            if(ABCD[0]>3){
                ABCD[0]-=3;
                ans+=(4+ABCD[0])/5;
            }
        }

        System.out.println(ans);

        sc.close();
    }
}
