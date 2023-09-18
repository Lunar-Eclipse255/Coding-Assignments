//Import
import java.util.*;
//Set-up
public class Lab_12 {

    public static void main (String[]args) {
        //Sets up scanner
        Scanner scanner = new Scanner(System.in);
        //Asks for a number from the user and stores it
        System.out.print("Give a number: ");
        int userNum = scanner.nextInt();
        //Prints the multiplication table starting at 1 up to and including n, with tabs between numbers
        for (int i =1; i<=userNum;i++){
            System.out.println(i*1 + "\t" + i*2 +"\t"+i*3+"\t"+i*4+"\t"+i*5+"\t"+i*6+"\t"+i*7+"\t"+i*8+"\t"+i*9+"\t"+i*10);
        }
        scanner.close();
    }
}
