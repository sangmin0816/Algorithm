package d220109;

import java.util.*;

public class q1439 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1439
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        
        int cnt[] = {0, 0};
        int j=0;

        for(int i=0; i<str.length()-1; i++){
            if(str.charAt(i)==str.charAt(i+1))  continue;
            else{
                cnt[j%2]++;
                j++;
            }
        }

        switch(j){
            case 0:
                System.out.println(0);
                break;
            default:
                System.out.println(cnt[(j+1)%2]);
        }

        

        sc.close();
    }
}
