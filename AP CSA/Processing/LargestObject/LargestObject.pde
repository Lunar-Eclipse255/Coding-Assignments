Ball[] b;

void setup(){
  size(600,600);
  // draw, update and bounce balls
  //makes a color
  color c=color(100,100,100);
  //makes a list to store 100 ballls, and stores the balls
  b=new Ball[100];
  for (int i=0;i<b.length;i++){
    b[i]=new Ball(c);
  }
  
  // initialize and populate b array.
  // all ball objects have the same color
  
}

void draw(){
  //draws background
  background(0);
  //displays and updates all 100 balls
  for (int i=0;i<b.length;i++){
    b[i].display();
    b[i].update();
  }
  //gets largest ball and changes its color
  Ball largest = largest(b);
  largest.c = color(0,0,50);
  
 
  // call largest and set its color to a different color
  // than the other ball objects
}

// returns Ball that has the largest radius
// return the first one if there are multiples. 

public Ball largest(Ball[] balls) {
  //gets largest ball from the 100 and returns it
  Ball largest = balls[0];
  for(Ball i : balls){
    if (i.radius>largest.radius){
      largest=i;
    }
  }
  return largest;
}
