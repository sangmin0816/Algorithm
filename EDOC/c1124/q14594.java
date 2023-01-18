package c1124;
import java.util.*;

public class q14594 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        HashSet<Integer> room = new HashSet<>(); // Set, 중복 제거

        for(int i=0; i<M; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            for(int j=x; j<y; j++){
                room.add(j);
            }
        }

        System.out.println(N-room.size());

        sc.close();
    }
}
