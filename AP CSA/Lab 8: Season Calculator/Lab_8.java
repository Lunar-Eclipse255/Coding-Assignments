//Imports
import java.util.Scanner;
public class Lab_8 {
    //Set-up
    public static void main (String[] args){
        //Sets up scanner
        Scanner scanner = new Scanner(System.in);
        //Asks for month and day and gets the input
        System.out.print("Give a month as a number: ");
        int month = scanner.nextInt();
        System.out.print("Give a day as a number: ");
        int day = scanner.nextInt();
        //Sees if day>31
        if (day>31){
            //prints error statement
            System.out.println("That date doesn't exist");
        }
        //Sees if month>12
        else if (month>12){
            //prints error statement
            System.out.println("That date doesn't exist");
        }
        //sees if month <= 0
        else if (month<=0){
            //prints error statement
            System.out.println("That date doesn't exist");
        }
        //sees if day<=0
        else if (day<=0){
            //prints error statement
            System.out.println("That date doesn't exist");
        }
        //Sees if the day is 31 for months that don't have 31 days
        else if ((month==4 || month==6 || month==9 || month==11) && day==31){
            //prints error statement
            System.out.println("That date doesn't exist");
        }
        //Sees if the day is greater than 28 in febuary
        else if (month==2 && day > 28){
            //prints error statement
            System.out.println("That date doesn't exist");
        }
        //Checks if its winter
        else if ((month == 12 && day >= 16) || (month >= 1 && month <= 2) || (month == 3 && day <= 15)){
            //Prints it's winter
            System.out.println("That's in Winter");
        }  
        //Checks if its spring
        else if ((month == 3 && day>15)|| (month >=4 && month <= 5) || (month ==6 && day <=15)){
            //Prints it's spring
            System.out.println("That's in Spring");
        }
        //Checks if its Summer
        else if ((month == 6 && day>15)|| (month >=7 && month <= 8) || (month ==9 && day <=15)) {
            //Prints it's summer
            System.out.println("That's in Summer");
        }
        
        else{
            //Says its fall
            System.out.println("That's in Fall");
        }
        scanner.close();
    }    
}