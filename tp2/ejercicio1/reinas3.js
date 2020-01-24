//Casado Natalia B. - Fiochetti Florencia - Perellón Maximiliano
//ejercicio 3

tablero = crearTablero();

crearTableroAux();

tablero = llenarTablero2(tablero);

validacion = false;

while (validacion == false) {
    validacion = validarTablero(tablero);
    tablero = llenarCeldaOcup(tablero);

    var vJ = 0; //valor de j
    var minimaCant = 0;  
    var cantCeldasVacias = 1

    for (var i = 1; i < 8; i++) {

        tableroAux = tablero.slice(); // copia de tableroAux a tablero
        vJ = [];

        for (var j = 0; j < 8; j++) { //fila
            if (tablero[i][j] == 0) { //detecta lugares vacios
                tableroAux[i][j] = 1;

                if (minimaCant <= CeldasVacias (llenarCeldaOcup(tableroAux))) { 
                    if (minimaCant < CeldasVacias(llenarCeldaOcup(tableroAux))){
                        vJ = [];
                        vJ.push(j); // agregar un valor al tablero
                    }else{
                        vJ.push(j);
                        minimaCant = celdasAtacadas(llenarCeldaOcup(tableroAux));
                        cantCeldasVacias = 0;
                    }
                }
            }    
            tableroAux = tablero.slice();
        }
        if (cantCeldasVacias == 0){ // veo si hay lugares vacios
            var aleat = []; 
            aleat = vJ[Math.round(Math.random()*(0,vJ))]; 
            tablero = llenarCeldaOcup(tablero);
        }else{
            console.log('No queda ningun lugar vacio');
        }
        tableroAux = tablero.slice();   
    }


for (var i = 0; i < 8; i++) {
    for (var j = 0; j < 8; j++){
        if(tablero[i][j] == 2){
            tablero[i][j] = 0;
        }  
    }        
}

console.log('Tablero FINAL: \n',tablero);

}


function crearTablero() {
    
    tablero = new Array(8);
    
    for (var i = 0; i < 8; i++){
        tablero[i] = new Array(8);
    }   
    
    for (var i = 0; i < 8; i++) {
        for (var j = 0; j < 8; j++){
            tablero[i][j] == "";  
        }        
    }
    return tablero;
} 


function crearTableroAux() {
    
    tableroAux = new Array(8);
    
    for (var i = 0; i < 8; i++){
        tableroAux[i] = new Array(8);
    }   
    
    for (var i = 0; i < 8; i++) {
        for (var j = 0; j < 8; j++){
            tableroAux[i][j] == "";  
        }        
    }
    return tableroAux;
} 


function llenarTablero2(tablero){
    var aleatorio ; 
    
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            tablero[i][j] = 0;
        }
    }

    aleatorio = Math.round(Math.random()*(1,6)); //coloco una reina en una posicion aleatoria de la primer fila menos en las esquinas
    console.log('La variable aleat es',aleatorio);
    tablero[0][aleatorio] = 1 ;
        
    console.log('Tablero LLENO \n', tablero);
    return tablero;
}


function validarTablero(tablero){
    cont = 0;
    limite = 7;
    for (let i = 0; i < 7; i++) {
        aux1 = 0;
        aux2 = 0;
        aux3 = 0;
        aux4 = 0;
        aux5 = 0;
        aux6 = 0;
        for (let j = 0; j < 7; j++) {
            if (tablero[i][j] == 1) {//filas
                aux1++;
            }
            if (tablero[j][i] == 1) {//columnas console.log('Llenando celdas ocupadas \n',tablero);
                aux2++;
            }
            
            if (j <= limite) {
                if (tablero[j][j+cont] == 1) {//Diagonal superior
                    aux3++;
                }
                if (tablero[j+cont][j] == 1) {//Diagonal inferior
                    aux4++;
                }
            }
            
            if (i >= j) {
                if (tablero[j][i-j] == 1) {
                    aux5++;
                }
            }
            
            if (i+j <= 7) {
                if (tablero[(7-j)][i+j] == 1) {
                    aux6++;
                }
            }
            
            limite--;
            cont++;
    
            if (aux1 > 1 || aux2 > 1 || aux3 > 1 || aux4 > 1 || aux5 > 1 || aux6 > 1) {
                return false;
                
            }
        }
    }
    return true;
}


function llenarCeldaOcup(tablero){ // Lleno tablero en donde no pueden estar las reinas
    var acum = 0;
        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 8; j++) {
                if (tablero[i][j] == 1) { //verifico filas
                    col = j;
                    fila = i;  
                }
            }
        }     
    
    for (let i = 0; i < 8; i++) {
        if (i != fila) {
            for (let j = 0; j < 8; j++) {
                if (j != col) {
                    if (j!=col-i+fila) {
                        if (j!=col+i-fila) {
                            acum += 1;  
                        }else{
                            tablero[i][j] = 2;
                        }
                    }else{
                        tablero[i][j] = 2; 
                    }
                }else{
                    tablero[i][j] = 2;  
                }   
            }
        }else{
            for (var j= 0; j < 8; j++) {
                tablero[i][j] = 2;
            }
        }
        tablero[fila][col] = 1
    }
    console.log('Llenando celdas ocupadas \n',tablero);
    return tablero;
}


function CeldasVacias(tablero){
    acum = 0;
    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (tablero[i][j] == 0){
                acum +=1
            }        
        }
    }
    return acum;
}


function celdasAtacadas(tablero){ //celdas atacadas en la ultima fila
    acum = 0;
    ultimaF = 0;
     for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (tablero[i][j] == 1){
                 ultimaF = i;  
            }
        }
    }
      
    for (let j = 0; j < 8; j++) {
        if (tablero[ultimaF][j] == 2){
              acum +=1;
        } 
    }      
            
    return acum;
} 
    