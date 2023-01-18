package 풀다만문제;
import java.util.*;


public class q1459 { // 모르겠당
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int Y = sc.nextInt();
        int W = sc.nextInt();
        int S = sc.nextInt();

        double mintime = (X+Y)*W;
        if(S<W*2){
            if(X<Y){
                for(int i=1; i<=X; i++) {
                    double time = (X+Y-2*i)*W + S*i;
                    if(mintime > time) mintime = time;
                }
                for(int i=1; i<=(Y-X)/2; i++){
                    double time = (X+Y-2*i)*W + S*i;
                    if(mintime > time) mintime = time;
                }
            }
            else{
                for(int i=1; i<=Y; i++) {
                    double time = (X+Y-2*i)*W + S*i;
                    if(mintime > time) mintime = time;
                }
                for(int i=1; i<=(X-Y)/2; i++){
                    double time = (X+Y-2*i)*W + S*i;
                    if(mintime > time) mintime = time;
                }
            }
        }

        System.out.println(mintime);

        sc.close();
    }
}
