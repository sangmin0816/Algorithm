import java.util.*;

public class c9656 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        String loser[] = {"CY", "SK", "CY", "SK", "CY", "SK"}; // 지게 되는 순서

        System.out.println(loser[((N-1)/3%2)*3+(N-1)%3]);
        // 수가 클 때는 3개씩 가져간다고 가정. 이를 
        sc.close();
    }
}