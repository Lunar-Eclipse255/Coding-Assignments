
int x;
int y;
boolean check;
boolean check2;
int vx;
int vy;
void setup(){
 x=200;
 y=150;
 size(900,600);
 background(0);
 check=false;
 check2=false;
 vx=75;
 vy=60;
 } 
 void draw(){
   background(0,0,50);
   fill(0,0,255);
   ellipse(x,y,50,50);
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
     x+=vx;
   }
   else{
    x-=vx-1;
   }
   if (check2){
    y+=vy;
   }
   else{
    y-=vy;
    }
 }
 
