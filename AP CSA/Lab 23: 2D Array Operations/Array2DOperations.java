public class Array2DOperations {
    public static int sum(int[][] array){
        int num=0;
        for(int i=0;i<array.length;i++){
            for(int j=0;j<array[i].length;j++){
                num+=array[i][j];
            }
        }
        return num;
    }
    public static int rowSum(int[][] array, int row){
        int num=0;
        for(int i=0;i<array[row].length;i++){
            num+=array[row][i];
        }
        return num;
    }
    public static int colSum(int[][] array, int col){
        int num=0;
        for(int i=0;i<array.length;i++){
            num+=array[i][col];
        }
        return num;
    }
    public static int sum2(int[][] array){
        int num=0;
        for(int i=0;i<array.length;i++){
            num+=rowSum(array,i);
        }
        return num;
    }
    public static int largest(int[][] array){
        int largest = array[0][0];
        for(int[] row : array){
            for(int col : row){
                if(col>largest){
                    largest=col;
                }
            }
        }
        return largest;
    }
    public static int largestByRow(int[][] array, int row){
        int largest = array[row][0];
        for(int i : array[row]){
            if(i>largest){
                largest=i;
            }
        }
        return largest;
    }
    public static int largest2(int[][] array){
        int largest = array[0][0];
        for(int i=0;i<array.length;i++){
            if(largestByRow(array,i)>largest){
                largest=largestByRow(array,i);
            }
        }
        return largest;
    }
    public static void main(String[] args) {
        int[][] numbers ={{3,4,5},{4,8,6},{5,7,7}};
        System.out.println(sum(numbers));
        System.out.println(rowSum(numbers,1));
        System.out.println(colSum(numbers,1));
        System.out.println(sum2(numbers));
        System.out.println(largest(numbers));
        System.out.println(largestByRow(numbers,0));
        System.out.println(largest2(numbers));
    }
}
