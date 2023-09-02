import java.util.*;
import java.lang.Math;
public class Testing {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Type a number: ");
        int number = Math.abs(console.nextInt());

        if (number % 2 == 0) {
            if (number % 3 == 0) {
                System.out.println("Divisible by 6.");
            }
        } else if (number % 2 == 1) {
            System.out.println("Odd.");
        } else {
            System.out.println("Even, but not divisible by 6.");
        }
    }
}


