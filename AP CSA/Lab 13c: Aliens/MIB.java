public class MIB {
       public static void main (String args[]){
      // this lab will violate our normal rules for placing
      // variables all at the top of the method.
      
         Alien frank;
         Alien bug;
      
         frank = new Alien("Frank", "Saturn", Location.ISAT, "Frank the Pug");
         bug = new Alien("Bug", "Romulus", new Location(38.89778, -77.0132), "Edgar");
      
         System.out.println("Aliens now 1: " + Alien.getNumberAliens());
         System.out.println("Wanted now 1: " + Alien.getNumberWanted());
      
      // next, let's move them around
         frank.move(Location.ISAT);
         bug.goneRogue();
      
         System.out.println("Aliens now 2: " + Alien.getNumberAliens());
         System.out.println("Wanted now 2: " + Alien.getNumberWanted());
      
      // Let's add a couple more
         Alien et; 
         Alien superman;
      
         et = new Alien(";opm**", "Home", new Location(38.8619, -77.0647), "ET");
         superman = new Alien("Kai-el", "Krypton", new Location(40.7306, -73.9889), "Clark Kent");
      
         System.out.println("Aliens now 3: " + Alien.getNumberAliens());
         System.out.println("Wanted now 3: " + Alien.getNumberWanted());
      
         et.deport();
         superman.goneRogue();
      
         System.out.println("Aliens now 4: " + Alien.getNumberAliens());
         System.out.println("Wanted now 4: " + Alien.getNumberWanted());
      
         bug.deport();
      
         System.out.println("Aliens now 5: " + Alien.getNumberAliens());
         System.out.println("Wanted now 5: " + Alien.getNumberWanted());
      
         Alien steve;
         steve = new Alien("Beedle", "Jupiter", new Location(38.89778, -77.0132),
            "Steven Spielberg");
      
         steve.capturedJMU();
         superman.capturedJMU();
      
         System.out.println("Aliens now 6: " + Alien.getNumberAliens());
         System.out.println("Wanted now 6: " + Alien.getNumberWanted());
      
         Alien pete;
         pete = steve;  // will we have new aliens now?
      
      // steve escapes
         steve.move(Location.ISAT);
         steve.goneRogue();
      
         System.out.println("Aliens now 7: " + Alien.getNumberAliens());
         System.out.println("Wanted now 7: " + Alien.getNumberWanted());
      
         System.out.println("\nThe final set of aliens: ");
         System.out.println(frank);
         System.out.println(bug);
         System.out.println(et);
         System.out.println(superman);
         System.out.println(steve);
         System.out.println(pete);
      
      }
}
