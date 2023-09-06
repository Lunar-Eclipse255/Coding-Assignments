//Imports
import java.util.Scanner;
//Set-up
public class Lab_7 {
    public static void main(String[] args) {
    //Sets up input
    Scanner console = new Scanner(System.in);
    //Asks for an input
    System.out.print("What price was the car sold at?: ");
    //Stores input to price variable
    int price=console.nextInt();
    //Declares commision variable
    double commision=8;
    //checks if price is greater than or equal to 1000
    if (price>=1000){
      //if so checks if price is less than or equal to 10000
      if (price<=10000){
        //if so sets commision to price times 0.1
        commision=price*0.1;
      }
      //if not checks if price is greater than 10000
      else if (price>10000){
        //if so checks if price is less than or equal to 50000
        if(price<=50000){
          //if so sets commision equal to price times 0.075
          commision=price*0.075;
        }
        //if not checks if price is greater than 50000
        else if (price>50000){
          //if so sets commision equal to price times 0.05
          commision=price*0.05;
        }
      }
    }
    //if its not its sets commision equal to price times 0
    else{
      commision=price*0;
    }
    //prints what your commision is
    System.out.println("Your commision is: $" + commision);
    console.close();
    }
}
