public class Ascii {
    public static void main(String[] args) {
        String[][] asciiArt =
        {
            {" ", " ", "_", "_", "_", " ", " "},
            {" ", "(", "o", " ", "o", ")", " "},
            {"(", " ", " ", "V", " ", " ", ")"},
            {" ", "-", "m", "-", "m", "-", " "},
        };
        asciiArt[1][2]="@";
        asciiArt[1][4]="@";
        
        for (String[] row : asciiArt)
        {
            for (String column : row) System.out.print(column);
            System.out.println();
        }
        String[][] asciiArt2 =
        {
            {"o", " ", " ", "o"},
            {" ", "_", "_", " "}
        };
        for (String[] row : asciiArt2)
        {
            for (String column : row) System.out.print(column);
            System.out.println();
        }
        for (String[] row : asciiArt2) System.out.println(String.join("",row));
    }
}
