//Casado Natalia B. - Fiochetti Florencia - Perellón Maximiliano
//Ejercicio Torre de Hanoi

function hanoi(number_disc, init, finish){
    
  if(number_disc > 0)
    {
      hanoi(number_disc-1, init, 6-init-finish); //del actual al siguiente
      console.log("Mueve el disco "+ number_disc + " de la torre " + init + " a la torre "+ finish);
      hanoi(number_disc-1, 6-init-finish, finish); //del siguiente al final
    }
  
  
  }
hanoi(number_disc = 3,init = 1,finish = 3);
