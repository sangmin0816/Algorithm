package 풀다만문제;
import java.util.*;
class Coo{
    int x;
    int y;
}

public class q1064 {
    public static void main(String[] args) { // 어떻게 하는지 모르겠다...
        Scanner sc = new Scanner(System.in);

        double ans = -1.0;

        ArrayList<Coo> arr = new ArrayList<Coo>();
        for(int i=0; i<3; i++){
            Coo temp = new Coo();
            temp.x = sc.nextInt();
            temp.y = sc.nextInt();
            arr.add(temp);
        }

        System.out.println(ans);

        sc.close();
    }
}
