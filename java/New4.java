import java.util.Scanner;

public class New4 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter distans in meter:");
        double a=sc.nextDouble();
        Double b=a/1000;
        System.out.print("distans in km:"+b);
        sc.close();
    }
}
