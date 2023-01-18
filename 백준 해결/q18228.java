package d1121;

import java.util.*;

public class q18228 { // https://www.acmicpc.net/problem/18228
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        ArrayList<Integer> left = new ArrayList<Integer>();
        ArrayList<Integer> right = new ArrayList<Integer>();
        int flag = 0;
        int ans = 0;

        for(int i=0; i<N; i++){ // 펭귄 위치(-1) 기준 왼쪽, 오른쪽 구분
            int temp=sc.nextInt();
            if(temp==-1){
                flag=1;
                continue;
            }
            if(flag==0)
                left.add(temp);
            else
                right.add(temp);
        }

        Collections.sort(left); // 왼쪽에서 가장 작은 값
        Collections.sort(right); // 오른쪽에서 가장 작은 값
        ans = left.get(0) + right.get(0); // 펭귄의 왼, 오 모두 한 부분이라도 끊어지면 죽음

        System.out.println(ans);

        sc.close();
    }
}
