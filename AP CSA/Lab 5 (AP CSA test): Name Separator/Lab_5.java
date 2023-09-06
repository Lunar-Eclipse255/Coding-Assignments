//Imports
import java.util.*;
//Set-up
public class Lab_5 {
    public static void main(String[] args) {
    //Sets up for inputs
    Scanner console = new Scanner(System.in);
    //Asks for First, Middle, and Last Name (Inputs)
    System.out.println("What is your first, middle, and last name?");
    //Stores the string as fullName
    String fullName = console.nextLine();
    //Gets the length of the first name
    int firstNameIndex = fullName.indexOf(" ");
    //Stores the First Name as String firstName
    String firstName = fullName.substring(0, firstNameIndex);
    //Gets a string with just the middle and last name
    String secondPart = fullName.substring(firstNameIndex+1);
    //Gets the length of the middle name
    int middleNameIndex = secondPart.indexOf(" ");
    //Stores the middle name as String middleName
    String middleName = secondPart.substring(0, middleNameIndex);
    //Stores the last name as String lastName
    String lastName = secondPart.substring(middleNameIndex+1);
    //Prints first last and middle name
    System.out.println("First name is " + firstName);
    System.out.println("Middle name is " + middleName);
    System.out.println("Last name is " + lastName);
    console.close();
  }
}
