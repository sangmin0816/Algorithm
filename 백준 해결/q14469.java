package d220130;
import java.util.*;

class Cow{
    int arrive;
    int check;
}

public class q14469 { // https://www.acmicpc.net/problem/14469
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        ArrayList<Cow> cows = new ArrayList<Cow>();

        for(int i=0; i<N; i++){
            Cow temp = new Cow();
            temp.arrive = sc.nextInt();
            temp.check = sc.nextInt();
            cows.add(temp);
        }

        Collections.sort(cows, new Comparator<Cow>(){ // 이 부분이 항상 어렵다.
            @Override
            public int compare(Cow c1, Cow c2){
                return c1.arrive - c2.arrive;
            }
        });

        int ans = 0;
        for(int i=0; i<N; i++){
            if(cows.get(i).arrive>ans) ans = cows.get(i).arrive;
            ans += cows.get(i).check;
        }

        System.out.println(ans);

        sc.close();
    }
}
