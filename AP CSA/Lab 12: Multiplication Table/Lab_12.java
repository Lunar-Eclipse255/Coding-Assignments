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
        //Prints the multiplication table starting at 1 up to and including userNum, with tabs between numbers
        for (int i =1; i<=userNum;i++){
            System.out.println("Table for "+i+":" );
            //Prints the times table up to the number j
            for (int j=1; j<=i; j++)
            System.out.println(j*1 + "\t" + j*2 +"\t"+j*3+"\t"+j*4+"\t"+j*5+"\t"+j*6+"\t"+j*7+"\t"+j*8+"\t"+j*9+"\t"+j*10);

        }
        scanner.close();
    }
}