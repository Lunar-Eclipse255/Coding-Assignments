//create 3 ball objects here

color red;

color blue;

color green;

Circle x1;

Circle x2;

Circle x3;



void setup(){

red = color(255,0,0);

green = color(0,255,0);

blue = color(0,0,255);

size(600, 600);

background(153);

//make red ball

x1 = new Circle(70,70,red);

//make green ball

x2 = new Circle(20,20,green);

//make blue ball

x3 = new Circle(120,120,blue);

}

void draw(){
 


background(color(0,0,0));
x1.display();
x2.display();
x3.display();
 x1.move();
 x2.move();
 x3.move();

 

 

//draw them on screen

//make balls move

}
