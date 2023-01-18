package d220116;
import java.util.*;

public class q9655 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/9655 거스름돈
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        String winner[] = {"SK", "CY", "SK", "CY", "SK","CY"};

        System.out.println(winner[((N-1)/3%2)*3+(N-1)%3]);

        sc.close();
    }    
}
