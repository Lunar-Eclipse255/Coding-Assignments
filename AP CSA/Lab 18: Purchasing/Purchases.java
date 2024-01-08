import java.util.*;
public class Purchases {
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        int numPurchases = scanner.nextInt();
        double[] purchaseArray = new double[numPurchases];
        for (int i=0;i<purchaseArray.length;i++){
            purchaseArray[i]= scanner.nextDouble();
        }
        double sum=0;
        for (double i:purchaseArray){
            sum +=i;
        }
        double average =sum/numPurchases;
        double over=0;
        for (double i:purchaseArray){
            if (i>average){
                over++;
            }
        }
        System.out.println("Sum: "+sum);
        System.out.println("Average: "+average);
        System.out.println("Over: "+over);
    }
}
