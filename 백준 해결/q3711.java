package d220123;
import java.util.*;
public class q3711 { // while(true)문 쓰기를 두려워하지 말라
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=0; i<T; i++){
            int G = sc.nextInt();
            int student[] = new int[G];
            for(int j=0; j<G; j++) student[j]=sc.nextInt();
            int m = 1;

            if(G!=1){
                while(true){
                    boolean flag=true;
                    ArrayList<Integer> res = new ArrayList<Integer>();
                    for(int k=0; k<G; k++){
                        if(res.contains(student[k]%m)){
                            flag=false;
                            break;
                        }
                        res.add(student[k]%m);
                    }
                    if(flag==true) break;
                    m++;
                }
            }

            System.out.println(m);
        }
        sc.close();
    }
}
