package d220130;
import java.util.*;

public class q9656 { // https://www.acmicpc.net/problem/9656 돌 게임 2
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt(); // 돌 갯수
        
        String loser[] = {"CY", "SK", "CY", "SK", "CY", "SK"};

        System.out.println(loser[((N-1)/3%2)*3+(N-1)%3]);

        sc.close();
    }
}
