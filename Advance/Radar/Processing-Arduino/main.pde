int w=400,h=400;
int i=0;
int deg=0;
void setup() {
  size(400, 400);
}
 
void draw() {
  background(0, 20, 0);
  strokeWeight(2);
  stroke(0, 130, 0);
  fill(0, 20, 0);
  ellipse(w/2, h/2, w, w);
  ellipse(w/2, h/2, w/2, w/2);
  line(0, h/2, w, h/2);
  line(w/2, 0, w/2, h);
  for(i=0;i<50;i++){
    float dx = w/2 * cos(radians(deg-i)) + w/2;
    float dy = h/2 * sin(radians(deg-i)) + h/2;
    line(w/2, h/2, dx, dy);
  }
  deg++;
}
