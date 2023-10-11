public class Alien {
    private static int alienCount;
	private static int rogueCount;
	
	private String name;			// original name
	private String homePlanet; // the home planet
	private String alias; 		// the name that they go by on earth
	private Location location;	// where the alien is currently located
	private boolean wanted;		// true if the MIB agency is looking for them.
	
	/************************************************************************
	 * default constructor - we know we have an alien but don't know much 
	 * about it. this method should increment the alien count.
	 ***********************************************************************/
	public Alien()
	{
		this("Unknown", "Unknown", Location.ISAT, "Unknown");
        alienCount++;
	}
	
	/***********************************************************************
	 * Explicit value constructor - Sets each of the attributes based on the 
	 * parameters and sets wanted to false. This method should increment the 
	 * alien count.
	 *
	 * @param name - This alien's original name
	 * @param homePlanet - The origination of this alien
	 * @param alias - The name this alien goes by on Earth
	 * @param location - The current location for this alien (after processing
	 **********************************************************************/
	public Alien(String name, String homePlanet,Location loc, String alias)
	{
        this.name =name;
        this.homePlanet=homePlanet;
        location=loc;
        this.alias=alias;
        wanted=false;
        alienCount++;
	
	}
	/*********************************************************************
	 * capturedJMU indicates an alien that has been captured and placed at 
	 * the JMU detention facility. 
	 * If the alien was a wanted criminal, then reset wanted to false and 
	 * decrement the rogueCount. In either case, this alien should be placed
	 * at the JMU location.
	 *********************************************************************/ 
	public void capturedJMU()
	{
        if (wanted==true){
            wanted=false;
            rogueCount--;
        }
        Location location=new Location(27.819142600708556, -82.63351600502762);
	}
	
	/*********************************************************************
	 * deported indicates an alien has been deported. It is possible to deport 
	 * an alien without a prior capture. If this alien is wanted, reset the 
	 * the wanted attribute to false and decrement the rogueCount. In either case, 
	 * set the location to null and decrement the alienCount.
	 *********************************************************************/
	public void deport()
	{
        if(wanted==true){
            wanted=false;
            rogueCount--;
        }
        location=null;
        alienCount--;
	}
	/**********************************************************************
	 * goneRogue identifies an alien that has violated the rules of alien
	 * immigration. If this is a new identification (wanted is false), set 
	 * wanted to true and increment the rogue count. If this alien is 
	 * already wanted do neither.
	 **********************************************************************/	
	public void goneRogue()
	{
        if (wanted==false){
            wanted=true;
            rogueCount++;
        }
	}
	/**********************************************************************
	 * move places this alien into a new location.
	 *
	 * @param newLoc The new current location
	 *********************************************************************/
	public void move(Location newLoc)
	{
        location=newLoc;
	}
	
	/********************************************************************
	 * getCurrent location returns the current location of this alien
	 * @return The current location
	 *******************************************************************/
	public Location getCurrentLocation()
	{
        return location;
	}
	
	/*******************************************************************
	 * getNumberAliens returns the total number of aliens on this planet
	 * 
	 * @return The total number of aliens (including those wanted
	 ******************************************************************/
	public static int getNumberAliens()
	{
        return alienCount;
	}
	
	/*******************************************************************
	 * getNumberWanted returns the total number of wanted aliens on the
	 * planet.
	 *
	 * @return The number of wanted aliens
	 ******************************************************************/
	public static int getNumberWanted()
	{
        return rogueCount;
	}
	
	/*******************************************************************
	 * toString displays basic information about this alien
	 *
	 * @return a String of the form: 
	 * "%s aka %s from %s currently at %s" 
	 * followed by the term "ROGUE" or the empty String depending on whether 
	 * isWanted is true or false. 
	 * If location is null, output "Off Planet" in place of the location.
	 *******************************************************************/
	public String toString()
	{
		String builder;
		String rogue;
		String location;
		
		if (this.location != null)
			location = this.location.toString();
		else
			location = "Off Planet";
		
		if(wanted)
			rogue = "ROGUE";
		else
			rogue = "";
			
		builder = String.format("%s aka %s from %s is currently at %s %s", this.name, this.alias,
		 this.homePlanet, location, rogue);
		 
		return builder;
	}
}
