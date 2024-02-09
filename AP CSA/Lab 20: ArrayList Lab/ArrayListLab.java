import java.util.*;
public class ArrayListLab {
  
   public static Integer smallest(ArrayList<Integer> test){
    Integer smallest = test.get(0);
    for(int i: test){
        if (i<smallest){
            smallest=i;
        }
    }
    return smallest;
   }
   
   public static String longest(ArrayList<String> words){
       String longest = words.get(0);
       for (int i=0; i<words.size();i++){
        if ((words.get(i)).length()>longest.length()){
            longest=(words.get(i));
        }
       }
       return longest;
   }
   
   public static void removeOcc(ArrayList<Integer> test1, int num)
   {
       Integer objectNum= new Integer(num);
       for (int i=0;i<test1.size();i++){
        if((test1.get(i)).equals(objectNum)){
            test1.remove(i);
            i--;
        }
       }
   }




   public static void main(String[] args)
   {
       ArrayList<Integer> nums = new ArrayList<Integer>();
       nums.add(12);
       nums.add(-5);
       nums.add(0);
       nums.add(0);
       nums.add(-9);
       nums.add(22);
       nums.add(0);

        
       ArrayList<String> words = new ArrayList<String>();
       words.add("hello");
       words.add("goodbye");
       words.add("welcome");
       words.add("hi");
       words.add("aloha");
      
       System.out.println(longest(words));
       System.out.println(smallest(nums));
       
       removeOcc(nums, 0);
       System.out.println(nums.toString());
       
   }


}


