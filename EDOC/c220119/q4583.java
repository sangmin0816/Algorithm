package c220119;
import java.util.*;

public class q4583 { // https://www.acmicpc.net/problem/4583
    public static void main(String[] args) { // 
        Scanner sc = new Scanner(System.in);

        while(true){
            String str = sc.next();
            if(str.charAt(0)=='#') break; // 첫 문자가 #이면 바로 종료
            Stack<Character> mirror = new Stack<Character>(); // arraylist가 아니라 후입선출 스택으로!
            int i;
            for(i=0; i<str.length(); i++){ // 입력받으면서 거울모양으로 바꿔줌
                switch(str.charAt(i)){
                    case 'b':
                        mirror.push('d');
                        break;
                    case 'd':
                        mirror.push('b');
                        break;
                    case 'p':
                        mirror.push('q');
                        break;
                    case 'q':
                        mirror.add('p');
                        break;
                    case 'i':
                    case 'o':
                    case 'v':
                    case 'w':
                    case 'x':
                        mirror.push(str.charAt(i));
                        break;
                    default: // 거울 문자가 아니면
                        System.out.println("INVALID");
                        i=str.length(); // 더 입력 안받게 바로 for문 종료
                        break;
                }
            }
            if(i==str.length()+1) continue; // INVALID한 경우
            else{
                while(!mirror.empty()){ // 스택이 빌 때까지 pop하며 출력
                    System.out.printf("%c", mirror.pop());
                }
                System.out.print('\n'); // 줄바꿈 출력
            }
        }

        sc.close();
    }
}
