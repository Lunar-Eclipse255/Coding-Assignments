import java.util.*;
public class Lab_3 {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        //Asks for a three digit number
        System.out.println("Give a 3 digit int");
        //Gets the input for teh 3 digit number
        int num = console.nextInt();
        //Does math to seperate the numbers by place
        int numOne= num%10;
        int numTen = ((num%100)-numOne)/10;
        int numHundred=(num-(num%100))/100;
        //Prints the result
        System.out.println("Hundreds: " + numHundred + " Tens: " + numTen + " Ones: " + numOne);
        console.close();
    }
}
