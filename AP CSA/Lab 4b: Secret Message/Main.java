//Set-up
class Main {
  public static void main(String[] args) {
    //Declares string
    String text = "Have you ever seen a fox drinking from under your faucet?";
    //Gets first three letters
    String Hav = text.substring(0,3);
    //Gets the letters from the 6th character of the 7th word to the 1st character of the 8th word
    String ingf = text.substring(30,35);
    //Gets first two letters of 9th word
    String un = text.substring(39,41);
    //Gets a space
    String space = " ";
    //Gets first letter of second to last word
    String y = text.substring(45,46);
    //Gets the length of the string
    int length = text.length();
    //Using the length of the word gets the last three characters
    String et = text.substring(length-3,length);
    //Concatatntes the different strings together
    String done = Hav + ingf + un + space + y + et;
    //Prints the hidden message
    System.out.print("Having fun yet?");
      
  }
}