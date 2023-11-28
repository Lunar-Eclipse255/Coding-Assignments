public class SelfDivisor {
    public static boolean isSelfDivisor(int number){
        int storage = number;
        int temp=0;
        while(storage>=10){
            temp = storage%10;
            storage = storage/10;
            if (temp==0){
                return false;
            }
            else if ((number%temp)!=0){
                return false;
            }
        }
        return true;
    }

    public static int[] firstNumSelfDivisors(int start, int num){
        int numb = num;
        int stars = start;
        int i =0;
        int[] nums = new int[num];
        while(numb>0){
            if (isSelfDivisor(stars)){
                nums[i]=stars;
                i++;
                numb--;
            }
            stars ++;
        }
        return nums;
    }
    
    
}
