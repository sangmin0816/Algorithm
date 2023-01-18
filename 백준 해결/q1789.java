package d220109;
import java.util.*;
import java.lang.Math;

public class q1789 { // https://www.acmicpc.net/problem/1789
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long S = sc.nextLong();

        long i = (long)Math.sqrt(2*S);
        // 요 i의 범위 때문에 한참 고민함. 얘도 아래 i*(i+1)/2 때문에 long으로 해줘야 함
        while((i*(i+1)/2)>S){
            i--;
        }

        System.out.println(i);

        sc.close();
    }
}
