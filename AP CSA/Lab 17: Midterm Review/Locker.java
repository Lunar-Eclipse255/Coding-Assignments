import java.lang.Math;
public class Locker {
    private String name;
    private int lockerCombo;
    private String hall;
    private boolean status;
    private String location;
    public static int lockerNum=0;
    public Locker(String name, String hall){
        this.name=name;
        this.hall=hall;
        lockerCombo=(int) (Math.random()*(2000)+1);
        status=false;
        lockerNum++;
        if (lockerNum%2==0){
            location = "Bottom";
        }
        else{
            location="Top";
        }
    }
    public void newCombo(){
        lockerCombo=(int) (Math.random()*(2000)+1);
    }
    public void openLocker(int combo){
        if (combo==lockerCombo) {
            status=true;
        }
    }
    public void closeLocker(){
        status=false;
    }
    public String position(){
        return location;
    }
    public String whichHall(){
        return hall;
    }
    public int combination() {
        return lockerCombo;
    }
    public boolean lockerStatus(){
        return status;
    }
    public String toString(){
        if (status){
            return ("Locker Number: "+lockerNum+" Hall: "+hall+" Position: "+location+" Combonation: "+lockerCombo+ " Status: Open");
        }
        return ("Locker Number: "+lockerNum+"; Hall: "+hall+"; Position: "+location+"; Combination: "+lockerCombo+ "; Status: Closed");
    }
    
}