#include <IRremote.h>

const int IR_RECEIVE_PIN = 2; // Asegúrate de que tu sensor esté conectado a este pin

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Inicializa el receptor IR
  Serial.println("Listo para recibir señales IR...");
}

void loop() {
  if (IrReceiver.decode()) {
    //Serial.print("Código recibido: 0x");
    Serial.println(IrReceiver.decodedIRData.command, HEX); // Muestra solo el comando
    IrReceiver.resume(); // Listo para recibir el siguiente código
  }
}
