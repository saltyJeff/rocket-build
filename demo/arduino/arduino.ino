#include "package.h"
extern void initialize();
extern void update();
void setup () {
  initialize();
}
void loop () {
  for(int i = 0; i < PKG_LEN; i++) {
    char a = *(PKG_START + i);
  }
  update();
}
