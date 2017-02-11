

#include "rad_def.inc"

global_settings { radiosity { Rad_Settings(Radiosity_Normal, off, off) } }


sky_sphere {
  pigment {
    gradient y
    color_map {
      [ 0.0 color rgb <0.8, 0.8, 1.6> ]
      [ 0.5 color rgb <0.0, 0.0, 0.0> ]
      [ 1.0 color rgb <0.8, 0.8, 1.6> ]
    }
    scale <1, 2, 1>
    translate -y
  }
}

light_source {
  <3, 5, 5>*20
  color rgb <0.95, 0.78, 0.42>
  area_light
  10*x, 10*z,
  4, 4
  jitter
  orient
}

camera {
  location <00, 0, 3>*10     // Position de la caméra
        look_at <0,0,0>    
  sky   <0,0,1>           // Ne pas modifier
  right <-1,0,0>          // Ne pas modifier
}

// ===== 1 ======= 2 ======= 3 ======= 4 ======= 5 ======= 6 ======= 7 ======= 8 ======= 9 ======= 10
 

 #declare Rp=0.5;  
 #declare nb=20;
 #declare ti=0;       // début et fin du paramètre
 #declare tf=6.285;
   #declare dt=0.002;   //Pour le calcul des dérivées
   #declare ddt=0.00001;   //Pour le calcul des dérivées

 
   
#macro M(tt) // courbe paramètrique de période 2pi 
  <3*cos(tt)+5*cos(3*tt),
   3*sin(tt)+5*sin(3*tt),  
   sin(5*tt/2)  *sin(3*tt)+sin(4*tt)-sin(6*tt)
  >
 
#end       
/*
#macro M(tt) // courbe paramètrique de période 2pi 
  <cos(10*tt)*5,
   sin(10*tt)*5,  
   tt
  >
#end  
   */      

#macro M(tt) // courbe paramètrique de période 2pi 

#include "formule_de_M.pov"
#end

#declare HH=0.0001;
#macro vv(tt) //vecteur vitesse
  (M(tt+dt/2)-M(tt-dt/2))/dt
 
#end 
#macro nv(tt) // courbe paramètrique de période 1     
  #declare vt= vv(tt) ;
  sqrt(vt.x*vt.x+vt.y*vt.y+vt.z*vt.z)
 
#end               

#macro aa(tt) // courbe paramètrique de période 1 
  (vv(tt+dt/2)-vv(tt-dt/2))/dt
 
#end   



 

#macro Affiche_courbe(Rb) 
        #declare tt=ti;
        #while (tt<=tf)                
                 sphere { M(tt) Rb
                         texture {pigment { color rgb <1, 1, 1> }
                         finish {ambient color rgb <0, 0, 0>   diffuse 1   }   
                         }}
                              
                 #declare tt=tt+2*Rb/nv(tt) ;
        #end   

#end  

#macro M_spirale1(tt,Rs,P)
     #declare e1= vv(tt)/nv(tt) ;
      #declare e1=e1/  sqrt(e1.x*e1.x+e1.y*e1.y+e1.z*e1.z);
     #declare e2=<-e1.y,e1.x,0>;
     #if (e2.x=0  & e2.y=0)    #declare e2=<-e1.z,0,e1.x>;  #end 
     #declare e2=e2/  sqrt(e2.x*e2.x+e2.y*e2.y+e2.z*e2.z);
     #declare e3=<e1.y*e2.z-e1.z*e2.y, -(e1.x*e2.z-e1.z*e2.x), e1.x*e2.y-e1.y*e2.x>;
     (M(tt)+e2*Rs*cos(P*tt)+e3*Rs*sin(P*tt))
#end  

#macro vv_spirale1(tt,Rs,P) //vecteur vitesse
  ((M_spirale1(tt+ddt/2,Rs,P)-(M_spirale1(tt-ddt/2,Rs,P)))/ddt);
/*  #declare M1=M_spirale1(tt+ddt/2,Rs,P);
  #declare M2=M_spirale1(tt-ddt/2,Rs,P);
  ((M1-M2)/ddt)
 */
#end 
#macro nv_spirale1(tt,Rs,P) // 
  #declare vvts= vv_spirale1(tt,Rs,P) ;
  sqrt(vvts.x*vvts.x+vvts.y*vvts.y+vvts.z*vvts.z)
 
#end               


#macro Affiche_courbe_spirale1(Rs,P,Rb) 
        #declare tt=ti;
        #while (tt<=tf)                
                 sphere { M_spirale1(tt+clock,Rs,P) Rb
                         texture {pigment { color rgb <1, 1, 1> }
                         finish {ambient color rgb <0, 0, 0>   diffuse 1   }   
                         }}
                              
                 #declare tt=tt+2*Rb/nv_spirale1(tt+clock,Rs,P);
        #end   

#end  

//Affiche_courbe(0.4) 
Affiche_courbe_spirale1(1,100,0.2)  

/*

 #declare eM= M_spirale1(1+ddt/2,0.6,100)  ;   

    text {
    ttf "timrom.ttf" concat(str(eM.x,8,8),",",str(eM.y,8,8),",",str(eM.z,8,8))+ 4, 0
    texture {pigment { color rgb <1, 1, 1> }   }
    translate <0,7,0>
  } 
  
   #declare eM= M_spirale1(1-ddt/2,0.6,100)  ;
    text {
    ttf "timrom.ttf"  concat(str(eM.x,8,8),",",str(eM.y,8,8),",",str(eM.z,8,8)) 4, 0
    texture {pigment { color rgb <1, 1, 1> }   }
    translate <0,4,0>
  }
   
  text {
    ttf "timrom.ttf" str(nv_spirale1(1,0.6,100),5,5) 4, 0
    texture {pigment { color rgb <1, 1, 1> }   }
    translate <0,10,0>
  }
  
   text {
    ttf "timrom.ttf" str(nv_spirale1(1,0.6,50),5,5) 4 0
    texture {pigment { color rgb <1, 1, 1> }  }
    translate <0,-5,0>
  }

*/