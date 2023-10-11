public class Contact

{

private String contactName;

private String contactNumber;

public Contact(String name, String number)

{

contactName = name;

contactNumber = number;

}

public void doSomething()

{

System.out.println(this);

}

public String toString()

{

return contactName + " " + contactNumber;

}

}