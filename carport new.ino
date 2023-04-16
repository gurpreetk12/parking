#include<ESP8266WiFi.h>
#include<Firebase_ESP_Client.h>
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"

#define DATABASE_URL "http://parkit-f33d5-default-rtdb.firebaseio.com/"
#define API_KEY "AIzaSyCtLv9WjKfJdOM6LQ-VBP9uOWCPdklBr0E"
//uF3IeAjJrGEVq0LiZJiQZiwzn7fUpUuYTX8skw2d
int slot1 = 0;
int slot2 = 0;
int slot3 = 0;
int slot4 = 0;

FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;
bool signupOK= false;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  WiFi.disconnect();
  delay(2000);
  Serial.print("Start connection");
  WiFi.begin("seriously_magnetic","magnetic");
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(100);

  }
  Serial.println("Connected");
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  if(Firebase.signUp(&config,&auth,"" , "")){
    Serial.println("ok");
    signupOK=true;
  }
  else{
    Serial.printf("%s\n",config.signer.signupError.message.c_str());
  }
  config.token_status_callback = tokenStatusCallback;
  Firebase.begin( &config ,&auth);
  Firebase.reconnectWiFi(true);


}

void loop() {
  slot1=digitalRead(D1);
  slot2=digitalRead(D2);
  slot3=digitalRead(D5);
  slot4=digitalRead(D4);
  
  
  if(Firebase.ready() && signupOK){
    Firebase.RTDB.setFloat(&fbdo,"/nodemcu1/slot1",slot1);
    Firebase.RTDB.setFloat(&fbdo,"/nodemcu1/slot2",slot2);
    Firebase.RTDB.setFloat(&fbdo,"/nodemcu1/slot3",slot3);
    Firebase.RTDB.setFloat(&fbdo,"/nodemcu1/slot4",slot4);
  }
  delay(1000);

}
