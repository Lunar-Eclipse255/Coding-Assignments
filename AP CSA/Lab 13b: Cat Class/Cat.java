public class Cat {

    private String catName;
    private int catAge;
    private String catColor;
    private double catWeight;

    //Default Constructer 
    public Cat(){
        catName = "Cat";
        catAge = 2;
        catColor = "Black";
        catWeight = 3;
    }

    //Constructer
    public Cat(String name, int age, String color, int weight) {
        catName = name;
        catAge = age;
        catColor = color;
        catWeight = weight;
    }

    //Mutator
    public void getDirty(){
        catColor = "Brown";
    }


    //Accessor
    public String meow(){
        String sound = "Meow! " + catName;
        return sound; 
    }


    //Accessor
    public boolean isHealthy(){
        if (catWeight < 15) {
            if (catAge < 4) {
                return true;
            }
        }

        return false;
        
    }


    public String toString() {
        return ("Your cat's name is "+catName+". They weigh "+catWeight+" pounds. They are "+catColor+". They are "+catAge+" years old.");
    }

    
}
