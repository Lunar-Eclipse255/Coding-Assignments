public class Cat {

    private String catName;
    private int catAge;
    private String catColor;
    private int catWeight;

    //Default Constructer 
    public void Cat(){
        catName = "Cat";
        catAge = 2;
        catColor = "Black";
        catWeight = 3;
    }

    //Constructer
    public void cat(String name, int age, String color, int weight) {
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
        String sound = "Meow!"+ catName;
        return sound; 
    }


    //Accessor
    public boolean isHealthy(){
        if (catWeight >= 15) {
            if (catAge >= 4) {
                return false;
            }
        }
        return true;
    }

    
}
