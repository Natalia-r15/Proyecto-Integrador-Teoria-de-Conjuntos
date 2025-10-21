#include <stdio.h>

#define MAX 10 

// Conjuntos
char emisores[MAX]; //arrleglo para guardar los emisores con las restricciones de que el máximo a guardar serán 10(MAX 10)
char receptores[MAX];
int llaves[MAX];

// Conexiones (E, K, R)
char conexionesE[MAX];
char conexionesR[MAX];
int conexionesK[MAX];

//variables para llevar un conteo de cuántos datos se van ingresando
int numEmisores = 0, numReceptores = 0, numLlaves = 0, numConexiones = 0;

//función para agregar un emisor
void agregarEmisor() {
    char emisor;
    if (numEmisores < MAX) {
        printf("Ingresa el nombre del emisor: ");
        scanf(" %c", &emisor); 
        emisores[numEmisores]=emisor; //guardamos el emisor del usuario en nuestro arreglo de emisores
        numEmisores++;
    } else printf("Límite de emisores alcanzado.\n");
}

void eliminarEmisor() {
    char nombre;
    int encontrado = 0; //encontrado es nuestra bandera para saber si lo encontró o no
    printf("Emisor a eliminar: ");
    scanf(" %c", &nombre);
    for (int i = 0; i < numEmisores; i++) {
        if (emisores[i]==nombre) { //emisores[i] accede a la posición de los emisores y verifica su caracter
            for (int j = i; j < numEmisores - 1; j++) //si se encuentra al emisor, recorremos el arreglo hasta el penúltimo número de emisores 
                emisores[j]=emisores[j + 1]; //se actualiza la posición, copia el valor de la posición siguiente (j + 1) a la posición actual (j).
            numEmisores--; //se va eliminando la cantidad de emisores en cada iteración 
            encontrado = 1; //si lo encuentra llegamos a nuestra bandera y dejamos de buscar al emisor
            break;
        }
    }
    if (!encontrado) printf("Emisor no encontrado.\n");
    //j siendo la posición donde encontramos al emisor (i)

}

void agregarReceptor() {
    if (numReceptores < MAX) {
        printf("Ingresa el nombre del receptor: ");
        scanf(" %c", &receptores[numReceptores]);
        numReceptores++;
    } else printf("Límite de receptores alcanzado.\n");
}

void eliminarReceptor() {
    char nombre;
    int encontrado = 0;
    printf("Receptor a eliminar: ");
    scanf(" %c", &nombre);
    for (int i = 0; i < numReceptores; i++) {
        if (receptores[i]==nombre) {
            for (int j = i; j < numReceptores - 1; j++)
                receptores[j]=receptores[j + 1];
            numReceptores--;
            encontrado = 1;
            break;
        }
    }
    if (!encontrado) printf("Receptor no encontrado.\n");
}

//LLAVES
void agregarLlave() {
    if (numLlaves < MAX) {
        printf("Ingresa el valor de la llave: ");
        scanf("%d", &llaves[numLlaves]);
        numLlaves++;
    } else printf("Límite de llaves alcanzado.\n");
}

void eliminarLlave() {
    int llave, encontrado = 0;
    printf("Llave a eliminar: ");
    scanf("%d", &llave);
    for (int i = 0; i < numLlaves; i++) {
        if (llaves[i] == llave) {
            for (int j = i; j < numLlaves - 1; j++)
                llaves[j] = llaves[j + 1];
            numLlaves--;
            encontrado = 1;
            break;
        }
    }
    if (!encontrado) printf("Llave no encontrada.\n");
}

//CONEXIONES
void crearConexion() {
    if (numConexiones < MAX) {
        char emisor, receptor;
        int llave, i, duplicado = 0;
        //i siendo un indice para recorrer las posiciones de cada conexión
        //duplicado siendo nuestra bandera para saber si una conexión existe o no

        printf("Emisor: ");
        scanf(" %c", &emisor);
        printf("Llave: ");
        scanf("%d", &llave);
        printf("Receptor: ");
        scanf(" %c", &receptor);

        // Verificar duplicado
        for (i = 0; i < numConexiones; i++) {
            if (conexionesE[i] == emisor && conexionesR[i] == receptor && conexionesK[i] == llave)
        //se comprueba que las conexiones de nuestro arreglo sean iguales a los valores que el usuario ingresó dependiendo de la posición i
            duplicado = 1; //si se cumple toda la condición se marca nuestra bandera para no volverla a agregar
        }

        if (!duplicado) { //si no se encuentra un duplicado se agrega la conexión
            conexionesE[numConexiones] = emisor; //mete al nuevo emisor en la lista de conexiones en orden
            conexionesR[numConexiones] = receptor;
            conexionesK[numConexiones] = llave;
            numConexiones++; //el número de conexiones aumenta en 1 para no repetir la posición
            printf("Conexión creada: ( %c, %d, %c)\n", emisor, llave, receptor);
        } else {
            printf("Conexión duplicada.\n");
        }
    } else printf("Límite de conexiones alcanzado.\n");
}
void mostrarDatos() {
    printf("\nEmisores = {");
    for (int i = 0; i < numEmisores; i++) {
        printf(" %c", emisores[i]);
        if (i < numEmisores - 1) printf(", ");
    }
    printf("}\n");

    printf("Receptores = {");
    for (int i = 0; i < numReceptores; i++) {
        printf(" %c", receptores[i]);
        if (i < numReceptores - 1) printf(", ");
    }
    printf("}\n");

    printf("Llaves = {");
    for (int i = 0; i < numLlaves; i++) {
        printf("%d", llaves[i]);
        if (i < numLlaves - 1) printf(", ");
    }
    printf("}\n");

    printf("Conexiones = [");
    for (int i = 0; i < numConexiones; i++) {
        printf("( %c, %d, %c)", conexionesE[i], conexionesK[i], conexionesR[i]);
        if (i < numConexiones - 1) printf(", ");
    }
    printf("]\n");
}

//VERIFICACIÓN DE FUNCIONES
void verificarFuncion() {
    int esFuncion = 1, inyectiva = 1, sobreyectiva = 1;

    //Función: Cada elemento de A tiene una y solo una flecha hacia B
    //se verifica si cada emisor se conecta solo a un receptor 
    for (int i = 0; i < numConexiones; i++) { //recorre todas las conexiones
        for (int j = i + 1; j < numConexiones; j++) { //recorre desde i+1 para no repetir comparación de pares
            if (conexionesE[i] == conexionesE[j] && conexionesR[i] != conexionesR[j])
            //si 2 conexiones tienen el mismo emisor pero receptores distintos, no es función
                esFuncion = 0; //si no cumple las condiciones de función, esFuncion cambia su valor a 0
        }
    }

    //Inyeciva: No hay dos elementos de A que apunten al mismo elemento de B
    //se verifica que ningún receptor se repite
    for (int i = 0; i < numConexiones; i++) {
        for (int j = i + 1; j < numConexiones; j++) {
            if (conexionesR[i] == conexionesR[j])
                inyectiva = 0;
        }
    }

    //Sobreyectiva: No hay ningún elemento en B que se quede sin una flecha que le apunte
    //se verifica que cada receptor tiene al menos un emisor
    for (int i = 0; i < numReceptores; i++) {
        int encontrado = 0;
        for (int j = 0; j < numConexiones; j++) {
            if (receptores[i] == conexionesR[j])
            //se comprueba que todos las conexiones del receptor sean las mismas que la cantidad de receptores
                encontrado = 1;
        }
        if (!encontrado)
            sobreyectiva = 0;
    }

    printf("\nVerificación de propiedades de funciones:\n");
    printf("- Es función: %s\n", esFuncion ? "SI" : "NO");
    printf("- Inyectiva: %s\n", inyectiva ? "SI" : "NO");
    printf("- Sobreyectiva: %s\n", sobreyectiva ? "SI" : "NO");
    printf("- Biyectiva: %s\n", (inyectiva && sobreyectiva) ? "SI" : "NO");
}

void verificarRelacion() {
    int reflexiva = 0, simetrica = 1, transitiva = 1; //se inician en 1 porque buscamos contraejemplos

    //Reflexiva: (a, a) todo elemento de A está relacionado consigo mismo
    for (int i = 0; i < numConexiones; i++) {
        if (conexionesE[i] == conexionesR[i]) //si encuentra un par donde emisor = receptor (a, a)
            reflexiva = 1; //marca que existe al menos un elemento reflexivo
    }

    //Simétrica: si (a, b) -> debe existir (b, a)
    for (int i = 0; i < numConexiones; i++) {
        int existeSimetrica = 0; //bandera para el par actual: se asume que NO tiene simétrico
        for (int j = 0; j < numConexiones; j++) {
            if (conexionesE[i] == conexionesR[j] && conexionesR[i] == conexionesE[j])
        //verifica que el emisor del par i es igual al receptor del par j, Y el receptor del par i es igual al emisor del par j
                existeSimetrica = 1;
        }
        if (!existeSimetrica)
            simetrica = 0;
    }

    //Transitiva: si (a, b) y (b, c) -> debe existir (a, c)
    for (int i = 0; i < numConexiones; i++) { //recorre cada par i (a, b)
        for (int j = 0; j < numConexiones; j++) { //recorre cada par j (b, c)
            if (conexionesR[i] == conexionesE[j]) { //si el receptor del par i es igual al emisor del par j 
                int existe = 0; //se marca una bandera de que si existe el par (a,c)
                for (int k = 0; k < numConexiones; k++) { //busca el par (a, c)
                    if (conexionesE[i] == conexionesE[k] && conexionesR[j] == conexionesR[k])
                    //si el emisor del par i es igual al emisor del par k y el receptor del par j es igual al receptor del par k
                        existe = 1; //se marca una bandera de que existe el par (a,c)
                        break; //salimos del bucle
                }
                if (!existe)
                    transitiva = 0; //si no existe este par, no hay transitividad
            }
        }
    }

    printf("\nVerificación de propiedades de relaciones:\n");
    printf("- Reflexiva: %s\n", reflexiva ? "SI" : "NO");
    printf("- Simétrica: %s\n", simetrica ? "SI" : "NO");
    printf("- Transitiva: %s\n", transitiva ? "SI" : "NO");
}
// ===== MENÚ PRINCIPAL =====
int main() {
    int opcion;
    do {
        printf("\n--- MENÚ PRINCIPAL ---\n");
        printf("1. Agregar Emisor\n2. Eliminar Emisor\n3. Agregar Receptor\n4. Eliminar Receptor\n");
        printf("5. Agregar Llave\n6. Eliminar Llave\n7. Crear Conexión\n");
        printf("8. Verificar Propiedades de Función\n9. Verificar Propiedades de Relación\n10. Mostrar todos los conjuntos\n");
        printf("0. Salir\n");
        printf("Opción: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1: agregarEmisor(); break;
            case 2: eliminarEmisor(); break;
            case 3: agregarReceptor(); break;
            case 4: eliminarReceptor(); break;
            case 5: agregarLlave(); break;
            case 6: eliminarLlave(); break;
            case 7: crearConexion(); break;
            case 8: verificarFuncion(); break;
            case 9: verificarRelacion(); break;
            case 10: mostrarDatos(); break;
        }
    } while (opcion != 0);

    return 0;
}
