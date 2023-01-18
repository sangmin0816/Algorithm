package d220130;
import java.util.*;

public class q12034 { // https://www.acmicpc.net/problem/12034 김인천씨의 식료품가게 (Large) 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=1; i<T+1; i++){
            int N = sc.nextInt();
            ArrayList<Integer> arr = new ArrayList<Integer>();
            for(int j=0; j<2*N; j++) arr.add(sc.nextInt()); // 항상 인덱스 주의하자 i랑 j 특히
            for(int j=0; j<N; j++) arr.remove(arr.indexOf(arr.get(j)/3*4));

            System.out.printf("Case #%d: ", i);
            for(int j=0; j<N; j++) System.out.printf("%d ", arr.get(j));
            System.out.printf("\n");
        }

        sc.close();
    }    
}
