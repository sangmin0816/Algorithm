package 풀다만문제;
import java.util.*;

public class q19947 {
    public static void main(String[] args) { // 틀림 수정 필요
        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int Y = sc.nextInt();

        int years[] = {5, 3, 1};
        double invest[] = {1.35, 1.2, 1.05};
        long ans = H;
            
        int i=0;
        while(Y>0){
            while(Y>=years[i]){
                ans = (int)(ans * invest[i]);
                Y-=years[i];
            }
            i++;
        }

        System.out.println(ans);

        sc.close();
    }
}
