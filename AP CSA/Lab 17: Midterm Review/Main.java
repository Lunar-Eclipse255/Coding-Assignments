public class Main {
    public static void main(String[] args) {
        Locker lockerOne = new Locker("Bob", "Landy");
        System.out.println(lockerOne);
        //System.out.println(lockerOne.position()+lockerOne.whichHall()+lockerOne.combination()+lockerOne.lockerStatus());
        lockerOne.openLocker(1234);
        System.out.println(lockerOne);
        lockerOne.openLocker(lockerOne.combination());
        lockerOne.newCombo();
        System.out.println(lockerOne);
        lockerOne.closeLocker();
        System.out.println(lockerOne);
    }
}
