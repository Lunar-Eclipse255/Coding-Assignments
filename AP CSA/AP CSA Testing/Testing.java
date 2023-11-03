public class Testing {
        public static void main(String[]args){
            printBackwards();
        }
        public static void printBackwards(){
            int[] element  = {1,-3,4,-4,7,2};
            //elementLength=element.length;
            for (int i=(element.length-1); i>0;i--){
                System.out.println("element ["+i+"] is "+element[i]);
            }

    }
}
