import java.util.*;
import java.lang.Math;
import java.lang.reflect.Field;
public class Testing{
    public static void main (String[] args){
        String str1 = new String("Advanced Placement");

String str2 = new String("Advanced Placement");

if (str1.equals(str2) && str1 == str2)

{

System.out.println("A");

}

else if (str1.equals(str2) && str1 != str2)

{

System.out.println("B");

}

else if (!str1.equals(str2) && str1 == str2)

{

System.out.println("C");

}

else if (!str1.equals(str2) && str1 != str2)

{

System.out.println("D");

}
    }
}
