package d220130;
import java.util.*;

public class q6550 { // https://www.acmicpc.net/problem/6550 부분 문자열
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()){ // 테스트 케이스 종료가 명확하지 않을 때 EOF 처리하는 법. 여기서 엄청 걸렸다 흑흑
            String s = sc.next();
            String t = sc.next();

            boolean flag = false;
            
            int j=0;
            for(int i=0; i<t.length(); i++){
                if(t.charAt(i)==s.charAt(j)){
                    if(j==s.length()-1){
                        flag=true;
                        break;
                    }
                    j++;
                }
            }

            if(flag) System.out.println("Yes");
            else System.out.println("No");
        }

        sc.close();
    }    
}
