import java.lang.Math;
public class Ball{
  float x, y;
  float radius;
  float change_x, change_y;
  color c; // c = color(255,0,0,) is red
            // c = color(255) is white
  boolean check;
  boolean check2;
  public Ball(color colors){
    // write the constructor that accepts one parameter(color) 
  // randomizing the ball's position, radius, change_x
  // change_y, you must use Math.random and Java casting
  // do not use Processing's random() and Processing casting
    c=colors;
    x=(float)(Math.random()*601);
    y=(float)(Math.random()*601);
    radius = (float) (Math.random()*41)+10;
    change_x = (float) (Math.random()*12)+1;
    change_y = (float) (Math.random()*12)+1;
    check=false;
    check2 =false;
  }
  
  public Ball(int[] array, float xPos, float yPos, float r, float deltaX, float deltaY){
    //write another constructor that accepts 
  // six parameters 
    if (array.length>1){
    c = color(array[0],array[1],array[2]);
    }
    else{
      c=color(array[0]);
    }
    x= xPos;
    y= yPos;
    radius = r;
    change_x = deltaX;
    change_y = deltaY;
    check=false;
    check2 =false;
  }
 
  void display (){
    // write the display() method to draw the ball
    fill(c);
    ellipse(x,y,radius,radius);
    //Ball ballOne = new Ball(colorArray);
  }
  void update(){
    // write the update() method to move the ball
  // and bounce if it hits the right/left edge
  if (x>=width){
     check=false;
   }
   else if (x<=0){
     check=true;
 }
 if (y>=height){
     check2=false;
   }
   else if (y<=0){
     check2=true;
   }
   if (check){
     x+=change_x;
   }
   else{
    x-=change_x;
   }
   if (check2){
    y+=change_y;
   }
   else{
    y-=change_y;
    }
  }
}    
  
  
  
  
  
  
  
  
  
  
  
