//imports
import java.util.Scanner;
//set-up
public class Lab_9 {
    public static void main(String[]args){
        //sets-up scanner
        Scanner scanner = new Scanner(System.in);
        //asks for a word and stores it as String word
        System.out.print("Give one word: ");
        String word =scanner.nextLine();
        
        //checks if word is less than or equal to, two characters long
        if (word.length()<=2){
            //if so prints error message
            System.out.println("Word is too short, it must be at least 3 characters long");
        }
        //if the objects ends in -ing, it moves the last four letters to the front of the word
        else if (word.substring(word.length()-3).equals("ing")){
            String newWord = word.substring(0,word.length()-4);
            System.out.println((word.substring(word.length()-4))+ newWord);
        }

        //if the word ends in a vowel it adds pig to the end of the word
        else if (word.charAt(word.length()-1) == 'a'|| word.charAt(word.length()-1) == 'e'|| word.charAt(word.length()-1) == 'i' || word.charAt(word.length()-1) == 'o' || word.charAt(word.length()-1) == 'u') {
            System.out.println(word+"pig");

        }
        //Else the haha is added to the begining of the word
        else{
            System.out.println("haha" + word);
        }
        scanner.close();
    }
}