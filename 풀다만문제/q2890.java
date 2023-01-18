package 풀다만문제;
import java.util.*;
public class q2890 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int R = sc.nextInt();
        int C = sc.nextInt();
        
        String map[] = new String[R];
        for(int i=0; i<R; i++) map[i]=sc.next();
        int ranks[][] = new int[10][2];

        for(int i=0; i<R; i++){
            for(int j=1; j<C-1; j++){
                char now = map[i].charAt(C-j-1);
                if(now!='.') {
                    ranks[(now-'1')][0]=j;
                    break;
                }
            }
        }

        for(int i=0; i<9; i++) System.out.println(ranks[i]);

        sc.close();
    }
}
