public class Testing{
  private static int row=0;
  private static int col=0;
  public static Location getLoc(){
    if (row==4){
      Location loc = new Location(row, col+1);
      return loc;
    }
    else if (col==4){
      Location loc = new Location(row+1,col);
      return loc;
    }
    else{
      Location loc = new Location(row, col);
      return loc;
    }

  }
}
