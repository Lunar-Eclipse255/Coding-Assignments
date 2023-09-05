import java.util.Scanner;
public class Lab_8 {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Give a month as a number: ");
        int month = scanner.nextInt();
        System.out.print("Give a day as a number: ");
        int day = scanner.nextInt();
        System.out.println("That's in " + Season(month, day));

    

    }
    
    public static String Season(int month, int day) {
        if ((month == 12 && day >= 16) || (month >= 1 && month <= 2) || (month == 3 && day <= 15)){
            return "Winter";
        }  
        else if ((month == 3 && day>15)|| (month >=4 && month <= 5) || (month ==6 && day <=15)){
            return "Spring";
        }
        else if ((month == 6 && day>15)|| (month >=7 && month <= 8) || (month ==9 && day <=15)) {
            return "Summer";
        }
        else{
            return "Fall";
        }
    }
}