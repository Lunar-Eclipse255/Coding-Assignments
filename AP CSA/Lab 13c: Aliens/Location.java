public class Location {
    public static final Location JMU = new Location(38.435427, -78.872942);
    public static final Location ISAT = new Location(38.434663, -78.863732);
    private double latitude;
    private double longitude;
    /**************************************************************
    * explicit value constructor for the this Location
    *
    * @param latitude The latitude in degrees
    * @param longitude The longitude in degrees
    *************************************************************/
    public Location(double latitude, double longitude)
    {
    this.latitude = latitude;
    this.longitude = longitude;
    }
    /*************************************************************
    * equals returns true if the two values are the same within
    * .000001 of each other and false otherwise
    *
    * @return true if the two values are the same between the
    *
    two objects and false otherwise
    ************************************************************/
    public boolean equals(Location other)
    {
    return (this.latitude - other.latitude) <= .000001 && (this.longitude - other.longitude) <= .000001;
    }
    /*************************************************************
    * toString returns the latitude and longitude for this Location
    *
    * @return The string representation of this Location
    ************************************************************/
    public String toString()
    {
    return String.format("%.6f/%.6f", latitude, longitude);
    }
}
