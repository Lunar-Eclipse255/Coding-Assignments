public class Testing {
    public static void main(String[]args){

        Contact c = new Contact("Alice", "555-1234");

        c.doSomething();
        
        c = new Contact("Daryl", "");
        
        c.doSomething();

    }
}
