import java.util.*;
import java.io.*;

class D extends Exception {
    D(String s) {
        super(s);
    }
}

public class Main1 {

    public static void vote(float a, float b) throws D {
        {
            if((a/b) <= 0.0004){
                throw new D("TooSmallNumber");
            }
            else System.out.println(a/b);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1 float number ");
        float a = sc.nextFloat();
        System.out.println("Enter 2 float number ");
        float b = sc.nextFloat();

        try {
            vote(a,b);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}

