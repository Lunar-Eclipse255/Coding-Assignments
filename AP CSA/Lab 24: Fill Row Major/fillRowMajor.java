public class fillRowMajor {
    public static String[][] fillRowMajor(String str, int rows, int cols){
        String[][] filled = new String[rows][cols];
        int counter =0;
        for (int i=0;i<rows;i++){
            for (int j=0;j<cols;j++){
                if(counter<(str.length())){
                    filled[i][j]=str.substring(counter,counter+1);
                    counter++;
                }
            }
        }
        return filled;
    }
    public static void main(String[] args) {
        String[][] result = fillRowMajor("do more", 3, 4);
        for(String[] rows: result){
            for(String cols: rows){
                System.out.print(" \""+cols+"\" ");
            }
            System.out.println();
        }
    }
}
