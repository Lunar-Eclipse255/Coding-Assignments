public class Main {
    public static void main(String[] args) {
        System.out.println(SelfDivisor.isSelfDivisor(20));
        int[] newNums= SelfDivisor.firstNumSelfDivisors(10,3) ;
        for (int i:newNums){
            System.out.println(i);
        }
    }
}
