#include<iostream>
using namespace std;
int main(){
    char c[]="GATE2011";
    char *p=c;
    cout<<p+p[3]-p[1];
}