import java.util.*;
public class ArrayLists {
    public static void main(String[]args){
        ArrayList<String> toDoList = new ArrayList<String>();
        toDoList.add("Do homework");
        toDoList.add("Help make dinner");
        toDoList.add("Call grandma");
        toDoList.set(1,"Order Pizza");
        System.out.println(toDoList.size()+" things to do");
        System.out.println("Here's the first thing to do "+toDoList.get(0));
        for (int i=0;i<toDoList.size()-1;i++){
            toDoList.set(i,toDoList.get(i+1));
        }
        toDoList.remove(toDoList.size()-1);
        System.out.println("Here's the first thing to do "+toDoList.get(0));
    }
    //Answer:
    //It is dynamic meaning if you remove an item it will change the 
    //length rather than just having empty spaces like an array and
    //would be even worse if you needed to add items.
}
