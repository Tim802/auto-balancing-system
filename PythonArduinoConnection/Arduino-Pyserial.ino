#include <Servo.h>

Servo ser1;
Servo ser2;
Servo ser3;
int initpos = 90;

const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];

int ang1 = 0;
int ang2 = 0;
int ang3 = 0;

boolean newData = false;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  
  ser1.attach(7);
  ser2.attach(4);
  ser3.attach(2);

  ser1.write(initpos);
  ser2.write(initpos);
  ser3.write(initpos);
}

void loop(){
  recvWithStartEndMarkers();
  if (newData == true) {
    strcpy(tempChars, receivedChars);
    parseData();
    newData = false;
  }
  ser1.write(ang1);
  ser2.write(ang2);
  ser3.write(ang3);
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void parseData(){

  char * strtokIndx;

    strtokIndx = strtok(tempChars,",");      // get the first part
    ang1 = atoi(strtokIndx); // copy it to ang1
 
    strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
    ang2 = atoi(strtokIndx);     // convert this part to an integer

    strtokIndx = strtok(NULL, ",");
    ang3 = atoi(strtokIndx); 
}