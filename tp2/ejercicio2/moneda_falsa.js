//Casado Natalia B. - Fiochetti Florencia - Perellón Maximiliano
//Ejercicio Moneda falsa

class Monedas {
    constructor(nombre, peso) {
        this.nombre = nombre;
        this.peso = peso;
    }
}

console.log("/******************MONEDAS******************/")
console.log("\n")
var mn1 = new Monedas("Moneda 1", 100);
var mn2 = new Monedas("Moneda 2", 100);
var mn3 = new Monedas("Moneda 3", 100);
var mn4 = new Monedas("Moneda 4", 100);
var mn5 = new Monedas("Moneda 5", 100);
var mn6 = new Monedas("Moneda 6", 100);
var mn7 = new Monedas("Moneda 7", 100);
var mn8 = new Monedas("Moneda 8", 100);
var mn9 = new Monedas("Moneda 9", 100);
var mn10 = new Monedas("Moneda 10", 100);
var mn11 = new Monedas("Moneda 11", 100);
var mn12 = new Monedas("Moneda 12", 100);

//Moneda aleatoria
var mn = Math.floor((Math.random() * (12-0))+0); 

//Peso de la moneda aleatoria
var pm = 100;
while (pm == 100) {
    pm = Math.floor((Math.random() * (105-95))+95); 
}

var monedas = new Array(mn1, mn2, mn3, mn4, mn5, mn6, mn7, mn8, mn9, mn10, mn11, mn12);
monedas[mn] = new Monedas(monedas[mn].nombre, pm);
console.log(monedas);
console.log("\n")

var izquierda = new Array(monedas[0], monedas[1], monedas[2], monedas[3]);
var derecha = new Array(monedas[4], monedas[5], monedas[6], monedas[7]);
var mesa = new Array(monedas[8], monedas[9], monedas[10], monedas[11]);

console.log("Buscando moneda falsa...")

//*********Pesaje**********//

// Equilibrado

//Primer pesaje equilibrado
if (pesaje(izquierda, derecha) == 3) { 
    var pesaje_izq = new Array(monedas[0], monedas[1], monedas[2]);
    var pesaje_der = new Array(monedas[8], monedas[9], monedas[10]);

    //Segundo pesaje equilibrado
    if (pesaje(pesaje_izq, pesaje_der) == 3) { 
        var pesaje_izq1 = new Array(monedas[0]);
        var pesaje_der1 = new Array(monedas[11]); 

        //Tercer pesaje
        if (pesaje(pesaje_izq1, pesaje_der1) == 1) {//izquierda
            console.log("La moneda falsa es la: " + monedas[11].nombre + " y pesa menos.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[11].nombre + " y pesa más.")      
        }
    }

    //Segundo pesaje a la izquierda
    else if (pesaje(pesaje_izq, pesaje_der) == 1) {
        var pesaje_izq1 = new Array(monedas[8]);
        var pesaje_der1 = new Array(monedas[9]); 

        //Tercer pesaje 
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[10].nombre + " y pesa menos.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[9].nombre + " y pesa menos.")      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[8].nombre + " y pesa menos.")      
        }
    }

    //Segundo pesaje a la derecha
    else if (pesaje(pesaje_izq, pesaje_der) == 2) {
        var pesaje_izq1 = new Array(monedas[8]);
        var pesaje_der1 = new Array(monedas[9]); 

        //Tercer pesaje
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[10].nombre + " y pesa más.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[9].nombre + " y pesa más.")      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[8].nombre + " y pesa más.")      
        }
    }
}

// Izquierda

//Primer pesaje a la izquierda
else if (pesaje(izquierda, derecha) == 1) { 
    var pesaje_izq = new Array(monedas[0], monedas[1], monedas[4], monedas[5]);
    var pesaje_der = new Array(monedas[6], monedas[8], monedas[9], monedas[10]);

    //Segundo pesaje equilibrado
    if (pesaje(pesaje_izq, pesaje_der) == 3) { 
        var pesaje_izq1 = new Array(monedas[2], monedas[7]);
        var pesaje_der1 = new Array(monedas[8], monedas[9]); 

        //Tercer pesaje
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[3].nombre + " y pesa más.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[2].nombre + " y pesa más.")      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[7].nombre + " y pesa menos.")      
        }
    }

    //Segundo pesaje a la izquierda
    else if (pesaje(pesaje_izq, pesaje_der) == 1) {
        var pesaje_izq1 = new Array(monedas[1], monedas[6]);
        var pesaje_der1 = new Array(monedas[8], monedas[9]); 

        //Tercer pesaje 
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[0].nombre + " y pesa más.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[1].nombre + " y pesa más.")      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[6].nombre + " y pesa menos.")      
        }
    }

    //Segundo pesaje a la derecha
    else if (pesaje(pesaje_izq, pesaje_der) == 2) {
        var pesaje_izq1 = new Array(monedas[4]);
        var pesaje_der1 = new Array(monedas[8]); 

        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[5].nombre + " y pesa menos.");      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[4].nombre + " y pesa menos.")      
        }
    }
}

// Derecha

//Primer pesaje a la derecha
else if (pesaje(izquierda, derecha) == 2) { 
    var pesaje_izq = new Array(monedas[0], monedas[1], monedas[4], monedas[5]);
    var pesaje_der = new Array(monedas[6], monedas[8], monedas[9], monedas[10]);

    //Segundo pesaje equilibrado
    if (pesaje(pesaje_izq, pesaje_der) == 3) { 
        var pesaje_izq1 = new Array(monedas[2], monedas[7]);
        var pesaje_der1 = new Array(monedas[8], monedas[9]); 

        //Tercer pesaje
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[3].nombre + " y pesa menos.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[7].nombre + " y pesa más.")      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[2].nombre + " y pesa menos.")      
        }
    }

    //Segundo pesaje a la derecha
    else if (pesaje(pesaje_izq, pesaje_der) == 2) {
        var pesaje_izq1 = new Array(monedas[1], monedas[6]);
        var pesaje_der1 = new Array(monedas[8], monedas[9]); 

        //Tercer pesaje
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[0].nombre + " y pesa menos.");
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[6].nombre + " y pesa más.")      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 2) { //derecha
            console.log("La moneda falsa es la: " + monedas[1].nombre + " y pesa menos.")      
        }
    }

    //Segundo pesaje a la izquierda
    else if (pesaje(pesaje_izq, pesaje_der) == 2) {
        var pesaje_izq1 = new Array(monedas[4]);
        var pesaje_der1 = new Array(monedas[8]); 

        //Tercer pesaje 
        if (pesaje(pesaje_izq1, pesaje_der1) == 3) {//equilibrado
            console.log("La moneda falsa es la: " + monedas[5].nombre + " y pesa más.");      
        } else if(pesaje(pesaje_izq1, pesaje_der1) == 1) { //izquierda
            console.log("La moneda falsa es la: " + monedas[4].nombre + " y pesa más.")      
        }
    }
}

function pesaje(izquierda, derecha) {
    var p1 = 0, p2 = 0;	
    var pesada = 0;

    for (let i = 0; i < izquierda.length; i++) {
        p1 += izquierda[i].peso;
        p2 += derecha[i].peso;
    }	
    if (p1 > p2) {
        pesada = 1; //Izquierda
    } else if (p1 < p2){
        pesada = 2; //Derecha
    } else {
        pesada = 3; //Equilibrado
    }
    return pesada;
}