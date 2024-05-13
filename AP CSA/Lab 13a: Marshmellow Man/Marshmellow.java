public class Marshmellow {

    private int numBodyParts;
    private int numEyes;
    private int numArms;
    private int numButtons;
    private String marshmellowName;

    public Marshmellow() {
        numEyes = 2;
        numBodyParts=2;
        numArms=2;
        numButtons=2;
        marshmellowName="Two";
    }
    public Marshmellow(int eyes, int bodyParts, int arms, int buttons, String name) {
        this.numEyes = eyes;
        numBodyParts = bodyParts;
        numArms = arms;
        numButtons = buttons;
        marshmellowName = name;
    }
    public int numEyesAccesor() {
        return numEyes;
    }
    public int numBodyPartsAccesor() {
        return numBodyParts;
    }
    public int numArmsAccesor() {
        return numArms;
    }
    public int numButtonsAccesor() {
        return numButtons;
    }
    public String nameAccesor() {
        return marshmellowName;
    }
    public void newNumEyes(int eyes) {
        numEyes = eyes;
    }
    public void newNumBodyParts(int bodyParts) {
        numBodyParts = bodyParts;
    }
    public void newNumArms(int arms) {
        numArms = arms;
    }
    public void newNumButtons(int buttons) {
        numButtons = buttons;
    }
    public void newMarshmellowName(int name) {
        marshmellowName = name;
    }
}

