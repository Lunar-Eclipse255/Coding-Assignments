// imports
import java.util.*;
import java.lang.Math;
//set-up
public class Lab_11 {
    
    public static void main (String[]args){
        
        //sets-up scanner
        Scanner scanner = new Scanner(System.in);
        //gets a number from the user and stores it as the int userNum
        System.out.print("Enter a number: ");
        int userNum = scanner.nextInt();
        //initializes the boolean thrirteenFound to false
        boolean thirteenFound = false;
        //a for loop that iterates the same number of times as userNum is large
        for (int i = 1; i<=userNum; i++){
            //initializes the variable randNum to a random number from 10 to 19 inclusive
            int randNum = (int) (Math.random() * 10) + 10;
            //prints randNum
            System.out.println("Next = " + randNum);
            //checks if the random number was 13
            if (randNum == 13) {
                //if so sets the boolean thirteenFound to true
                thirteenFound = true;
            }
        }
        //if there was a thirteen prints that there was a thirteen
        if (thirteenFound) {
            System.out.println("We saw a 13!");
        }
        //if there was no thirten prints that there was no 13 
        else {
            System.out.println("No 13 was seen");
        }

    }

}
