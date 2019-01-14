#pragma once
//utility methods
//pass the name of the benchmark to n, and the code to time to x
#define BENCHMARK(n, x) {\
    unsigned long benchTime = millis();\
    x\
    benchTime = millis() - benchTime;\
    Serial.print("Time to ");\
    Serial.print(n);\
    Serial.print(": ");\
    Serial.println(benchTime);\
}

//runs the code x every n milliseconds
#define RUN_EVERY(n, x) if(last_update + n < millis()) x
