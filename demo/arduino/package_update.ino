#include "package.h"
unsigned long last_update = 0;
extern void demo_initialize();
extern void demo_update();
void initialize () {
demo_initialize();
}
void update () {
demo_update();
last_update = millis();
}