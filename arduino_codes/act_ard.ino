#include <SPI.h>

const int ss = 10;
long int val7 = 0;
long int val6 = 0;
long int val8 = 0;
long int val9 = 0;
long int val10 = 0;
long int val11 = 0;
long int val12 = 0;
long int val13 = 0;
long int val14 = 0;
long int val15 = 0;
long int val16 = 0;
long int val17 = 0;
long int take_reading(void);
void switch_to_x(void);
void switch_to_y(void);
void ads_sleep(void);
void ads_wakeup(void);
void sync_conv(void);

int i=0;

void setupPWM16() {
    DDRB |= _BV(PB1) | _BV(PB2);        /* set pins as outputs */
    TCCR1A = _BV(COM1A1) | _BV(COM1B1)  /* non-inverting PWM */
        | _BV(WGM11);                   /* mode 14: fast PWM, TOP=ICR1 */
    TCCR1B = _BV(WGM13) | _BV(WGM12)
        | _BV(CS10);                    /* no prescaling */
    ICR1 = 0x0400;                      /* TOP counter value */
}  
void analogWrite16(uint8_t pin, uint16_t val)
{
    switch (pin) {
        case  9: OCR1A = val; break;
        case 10: OCR1B = val; break;
    }
}
void setup() {
  // put your setup code here, to run once:
digitalWrite(3,OUTPUT);
digitalWrite(5,OUTPUT);
digitalWrite(6,OUTPUT);
tone(3,60000);
setupPWM16();
  Serial.begin(500000);
  pinMode(ss,OUTPUT);  
  TCCR0B = TCCR0B & B11111000 | B00000001; //prescaler is set to 1 with base frequency of 62.5KHz
 // analogWrite(3,128);
  tone(3,60000);
  digitalWrite(ss, HIGH);
  SPI.begin();
  delayMicroseconds(600);
  //FOR RESETTING
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00000110);//reset
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();

  //FOR SELF OFFSET CALLIBRATION
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B01100010);//SELFCAL
  SPI.transfer(B11111111);
  SPI.transfer(B11111111);
  SPI.transfer(B11111111);
  SPI.transfer(B11111111);
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
 
  //FOR STOPPING CONTINOUS MODE
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00010110);//SDATAC
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();

  //FOR SETTING INTERNAL REFERENCE
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B01000010);// WREG
  SPI.transfer(B00000000); // FOR WRITING 1 BYTE
  SPI.transfer(B00110000); // FOR SELECTING INTERNAL REFERENCE IN MUX1
  SPI.transfer(B11111111); // NOP?
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();

  //FOR SETTING PGA AND DATA RATE
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B01000011);// WREG
  SPI.transfer(B00000000); // FOR WRITING 1 BYTE
  SPI.transfer(B00011000); // FOR SETTING PGA=120, 320SPS in SYS0
  SPI.transfer(B11111111); // NOP?
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
  
  //FOR SYNC ADC CONVERSIONS
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00000100);//SYNC
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();

  switch_to_x();
}

void loop() {
  // put your main code here, to run repeatedly:
for(int i=0;i<1023;i=i+200)
{
analogWrite16(9, i);

  for(int j=0;j<=255;j=j+1)
  {
    analogWrite(5,j);
    //delay(10);
    float x_reading = (float)((analogRead(A0)*5.0)/1023)*1000;
    for(int k=0;k<3;k++){
    x_reading = (x_reading + (float)((analogRead(A0)*5.0)/1023)*1000)/2;
    //analogWrite(5,(45*x_reading));
    }
    x_reading = (x_reading + (3)*val6 + (3)*val7 + (3)*val10)/10;
    
//    Serial.print(",");
   val10=val7;
   val7=val6;
   val6 = x_reading;

   float y_reading = (float)((analogRead(A1)*5.0)/1023)*1000;
    for(int k=0;k<3;k++){
    y_reading = (y_reading + (float)((analogRead(A1)*5.0)/1023)*1000)/2;
    //analogWrite(5,(45*x_reading));
    }
    y_reading = (y_reading + (3)*val8 + (3)*val9 + (3)*val9)/10;

//    Serial.print(",");
   val11 = val9;
   val9 = val8;
   val8 = y_reading;

   float current = x_reading;
   float voltage = (y_reading - x_reading);
    Serial.print(current);
    Serial.print(",");
    Serial.println(voltage);
//    Serial.println(y_reading);
  }
  val6=val7=val8=val9=val10=val11=0;
}
}

long int take_reading(){
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00010010);//RDATA
  byte a=SPI.transfer(B11111111); //NO  OP
  byte b=SPI.transfer(B11111111); //NO  OP
  long int value = (((a<<8)| b)>>5)*32;
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
  return value;
}

 void switch_to_y()
{
  //FOR SWITCHING TO FETCH STEP INPUT
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B01000000);// WREGINTO MUX0
  SPI.transfer(B00000000); // FOR WRITING 1 BYTE
  SPI.transfer(B00011110); // FOR SELECTING AIN2 as positive input and AIN3 as negative input
  SPI.transfer(B11111111); // NOP?
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
}

 void switch_to_x()
{
  //FOR SWITCHING TO FETCH RAMP INPUT
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B01000000);// WREGINTO MUX0
  SPI.transfer(B00000000); // FOR WRITING 1 BYTE
  SPI.transfer(B00100110); // FOR SELECTING AIN3 as positive input and AIN6 as negative input
  SPI.transfer(B11111111); // NOP?
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
}

void sync_conv()
{
  //FOR SYNC ADC CONVERSIONS
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00000100);//SYNC
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
}

void ads_wakeup()
{
  //WAKEUP
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00000000);//WAKEUP
  SPI.transfer(B11111111);//NOP
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
  
}

void ads_sleep()
{
  //SLEEP
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00000010);//SLEEP
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
}
