public class Driver {
    public static void main (String[] args){
        Cat cat1 = new Cat();
        System.out.println(cat1.meow());
        System.out.println(cat1.isHealthy());
        System.out.println(cat1); // cat1.toString(); prints out memory location by default
        Cat cat2 = new Cat("Sherlock", 2, "Black and White", 5);
        System.out.println(cat2.meow());
        cat2.getDirty();
        System.out.println(cat2);
    }
}
