package d1121;

import java.util.*;

public class q16173 { // 점프왕 쩰리 https://www.acmicpc.net/problem/16173
    public static void dfs(int x, int y, int N, int[][] arr, boolean[][] visited){
        if(x >=N || y>=N) // 범위 벗어남
            return;
        int now = arr[x][y];
        if(now==-1){ // 승리지점 도착
            System.out.println("HaruHaru");
            System.exit(0); // 프로그램 종료
        }
        visited[x][y]=true; // 방문 O
        
        // 범위 안에서, 미방문
        if((x+now)<N && visited[x+now][y]==false)
            dfs(x+now, y, N, arr, visited); // 오른쪽 이동
        if((y+now)<N && visited[x][y+now]==false)
            dfs(x, y+now, N, arr, visited); // 아래로 이동
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 게임 구역 크기
        int[][] arr = new int[N][N]; // 게임판의 맵(이동 숫자)
        boolean[][] visited = new boolean[N][N]; // 방문 여부

        for(int i=0; i<N; i++)
            for(int j=0; j<N; j++)
                arr[i][j]=sc.nextInt();

        dfs(0, 0, N, arr, visited);
        System.out.println("Hing");
        sc.close();
    }
}

// dfs 문제
// 어려웠던 점: dfs의 베이스 케이스 설정이 어려웠다. if(좌표, visited) 뒤에 else를 넣었는데 그게 아니었다.