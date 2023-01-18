package c1117;

import java.util.*;

public class q14655 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] maxcoin = new int[N+2];
        int[] mincoin = new int[N+2];
        Integer[] maxround = new Integer[2*N];
        int[] minround = new int[2*N];

        for(int i=0; i<N; i++)
            maxcoin[i]=sc.nextInt();
        for(int i=0; i<N; i++)
            mincoin[i]=sc.nextInt();
        for(int i=N; i<N+2; i++){
            maxcoin[i]=maxcoin[i-N];
            mincoin[i]=mincoin[i-N];
        }
        for(int i=0; i<N; i++){
            maxround[i]=maxcoin[i]+maxcoin[i+1]+maxcoin[i+2];
            minround[i]=mincoin[i]+mincoin[i+1]+mincoin[i+2];
            maxround[N+i]=maxround[i]*-1;
            minround[N+i]=minround[i]*-1;
        }

        Arrays.sort(maxround, Comparator.reverseOrder());
        Arrays.sort(minround);

        int ans = maxround[0] - minround[0];
        System.out.println(maxround[0]);
        System.out.println(minround[0]);
        System.out.println(ans);

        sc.close();
    }
}
