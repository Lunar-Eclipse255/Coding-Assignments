import java.util.Scanner;
public class AreaTraingle {
    public static void main(String[] args) {  
        Scanner scanner = new Scanner(System.in);
        double detOne=0;
        double detTwo=0;
        double detThree=0;
        double sol=0;
        System.out.println("State the x and y points of the first vertex seperated by a space");
        double xOne = scanner.nextDouble();
        double yOne = scanner.nextDouble();
        System.out.println("State the x and y points of the second vertex seperated by a space");
        double xTwo = scanner.nextDouble();
        double yTwo = scanner.nextDouble();
        System.out.println("State the x and y points of the third vertex seperated by a space");
        double xThree = scanner.nextDouble();
        double yThree = scanner.nextDouble();
        double[][] matrix = {
            {xOne,yOne,1},
            {xTwo,yTwo,1},
            {xThree,yThree,1}
        };
        detOne=xOne*(yTwo-yThree);
        detTwo=(-1*xTwo)*(yOne-yThree);
        detThree=xThree*(yOne-yTwo);
        sol=detOne+detTwo+detThree;
        System.out.println(Math.abs(0.5*sol));
    }
}
