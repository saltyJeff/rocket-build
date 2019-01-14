//put link to the library containing the desired header in triple slashes after the include statement
//you can just copy the download zip link on github
#include <Adafruit_Sensor.h> ///https://github.com/adafruit/Adafruit_Sensor/archive/master.zip

#include "rocket_utils.h" //there's no auto-import for headers using the " " notation, ya'll just gotta download it to your folder

//there is an extern unsigned long last_update that is automatically filled with the millis() of the last update
extern unsigned long last_update;

//all other extern data means it will be a candidate for serialiation
float& sin_wave = package.demo_sin_wave;
int& bl4ze = package.demo_bl4ze = 420; //define constants such as BAZE_IT which can be replaced by the preprocessor. Use this for magic numbers such as pins so that the builds can be ported between chips

//for extern data we don't support multi-declarations (my regex game ain't that strong)
//BAD: extern float a,b,c;

//name your initialization loop initialize
void demo_initialize () {

}
//name your update loop update
void demo_update () {
    sin_wave = (float)sin(millis());

    //to update something every X milliseconds, use a macro from the util file
    RUN_EVERY(500, bl4ze++;) //no semicolon after macros, but end argument 2 with a semicolon
}