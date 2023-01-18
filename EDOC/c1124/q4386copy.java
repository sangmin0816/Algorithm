package c1124;
import java.util.*;

public class q4386copy {
    private static int[] parent;
    private static ArrayList<Coordinates> tmpList = new ArrayList<>();
    private static ArrayList<Star> starList = new ArrayList<>();
    private static float answer = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 별의 갯수
        for (int i = 0; i < n; i++) { // 각 별의 좌표
            double x = sc.nextDouble();
            double y = sc.nextDouble();
            tmpList.add(new Coordinates(x, y)); // 일단 가중치 0으로 초기화
        }

        parent = new int[n];
        for (int i = 0; i < n; i++) { // 자기 자신으로 루트노드 초기화
            parent[i] = i; 
        }
        
        // 각 별 간의 간선 추가된 Star 배열
        for (int i = 0; i < tmpList.size() - 1; i++) {
            Coordinates star1 = tmpList.get(i);
            double x1 = star1.x;
            double y1 = star1.y;
            for (int j = i + 1; j < tmpList.size(); j++) {
                Coordinates star2 = tmpList.get(j);
                double x2 = star2.x;
                double y2 = star2.y;
                double weight = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
                starList.add(new Star(i, j, weight));
            }
        }

        // 간선 가중치 따라 starList 오름차순 정렬
        Collections.sort(starList);
        for (int i = 0; i < starList.size(); i++) {
            Star star = starList.get(i);
            if (!isSameParent((int) star.a, (int) star.b)) {
                answer += star.weight;
                union((int) star.a, (int) star.b); //연결
            }
        }

        System.out.printf("%.2f", answer);

        sc.close();
    }

    private static void union(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) {
            if (x < y) parent[y] = x;
            else parent[x] = y;
        }
    }

    private static int find(int x) {
        if (parent[x] == x) return x;
        else return parent[x] = find(parent[x]);
    }

    private static boolean isSameParent(int x, int y) {
        x = find(x);
        y = find(y);
        return x == y;
    }

    static class Coordinates{
        public Coordinates(double x2, double y2) {
        }
        double x;
        double y;
    }

    static class Star implements Comparable<Star> { // 간선 배열
        double a;
        double b;
        double weight;

        public Star(double x, double y, double weight) {
            this.a = x;
            this.b = y;
            this.weight = weight;
        }

        @Override
        public int compareTo(Star o) { // 간선 가중치에 따라 오름차순 정렬
            return Double.compare(weight, o.weight);
        }
    }
}
