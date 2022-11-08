#include<iostream>
using namespace std;


void print(int arr[],int n){
    for(int i=0;i<n-2;i++){
        int current=arr[i];
        int min=i;


        for(int j=i;j<n;j++){
            if(arr[j]<arr[min])
            min=j;
        }
         swap(arr[min],arr[i]);
    }
   
}



int main(){
    int arr[]={1,3,5,7,9,2,45};
    int n=sizeof(arr)/sizeof(int);
    // cout<<n;


s
// for(int i=0;i<n;i++){
//     cout<<arr[i]<<" ";
// }
// cout<<endl;
for(auto x:arr)
cout<<x<<" ,";

// print
 print(arr,n);
cout<<endl;
 for(auto x:arr)
cout<<x<<" ,";


}