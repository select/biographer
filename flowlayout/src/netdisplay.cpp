#include <float.h>
#include "netdisplay.h"
#define SIZEX 640
#define SIZEY 480
static const vector<vector<forcevec> > dummy;
class dbgline{
   public:
      dbgline(double _x1,double _y1, double _x2, double _y2, int _r, int _g, int _b):x1(_x1),y1(_y1),x2(_x2),y2(_y2),r(_r),g(_g),b(_b){};
      double x1,y1,x2,y2;
      int r,g,b;
};
static vector<dbgline> dbglines;

void debugline(double x1,double y1, double x2, double y2, int r, int g, int b){
   dbglines.push_back(dbgline(x1,y1,x2,y2,r,g,b));
}


NetDisplay::NetDisplay(const Network &n): waitKeyPress(false), net(n),sizeX(SIZEX),sizeY(SIZEY),forces(dummy),hasforces(false){
   init();
}
NetDisplay::NetDisplay(const Network &n, vector<vector<forcevec> > &f): waitKeyPress(false), net(n),sizeX(SIZEX),sizeY(SIZEY),forces(f),hasforces(true){
   init();
}
void NetDisplay::init(){
   if(!(dpy=XOpenDisplay(NULL))) {
      fprintf(stderr, "ERROR: Could not open display\n");
      exit(1);
   }
   scr=DefaultScreen(dpy);
   rootwin=RootWindow(dpy, scr);

   win=XCreateSimpleWindow(dpy, rootwin, 1, 1, sizeX, sizeY, 0, 
         BlackPixel(dpy, scr), BlackPixel(dpy, scr));

   XStoreName(dpy, win, "biographer-layout");
   XSelectInput(dpy, win, ExposureMask|ButtonPressMask|KeyPressMask|StructureNotifyMask);
   XMapWindow(dpy, win);
   cs=cairo_xlib_surface_create(dpy, win, DefaultVisual(dpy, 0), sizeX, sizeY);
   processEvents();
   stepnum=1;
}
NetDisplay::~NetDisplay(){
	cairo_surface_destroy(cs);
	XCloseDisplay(dpy);
}
void NetDisplay::processEvents(){
   XEvent e;
   //if (!waitKeyPress) usleep(100000);
   //XFlush(dpy);
   XSync(dpy,false);
   bool cont=false;
   while((!cont && waitKeyPress) || XCheckWindowEvent(dpy,win,ExposureMask|ButtonPressMask|KeyPressMask|StructureNotifyMask,&e)) {
      if (!cont && waitKeyPress) XNextEvent(dpy, &e);
      if(e.type==Expose && e.xexpose.count<1) {
         draw();
      } else if (e.type==ConfigureNotify){
         int sx=e.xconfigure.width;
         int sy=e.xconfigure.height;
         if (sx!=sizeX || sy!=sizeY){
            sizeX=sx;
            sizeY=sy;
            cairo_xlib_surface_set_size( cs , sx , sy );
         }
      } else if(e.type==ButtonPress) {
         if (e.xbutton.button==Button2 || e.xbutton.button==Button3) waitKeyPress=!waitKeyPress;
         cont=true;
      } else if(e.type==KeyPress){
         char* key=(XKeysymToString(XLookupKeysym(&e.xkey,0)));
         //printf("key pressed: %c\n",key[0]);
         if ((key[0]>='0') && (key[0]<='9')){
            stepnum=atoi(key);
            if (stepnum==0) stepnum=10;
            cont=true;
         }
      }
   }
//   XSync(dpy,true);
}
int NetDisplay::show(){
   draw();
   processEvents();
   dbglines.clear();
   if (stepnum>1) printf("progressing %i steps\n",stepnum);
   return stepnum;
}
const unsigned short ccols[10][3]={{0,0,1},{0,1,0},{1,0,0},{1,1,0},{0,1,1},{1,0,1},{0.5,0,1},{0,0.5,1},{1,0.5,0},{0,1,0.5}};
const unsigned short fcols[10][3]={{0,0,1},{0,1,0},{1,0,0},{1,1,0},{0,1,1},{1,0,1},{0.5,0,1},{0,0.5,1},{1,0.5,0},{0,1,0.5}};
void NetDisplay::draw(){
   cairo_t *c;
   int i,j;
   int sc=net.compartments.size();
   int sn=net.nodes.size();
   int se=net.edges.size();
   double xmin=DBL_MAX;
   double ymin=DBL_MAX;
   double xmax=-DBL_MAX;
   double ymax=-DBL_MAX;
   c=cairo_create(cs); // cairo context
	cairo_set_source_rgb (c, 255, 255, 255); 
	cairo_paint (c); // clear screen
   // calculate bbox
   for (i=1;i<sc;i++){
      const Compartment &cp=net.compartments[i];
      if (xmin>cp.xmin) xmin=cp.xmin;
      if (ymin>cp.ymin) ymin=cp.ymin;
      if (xmax<cp.xmax) xmax=cp.xmax;
      if (ymax<cp.ymax) ymax=cp.ymax;
   }
   for (i=0;i<sn;i++){
      const Node &n=net.nodes[i];
      if (xmin>n.x-n.width/2) xmin=n.x-n.width/2;
      if (ymin>n.y-n.height/2) ymin=n.y-n.height/2;
      if (xmax<n.x+n.width/2) xmax=n.x+n.width/2;
      if (ymax<n.y+n.height/2) ymax=n.y+n.height/2;
   }
//   printf("bbox (%f,%f) - (%f,%f)\n",xmin,ymin,xmax,ymax);
   // set tranforms according to bbox
   double scale= ((double) sizeX)/(xmax-xmin);
   if (((double) sizeY)/(ymax-ymin)<scale) scale=((double) sizeY)/(ymax-ymin);
//   printf("dpy: (%d,%d); user: (%f,%f); scale %f\n",sizeX,sizeY,xmax-xmin,ymax-ymin,scale);
   cairo_set_line_width (c, 1/scale);
   cairo_scale(c,scale,scale);
   cairo_translate(c,-xmin,-ymin);
   // draw compartments
   for (i=1;i<sc;i++){
      const Compartment &cp=net.compartments[i];
      if (i<10) cairo_set_source_rgb(c,ccols[i][0],ccols[i][1],ccols[i][2]);
      cairo_rectangle(c,cp.xmin,cp.ymin,cp.xmax-cp.xmin,cp.ymax-cp.ymin);
      cairo_stroke(c);
//      printf("Compartment %s: (%f,%f - %f,%f) (org)\n",cp.name.c_str(),cp.xmin,cp.ymin,cp.xmax,cp.ymax);
   }
   // draw nodes
   for (i=0;i<sn;i++){
      const Node &n=net.nodes[i];
      double x=n.x;
      double y=n.y;
      cairo_user_to_device(c,&x,&y);
//      printf("Node %s: %f,%f (%f,%f) -> %f,%f\n",n.name.c_str(),n.x,n.y,n.width,n.height,x,y);
      cairo_set_source_rgb (c, 0,0,0); 
      cairo_rectangle(c,n.x-n.width/2,n.y-n.height/2,n.width,n.height);
      cairo_stroke(c);
      cairo_set_source_rgb(c,ccols[(int) n.type][0],ccols[(int) n.type][1],ccols[(int) n.type][2]);
      cairo_rectangle(c,n.x-n.width/2+1,n.y-n.height/2+1,n.width-2,n.height-2);
      cairo_stroke(c);
      cairo_move_to(c,n.x-n.width/2,n.y-n.height/2);
      cairo_show_text(c,n.name.c_str());
      cairo_set_source_rgb (c, 0,0,0); 
      cairo_set_dash (c,(double[2]){3/scale,3/scale},2,0);
      cairo_move_to(c,n.x,n.y);
      cairo_line_to(c,n.x+n.width/2*cos(n.dir),n.y+n.width/2*sin(n.dir));
      cairo_stroke(c);
      cairo_set_dash (c,NULL,0,0);
      if (hasforces){
         for (j=0;j<forces[i].size();j++){
            int col=forces[i][j].col;
            const Point &v=forces[i][j].vec;
            cairo_set_source_rgb(c,fcols[col][0],fcols[col][1],fcols[col][2]);
            cairo_move_to(c,n.x,n.y);
            cairo_line_to(c,n.x+v.x,n.y+v.y);
            cairo_stroke(c);
         }
      }
   }
   cairo_set_source_rgb (c, 0,0,0); 
   for (i=0;i<se;i++){
      const Edge &e=net.edges[i];
      const Node &n1=net.nodes[e.from];
      const Node &n2=net.nodes[e.to];
      cairo_set_dash (c,NULL,0,0);
      cairo_set_line_width(c,1/scale);
      if (e.type==catalyst || e.type==activator || e.type==inhibitor) cairo_set_dash (c,(double[2]){3/scale,3/scale},2,0);
      if (e.type==substrate) cairo_set_line_width(c,2/scale);
      double x1=n1.x;
      double y1=n1.y;
      double x2=n2.x;
      double y2=n2.y;
      double dx=x2-x1;
      double dy=y2-y1;
      double alpha1; // fraction of the line which is covered by node 1
      double alpha2; // fraction of the line which is covered by node 2
      double alpha_h;
      alpha1=fabs(n1.width/(2*dx));
      alpha_h=fabs(n1.height/(2*dy));
      if (alpha_h<alpha1) alpha1=alpha_h;
      alpha2=fabs(n2.width/(2*dx));
      alpha_h=fabs(n2.height/(2*dy));
      if (alpha_h<alpha2) alpha2=alpha_h;
      if (alpha1+alpha2>=1.0){
//         printf("edge completely covered\n");
      } else {
         x1+=dx*alpha1;
         y1+=dy*alpha1;
         x2-=dx*alpha2;
         y2-=dy*alpha2;
         cairo_move_to(c,x1,y1);
         cairo_line_to(c,x2,y2);
         cairo_stroke(c);
      }
   }
   for (i=0;i<dbglines.size();i++){
      dbgline &d=dbglines[i];
      cairo_set_source_rgb(c,(double)d.r/255,(double)d.g/255,(double)d.b/255);
      cairo_move_to(c,d.x1,d.y1);
      cairo_line_to(c,d.x2,d.y2);
      cairo_stroke(c);
   }
   cairo_show_page(c);
   cairo_surface_flush(cs);
   cairo_destroy(c);
}