// -----
// encoder.ino - Example for the RotaryEncoder library.
// This class is implemented for use with the Arduino environment.
//
// Copyright (c) by Matthias Hertel, http://www.mathertel.de
// This work is licensed under a BSD 3-Clause License. See http://www.mathertel.de/License.aspx
// More information on: http://www.mathertel.de/Arduino
// -----
// 18.01.2014 created by Matthias Hertel
// 04.02.2021 conditions and settings added for ESP8266
// -----

#include <Arduino.h>
#include <RotaryEncoder.h>
#include <SoftwareSerial.h>
#include <SparkFun_RV8803.h>

#define PIN_IN1 2
#define PIN_IN2 3

SoftwareSerial lcd(2, 11);
RV8803 rtc;

uint8_t minuteAlarmValue = 8; //0-60, change this to a minute or two from now to see the alarm get generated
uint8_t hourAlarmValue = 11; //0-24
uint8_t weekdayAlarmValue = SUNDAY | SATURDAY; //Or together days of the week to enable the alarm on those days.
uint8_t dateAlarmValue = 0; //1-31

#define MINUTE_ALARM_ENABLE true
#define HOUR_ALARM_ENABLE true
#define WEEKDAY_ALARM_ENABLE false
#define DATE_ALARM_ENABLE false

// Setup a RotaryEncoder with two signal input pins:
RotaryEncoder encoder(PIN_IN1, PIN_IN2, RotaryEncoder::LatchMode::FOUR3);



void checkPosition()
{
  encoder.tick(); // just call tick() to check the state.
}

void clear()
{
  lcd.write(0xFE);  // send the special command
  lcd.write(0x01);  // send the clear screen command
}

void setCursor(byte cursor_position)
{
  lcd.write(0xFE);  // send the special command
  lcd.write(0x80 + cursor_position);  // send the set cursor command
}

int lastState = LOW;

void setup()
{
  lcd.begin(9600); // initialize the lcd 

  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);

  attachInterrupt(PIN_IN1, checkPosition, CHANGE);
  attachInterrupt(PIN_IN2, checkPosition, CHANGE);

  Wire.begin();
  
  Serial.begin(115200);
  Serial.println("Set Time on RTC");

  if (rtc.begin() == false) {
    Serial.println("Something went wrong, check wiring");
  }
  else
  {
    Serial.println("RTC online!");
  }

  //Use the time from the Arduino compiler (build time) to set the RTC
  //Keep in mind that Arduino does not get the new compiler time every time it compiles. To ensure the proper time is loaded, open up a fresh version of the IDE and load the sketch.
  //Also note that due to upload times, compiler time may be a little bit off on seconds/hundredths
  if (rtc.setToCompilerTime() == false) {
    Serial.println("Something went wrong setting the time");
  }

  // Read the initial state of CLK
  rtc.disableAllInterrupts();
  rtc.clearAllInterruptFlags();//Clear all flags in case any interrupts have occurred.
  rtc.setItemsToMatchForAlarm(MINUTE_ALARM_ENABLE, HOUR_ALARM_ENABLE, WEEKDAY_ALARM_ENABLE, DATE_ALARM_ENABLE); //The alarm interrupt compares the alarm interrupt registers with the current time registers. We must choose which registers we want to compare by setting bits to true or false
  rtc.setAlarmMinutes(minuteAlarmValue);
  rtc.setAlarmHours(hourAlarmValue);
  rtc.setAlarmWeekday(weekdayAlarmValue);
  //rtc.setAlarmDate(dateAlarmValue); //Uncomment this line if you are using the date alarm instead of the weekday alarm.
  rtc.enableHardwareInterrupt(ALARM_INTERRUPT); 
}

int x = 0;

// Read the current position of the encoder and print out when changed.
void loop() {
  static int pos = 0;
  encoder.tick();
  int currentState = digitalRead(8);

  int newPos = encoder.getPosition();
  if (pos != newPos) {
    clear();
    setCursor(0);
    lcd.print("Water every: ");
    lcd.print(newPos);
    lcd.print("      days");
    pos = newPos;
    }
    
    
  if (rtc.getInterruptFlag(FLAG_ALARM)) {
      x = x + 1;
      if (x == newPos) {
        Serial.println("Alarm Triggered, clearing flag");
        digitalWrite(7, HIGH);
        int pump = 20000;
        delay(pump);
        digitalWrite(7, LOW);
        x = 0;
        rtc.clearInterruptFlag(FLAG_ALARM);
       
    }
     else {
        Serial.println("Alarm triggered, but incorrect day number");
        rtc.clearInterruptFlag(FLAG_ALARM);
        }
  }

  if (lastState != currentState) {
    if (currentState == HIGH) {
      clear();
      setCursor(0);
      lcd.print("Fill Water to       line!");
    }
    else {
      clear();
      setCursor(0);
      lcd.print("Water every: ");
      lcd.print(newPos);
      lcd.print("      days");
    }
}
// check the state of the water level senor - if high signal to the user they must refill
lastState = currentState;
}


// The End
