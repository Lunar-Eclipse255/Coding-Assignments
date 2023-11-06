import java.util.*;
public class AverageMath {
    public static void main(String[]args){
        //creates the array
        int[] array={-5, 96, 98, 56, 77};
        //calls the methods and prints what they return
        //prints the average
        System.out.println(average(array));
        //prints the num of numbers above the average
        System.out.println(countAboveAve(array));
        //prints the largest number in the array
        System.out.println(largest(array));
        //prints the index of the smallest number in the array
        System.out.println(indexOfsmallest(array));
        //prints the array
        System.out.println(Arrays.toString(array));
        
    }
    public static double average(int[] array){
        //gets the length of the array
        double total=array.length;
        double num=0;
        //gets the sum of the numbers in the array
        for (int i : array){
            num+=i;
        }
        //returns the sum of numbers divided by the total number of numbers to get the average
        return num/total;
    }
    public static int countAboveAve(int[]array){
        int aboveAve=0;
        //gets the number of nums above the average
        for (int i: array){
            if (i>average(array)){
                aboveAve++;
            }
        }
        //returns the number of nums above the average
        return aboveAve;
    }
    public static int largest(int[] array){
        int largestNum=array[0];
        //gets the largest numbers
        for (int i:array){
            if (i>largestNum){
                largestNum=i;
            }
        }
        //returns the largest numbers
        return largestNum;
    }
    public static int indexOfsmallest(int[]array){
        int smallest=0;
        //gets the index of the smallest number
        for(int i=0;i<array.length;i++){
            if (array[i]<smallest){
                smallest=i;
            }
        }
        //returns the index of the smallest number
        return smallest;
    }

}
