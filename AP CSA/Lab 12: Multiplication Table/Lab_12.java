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
        //Prints what table the number is for
        System.out.println("Table for "+userNum+":" );
        //Prints the multiplication table starting at 1 up to and including n, with tabs between numbers
        for (int i =1; i<=userNum;i++){
            for(int j=1; j<=10; j++){
                System.out.print(i*j+"\t");
            }
            //Goes down a line
            System.out.println();
        }
        scanner.close();
    }
}
