public class Meds {

 

 private String type;

 private int strength;

 private boolean needH20;

 

 

public Meds(String type, int strength, boolean need)

{

 this.type = type;

 this.strength = strength;

 needH20 = need;

}

 

//Returns the type of medicine such pill, liquid, capsule, etc 

public String getType()

{

 return type;

}

//Returns the strength of medicine in whole mg

public int getStrength()

{

 return strength;

}

//Sets the quality of the medicine to this value

public void setStrength(int value)

{

 strength = value;

}

//Returns whether or not a medicine needs to be taken with water

public boolean needWater()

{

 return needH20;

}

}

