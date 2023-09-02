import java.util.*;
public class Lab_4a {
    public static void main(String[] args) {
        //Sets-up for input
        Scanner console = new Scanner(System.in);
        //Asks for a word
        System.out.println("Give a word");
        //Stores their answer
        String word = console.next();
        //Finds where in the word a is
        int place = word.indexOf('a');
        //Prints the place of a
        System.out.println(place);
      }
}
