#include "TinyGPS++.h"
#include "SoftwareSerial.h"

SoftwareSerial serial_connection(10, 11);
TinyGPSPlus gps;

void setup()
{
    Serial.begin(9600);
    serial_connection.begin(9600);
    Serial.println("GPS Start");
}

/**
 * Função principal de loop do Arduino responsável por processar dados do GPS.
 * 
 * - Lê dados disponíveis da conexão serial e decodifica usando a biblioteca GPS.
 * - Quando uma nova localização é recebida, extrai latitude e longitude.
 * - Verifica se a localização está dentro de áreas específicas (alas e salões) com base em coordenadas pré-definidas.
 * - Exibe no Serial Monitor o nome da ala e/ou salão correspondente, ou informa se está fora dessas áreas.
 * - Também imprime informações adicionais como latitude, longitude, número de satélites, velocidade (mph) e altitude (pés).
 * 
 * Observação: Os limites das áreas (alas e salões) são definidos por intervalos de latitude e longitude.
 */
void loop()
{
    while(serial_connection.available())
    {
        gps.encode(serial_connection.read());
    }
    if(gps.location.isUpdated())
    {
        double lat = gps.location.lat();
        double lng = gps.location.lng();

        String ala = "";
        String salao = "";

        if (lat >= 39.122000 && lat <= 39.123000 && lng >= -121.025000 && lng <= -121.024000) {
            ala = "Ala 1";
        } else if (lat >= 39.124000 && lat <= 39.125000 && lng >= -121.026000 && lng <= -121.025000) {
            ala = "Ala 2";
        }

        if (lat >= 39.126000 && lat <= 39.127000 && lng >= -121.027000 && lng <= -121.026000) {
            salao = "Salao A1";
        } else if (lat >= 39.128000 && lat <= 39.129000 && lng >= -121.028000 && lng <= -121.027000) {
            salao = "Salao A2";
        } else if (lat >= 39.130000 && lat <= 39.131000 && lng >= -121.029000 && lng <= -121.028000) {
            salao = "Salao A3";
        }

        if (ala != "" && salao != "") {
            Serial.print(ala);
            Serial.print(" e ");
            Serial.println(salao);
        } else if (ala != "") {
            Serial.println(ala);
        } else if (salao != "") {
            Serial.println(salao);
        } else {
            Serial.println("Fora das alas e saloes");
        }

        Serial.println(lat, 6);
        Serial.println(lng, 6);
        Serial.println(gps.satellites.value());
        Serial.println(gps.speed.mph());
        Serial.println(gps.altitude.feet());
        Serial.println("");
    }
}
