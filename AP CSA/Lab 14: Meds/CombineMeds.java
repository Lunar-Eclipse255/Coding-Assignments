public class CombineMeds {
    private Meds medOne;
    private Meds medTwo;
    public CombineMeds(Meds m1, Meds m2){
        medOne = m1;
        medTwo = m2;
    }

    public boolean combine(){
        if ((medOne.getType()).equals(medTwo.getType())){
            if (medOne.needWater()==medTwo.needWater()){
                return true;
            }
        }
        return false;
    }
    public int takenTogether(int max){
        if (!((medOne.getStrength()>(2*medTwo.getStrength()))||(medTwo.getStrength()>(2*medOne.getStrength())))){
            if ((medOne.getStrength()+medTwo.getStrength())<max){
                if (medOne.needWater()==medTwo.needWater()){
                    return medOne.getStrength()+medTwo.getStrength();
                }
            }
        }
        return 0;
    }
}
