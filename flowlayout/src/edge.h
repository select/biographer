#ifndef th_edge_h
#define th_edge_h
#include "headers.h"

class Edge {
public:
   Edge(int _from, int _to, Edgetype _type){   
       from=_from;
       to=_to;
       pts.type=_type;
   }       

   int from,to;
   Edgeproperties pts;
   
};

#endif






     
      
