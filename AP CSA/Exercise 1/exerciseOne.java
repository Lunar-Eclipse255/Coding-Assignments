import java.util.*;

public class exerciseOne{
    public static void main(String[]args){
        int nums[]={0,1,2,3,4};
        int nums2[];
        nums2=nums;
        System.out.println(nums[2]);
        nums2[2]=22;
        System.out.println(Arrays.toString(nums));
        System.out.println(Arrays.toString(nums2));
        System.out.println(nums.length);
        System.out.println(nums2.length);
    }
}