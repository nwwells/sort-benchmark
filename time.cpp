#include <iostream>
#include <sys/time.h>
#include <stdio.h>
#include <unistd.h>
#include <algorithm>
#include <vector>
#include <cstdlib> 
using namespace std;
int main(int argc, char* argv[]) {
  for (int j = 0; j < 100; ++j) {
    srand(time(NULL));
    int arraySize = 10000;
    struct timeval start, end;
    int myints[arraySize];
    for (int i = 0; i < arraySize; ++i)
      myints[i] = rand() % 100000 + 1;
    vector<int> myvector (myints, myints+arraySize);
    vector<int>::iterator it;
    long mtime, seconds, useconds;    
    gettimeofday(&start, NULL);
    sort (myvector.begin(), myvector.end());
    gettimeofday(&end, NULL);
    seconds  = end.tv_sec  - start.tv_sec;
    useconds = end.tv_usec - start.tv_usec;
    mtime = ((seconds) * 1000000 + useconds);
    printf("Elapsed time: %ld microseconds\n", mtime);
  }
}
