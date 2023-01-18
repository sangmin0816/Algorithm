package c1117;

import java.util.*;

public class q1388 { // https://www.acmicpc.net/problem/1388
    public static int N;
    public static int M;
    public static char[][] floor;
    public static boolean[][] visited;
    public static int ans = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        visited = new boolean[N][M];
        floor = new char[N][M];
        
        for(int i=0; i<N; i++){
            floor[i]=sc.next().toCharArray();
        }

        dfs();
        
        System.out.println(ans);

        sc.close();
    }

    static void dfs(){
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                visited[i][j]=true;
                char now = floor[i][j];
                if(now=='-'){
                    while(i<N && floor[i][j]==now && visited[i][j]==false){
                        visited[i][j]=true;
                        i++;
                    }
                    ans++;
                }
                if(now=='|'){
                    int k=j;
                    while(j<M && floor[i][k]==now && visited[i][k]==false){
                        visited[i][k]=true;
                        k++;
                    }
                    ans++;
                }
            }
        }
    }
}
