#pragma once
struct DATA_PACKAGE {
float demo_sin_wave;
int demo_bl4ze;
} package;
const char* PKG_START = (char*)&package;
const int PKG_LEN = sizeof(package);