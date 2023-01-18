package c1117;

import java.util.*;

public class q1931 { // 회의실 배정 https://www.acmicpc.net/problem/1931
    public static class meeting { // 회의 객체
        int start; // 회의 시작 시간
        int end; // 회의 끝 시간
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 총 예약
        ArrayList<meeting> marr = new ArrayList<meeting>(); // 예약 리스트
        int ans = 0;

        for(int i=0; i<N; i++){ // 예약 리스트 생성
            meeting temp = new meeting();
            temp.start = sc.nextInt();
            temp.end = sc.nextInt();
            marr.add(temp);
        }

        Comparator<meeting> eComparator = new Comparator<meeting>() {
            public int compare(meeting m1, meeting m2){
                if(m1.end==m2.end) // end 시간이 같으면 start따라 정렬 필요
                    return m1.start-m2.start;
                return m1.end - m2.end;
            }
        };

        Collections.sort(marr, eComparator); // 끝, 시작 시간 순으로 오름차순 정렬

        int i=0;
        while(!marr.isEmpty()){
            meeting temp = marr.remove(0); // end 최소면서 start 최소인 예약
            if(temp.start>=i){ // 확정 예약과 겹치지 않으면
                ans++;
                i=temp.end; // 예약 확정
            }
        }

        System.out.println(ans);

        sc.close();
    }
}

// 어려웠던 점: 끝 시간이 같을 경우 시작 시간을 정렬해야 하는 걸 빼먹어서 한참 해맸다.
// java의 정렬 함수에 대해 많이 배울 수 있었다.