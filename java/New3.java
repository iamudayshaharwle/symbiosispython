import java.util.*;

public class New3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter first sub marks:");
        int a = sc.nextInt();
        System.out.println("enter 2nd sub marks");
        int b = sc.nextInt();
        System.out.println("enter 3rd sub marks");
        int c = sc.nextInt();
        System.out.println("enter 4rd sub marks");
        int d = sc.nextInt();
        System.out.println("enter 5th sub marks");
        int e = sc.nextInt();
        float sum=a+b+c+d+e;
        float per=sum/5;
        System.out.print("persentage:" +per+"%");
        sc.close();


    }

}
