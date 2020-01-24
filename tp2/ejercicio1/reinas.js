//Casado Natalia B. - Fiochetti Florencia - Perellón Maximiliano
//ejercicio 1 

//Matriz correcta usada para prueba
/*var tablero = [
    [0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0]
  ]; */

tablero = crearTablero();

llenarTablero(tablero);

console.log(tablero)

validacion = false;

validar();

function validar() {
    while (validacion == false) {
        validacion = validarTablero(tablero);
        console.log('Validacion:', validacion);
    }
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
    console.log('tablero creadoo \n');
    return tablero;
} 


function llenarTablero(tablero){
	var aleatorio ; 
	
	for (let i = 0; i < 8; i++) {
		for (let j = 0; j < 8; j++) {
			tablero[i][j] = 0;
		}
	}

	for (let i = 0; i < 8; i++) {
		aleatorio = Math.round(Math.random()*(0,7));
		console.log('la variable aleat es',aleatorio);
        tablero[i][aleatorio] = 1 ;
	}  

	console.log('tablero lleno \n');
	return tablero;
}


function validarTablero(tablero){
    console.log(tablero);

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
            if (tablero[i][j] == 1) {//Comprueba filas
                aux1++;
            }
            if (tablero[j][i] == 1) {//Comprueba columnas
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

