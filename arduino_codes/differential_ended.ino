#include <SPI.h>

const int ss = 10;
const int start = 9;
const int drdy = 3;
long int old_val=0;

long int take_reading(void);
void switch_to_x(void);
void switch_to_y(void);
void ads_sleep(void);
void ads_wakeup(void);
void sync_conv(void);
void setup() {
  
  Serial.begin(500000);
  pinMode(ss,OUTPUT);
  pinMode(start,OUTPUT);
  pinMode(4,OUTPUT);
  digitalWrite(start,HIGH);
  digitalWrite(ss, HIGH);
  digitalWrite(4,HIGH);
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
  SPI.transfer(B00101001); // FOR SETTING PGA=1, 2000SPS in SYS0
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

 // switch_to_y();sync_conv();
}

void loop() {

  digitalWrite(4,LOW);
  digitalWrite(4,HIGH);
  long int val = take_reading();
  long int val1 = take_reading();
  long int val2 = take_reading();
  long int x_reading=(val + val1+ val2)/3;
  switch_to_y();sync_conv();
  long int val3 = take_reading();
  long int val4 = take_reading();
  long int val5 = take_reading();
  long int y_reading=(val3 + val4+ val5)/3;
  switch_to_x();sync_conv();
  Serial.println(String(x_reading)+","+String(y_reading));
}

long int take_reading(){
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B00010010);//RDATA
  byte a=SPI.transfer(B11111111); //NO  OP
  byte b=SPI.transfer(B11111111); //NO  OP
  long int value = (((a<<8)| b));
  return value;
  delayMicroseconds(1.75);
  digitalWrite(ss,HIGH);
  SPI.endTransaction();
}

 void switch_to_y()
{
  //FOR SWITCHING TO FETCH STEP INPUT
  SPI.beginTransaction(SPISettings(200000,MSBFIRST,SPI_MODE1));
  digitalWrite(ss,LOW);
  delayMicroseconds(0.01);
  SPI.transfer(B01000000);// WREGINTO MUX0
  SPI.transfer(B00000000); // FOR WRITING 1 BYTE
  SPI.transfer(B00010001); // FOR SELECTING AIN2 as positive input and AIN1 as negative input
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
  SPI.transfer(B00000001); // FOR SELECTING AIN0 as positive input and AIN1 as negative input
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

