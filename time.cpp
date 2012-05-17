#include <iostream>
#include <sys/time.h>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

const int arraySize = 1000000;

int main(int argc, char* argv[]) {
    srand(time(NULL));
    struct timeval start, end;
    int myints[arraySize];
    long mtime, seconds, useconds;    
    for (int j = 0; j < 1000; ++j) {
        for (int i = 0; i < arraySize; ++i)
            myints[i] = rand() % 100000 + 1;

        gettimeofday(&start, NULL);
        sort(myints, myints + arraySize);
        gettimeofday(&end, NULL);

        seconds  = end.tv_sec  - start.tv_sec;
        useconds = end.tv_usec - start.tv_usec;
        mtime = ((seconds) * 1000000 + useconds);
        printf("Elapsed time: %ld microseconds\n", mtime);
    }
}
