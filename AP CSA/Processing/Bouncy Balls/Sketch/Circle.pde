public class Circle

{

//instance variables including both x and y position, radius, color and Velocity in X and y directions. Color is provided.

private color c;
private int xPos;
private int yPos;
private int radius;
private int velX;
private int velY;
private boolean check;
private boolean check2;

//default constuctor you can choose values except speed set to 3 and 5

public Circle()

{

c = color(255,0,0);

xPos = 50;

yPos = 50;

radius = 50;

velX = 3;

velY = 5;

check=false;
check2=false;

}

//constructor where color is specified by parameter

public Circle(color x)

{

c = x;

xPos = 50;

yPos = 50;

radius = 50;

velX = 3;

velY = 5;

check=false;
check2=false;

}

 

//constructor

public Circle(int x, int y, color c)

{
this.c = c;

xPos = x;

yPos = y;

radius = 50;

velX = 3;

velY = 5;

check=false;
check2=false;


}



 

 

//void display function

//fills and draws the ellipse (circle) on the screen

void display()

{
  fill(c);
  ellipse(xPos,yPos,radius,radius);

}

//void move method

//updates x and y coordinates with velocities. Make sure to use if statments to keep on the screen

void move()

{

 if (xPos>=width){
     check=false;
   }
   else if (xPos<=0){
     check=true;
 }
 if (yPos>=height){
     check2=false;
   }
   else if (yPos<=0){
     check2=true;
   }
   if (check){
     xPos+=velX;
   }
   else{
    xPos-=velX;
   }
   if (check2){
    yPos+=velY;
   }
   else{
    yPos-=velY;
    }

 

}

 




}
