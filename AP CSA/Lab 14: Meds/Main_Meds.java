public class Main_Meds {
    public static void main(String[]args){
        Meds m1 = new Meds("liquid",1000, false);
        Meds m2 = new Meds("capsule",600, true);
        Meds m3 = new Meds("capsule",500, true);
        CombineMeds cm = new CombineMeds(m2,m3);
        CombineMeds cm2 = new CombineMeds(m1,m3);
        System.out.println(cm.combine());
        System.out.println(cm.takenTogether(1200));
        System.out.println(cm2.takenTogether(1600));
        System.out.println(cm2.combine());
    }
}
