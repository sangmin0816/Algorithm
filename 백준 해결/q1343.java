package d220102;
import java.util.*;

public class q1343 {
    public static void main(String[] args) { // https://www.acmicpc.net/problem/1343 폴리오미노
        Scanner sc = new Scanner(System.in);

        String board = sc.next();
        String ans = "";
        int counter = 0;
        
        for(int i=0; i<board.length(); i++){
            if(board.charAt(i)=='X') counter++;
            else{
                if(counter%2!=0){
                    System.out.println("-1");
                    System.exit(0);
                }
                while(counter>0){
                    if(counter>=4) {
                        ans+="AAAA";
                        counter-=4;
                    }
                    else {
                        ans+="BB";
                        counter-=2;
                    }
                }
                ans+=".";
            }
        }

        if(counter%2!=0){
            System.out.println("-1");
            System.exit(0);
        }
        while(counter>0){
            if(counter>=4) {
                ans+="AAAA";
                counter-=4;
            }
            else {
                ans+="BB";
                counter-=2;
            }
        }
        System.out.println(ans);
        sc.close();
    }
}
