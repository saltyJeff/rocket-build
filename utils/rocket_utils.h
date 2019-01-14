#pragma once
//utility methods
//pass the name of the benchmark to n, and the code to time to x
//NEVER EVER USE THE PREPROCESSOR AGAIN AGHAHGAHG
#define BENCHMARK(n, x) {\
    unsigned long benchTime = millis();\
    x\
    benchTime = millis() - benchTime;\
    Serial.print("Time to ");\
    Serial.print(n);\
    Serial.print(": ");\
    Serial.println(benchTime);\
}

//the real code
#define RUN_EVERY_I(n, x, i) \
    unsigned long lastRun ##i = 0;\
    if(lastRun ##i + n < millis()) {\
        x\
        lastRun ##i = millis();\
    }
//a random masking thing so GCC doesn't catch on to the fact that i'm expanding i
#define RUN_EVERY_I_2(n, x, i) RUN_EVERY_I(n, x, i)

//replaces i (the identifier) with a unique __counter__
//runs the code x every n milliseconds
#define RUN_EVERY(n, x) RUN_EVERY_I_2(n, x, __COUNTER__)