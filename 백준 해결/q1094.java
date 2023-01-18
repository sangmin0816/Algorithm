package d220123;
import java.util.*;
public class q1094 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1094
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();

        String xx = Integer.toBinaryString(X);
        xx=xx.replaceAll("0", "");

        System.out.println(xx.length());

        sc.close();
    }
}
