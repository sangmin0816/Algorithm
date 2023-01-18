package 풀다만문제;
import java.util.*;
public class q2635 {
    public static void main(String[] args) { // 내가 초등부 문제도 못 풀다니
        Scanner sc = new Scanner(System.in);

        int first = sc.nextInt();

        int max = 3;
        for(int i = first; i>0; i--){
            int x = first;
            int y = i;
            int count = 2;
            while(x-y>=0){
                y=x-y;
                x=x-y;
                count++;
            }
            if(count>max) max=count;
        }

        System.out.println(max);
        sc.close();
    }
}
