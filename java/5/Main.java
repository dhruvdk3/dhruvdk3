import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        // System.out.println((int) 1);
        int sp = 0;
        int li = 0;
        int ap = 0;
        int di = 0;
        int i;
        try {
            FileReader fr = new FileReader("x.txt");

            while ((i = fr.read()) != -1) {
                if (i == 32) {
                    sp++;
                }
                // System.out.println(i);
                if (i >= 48 && i <= 57) {
                    di++;
                }
                if (i >= 97 && i <= 122) {
                    ap++;
                }
                if (i == 10) {
                    li++;
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        }
        System.out.println("Spaces : " + sp);
        System.out.println("Digits : " + di);
        System.out.println("Alphabets : " + ap);
        System.out.println("lines : " + (li - 1));
    }
}
