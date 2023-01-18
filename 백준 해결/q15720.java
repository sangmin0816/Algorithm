package d1121;
import java.util.*;

public class q15720 { // https://www.acmicpc.net/problem/15720
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int B = sc.nextInt(); // 버거 갯수
        int C = sc.nextInt(); // 사이드 갯수
        int D = sc.nextInt(); // 음료 갯수
        int[] set = {B, C, D}; // 구성할 수 있는 셋트 갯수의 최소값
        Integer[] Barr = new Integer[B]; // 버거 가격
        Integer[] Carr = new Integer[C]; // 사이드 가격
        Integer[] Darr = new Integer[D]; // 음료 가격
        int initans = 0; // 할인 전 가격
        int setans = 0; // 최소 할인 가격(셋트 구성 최대값)

        for(int i=0; i<B; i++){
            Barr[i]=sc.nextInt();
            initans+=Barr[i];
        }
        for(int i=0; i<C; i++){
            Carr[i]=sc.nextInt();
            initans+=Carr[i];
        }
        for(int i=0; i<D; i++){
            Darr[i]=sc.nextInt();
            initans+=Darr[i];
        }

        Arrays.sort(set); // 구성할 수 있는 세트 갯수
        Arrays.sort(Barr, Collections.reverseOrder());
        Arrays.sort(Carr, Collections.reverseOrder());
        Arrays.sort(Darr, Collections.reverseOrder());

        for(int i=0; i<set[0]; i++){ // 구성할 수 있는 세트 가격 합
            setans+=Barr[i]+Carr[i]+Darr[i];
        }
        setans = (int)(initans - setans*0.1); // 초기 값에서 할인값(원래 가격 * 0.1) 빼서 할인 가격

        System.out.println(initans);
        System.out.println(setans);

        sc.close();
    }
}
