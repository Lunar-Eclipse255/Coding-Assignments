//Impotrs
import java.util.*;
//Set-up
public class Lab_10 {
    public static void main (String[]args){
        //Sets up scanner
        Scanner scanner = new Scanner(System.in);
        //Asks for and stores an integer
        System.out.print("Give an Integer: ");
        int userNum = scanner.nextInt();
        //Sets the variable checkNum to the value the user inputted
        int checkNum = userNum;
        //Initializes the Int factorNum
        int factorNum=0;
        //While checkNum is greater than or equal than 1
        while (checkNum>=1){
            //Checks if the user inputted number is equal to checkNUm
            if (userNum%checkNum==0) {
                //If so increases factor number by One
                factorNum++;
                //Decreases checkNum by one
                checkNum--;
            }
            else {
                //Decreses checkNum by one
                checkNum--;
            }
        }
        //Prints out how manu factors the user inputted number has
        System.out.println(userNum + " has " + factorNum + " factors");
        scanner.close();
    }
}