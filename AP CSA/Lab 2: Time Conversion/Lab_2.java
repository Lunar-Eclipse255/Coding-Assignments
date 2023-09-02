public class Lab_2 {
    public static void main(String[] args) {
        //Declares age and time
        int age = 15;
        int minutes = 351;
        //Prints age 
        System.out.println("Age: " + age);
        //Sets hourTime equal the amount of minutes divided by 60
        int hourTime = minutes/60;
        //Finds how many minutes are remaining by taking modulus of minutes and 60
        int hourTimeExtra=minutes%60;
        //Prints the value of just minutes then the converted value
        System.out.println(minutes + " minutes is equal to " + hourTime + " hours " + hourTimeExtra + " minutes.");
      }
}
