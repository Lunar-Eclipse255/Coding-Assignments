public class Sorting {
    public static void insertionSort(int[] array){
        for(int i = 1; i < array.length; i++){
            int[] temp =new int[1];
           int current = array[i];
           int index = i - 1;
           while(index >= 0 && current < array[index]){
              temp[0]=array[index];
            array[index]=array[index+1];
            array[index+1]=temp[0];  
            index--; 
            }
           //list.add(index+1, current);  
            
            
        }
        for (int j:array){
            System.out.println(j);
        }
      }
      public static void main(String[] args) {
        int[] array = {5,4,3,2,1,8,7,6,10,9};
        insertionSort(array);

      }
      
}
