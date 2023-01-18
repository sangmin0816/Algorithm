package c220119;
import java.util.*;

public class q15904 { // https://www.acmicpc.net/problem/15904
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        ArrayList<Character> ucpc = new ArrayList<Character>(); // 선입선출 큐

        for(int i=0; i<str.length(); i++){
            if(((str.charAt(i)-'a')<0) && str.charAt(i)!=' ') ucpc.add(str.charAt(i)); // 대문자만 큐에 넣음
        }

        Boolean flag = false;

        if(ucpc.size()>3){ // 대문자 3개 이하는 실패
            String check = "UCPC";
            int i=0;
            while(!ucpc.isEmpty()){
                if(ucpc.remove(0)==check.charAt(i)) { // check와 비교해 큐에서 대문자 꺼냄
                    i++;
                    if(i==4) { // UCPC 만들어지면 성공
                        flag = true;
                        break;
                    }
                }
            }
        }

        if(flag==true)  System.out.println("I love UCPC");
        else System.out.println("I hate UCPC");
        
        sc.close();
    }
}
