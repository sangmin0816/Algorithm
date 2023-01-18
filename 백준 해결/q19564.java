package d1121;
import java.util.*;

public class q19564 { // https://www.acmicpc.net/problem/19564
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String S = sc.next(); // 문자열
        int K = 1; // abc~ 알파벳 입력 횟수
        int pv = 0; // 이전 알파벳
        
        for(int i=0; i<S.length(); i++){
            int now = S.charAt(i); // 현재 알파벳
            // 등호를 빼먹어서 틀렸다. 같은 문자 입력되어도 K++ 해야 한다.
            if(pv>=now) // 현재가 pv보다 전에 나오거나 같은 알파벳이면 K 입력 필요
                K++; 
            pv=now;
        }

        System.out.println(K);

        sc.close();
    }
}
