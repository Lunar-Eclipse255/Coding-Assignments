import java.util.*;
class Main {
  public static void main(String[] args) {
    Scanner console = new Scanner(System.in);
    System.out.println("What is your first, middle, and last name?");
    String fullName = console.nextLine();
    int firstNameIndex = fullName.indexOf(" ");
    String firstName = fullName.substring(0, firstNameIndex);
    String secondPart = fullName.substring(firstNameIndex+1);
    int middleNameIndex = secondPart.indexOf(" ");
    String middleName = secondPart.substring(0, middleNameIndex);
    String lastName = secondPart.substring(middleNameIndex+1);
    System.out.println("First name is " + firstName);
    System.out.println("Middle name is " + middleName);
    System.out.println("Last name is " + lastName);
  }
}