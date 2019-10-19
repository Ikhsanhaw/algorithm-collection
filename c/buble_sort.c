#include<stdio.h>

void swap(int* l, int* r){
  *l = *l + *r;
  *r = *l - *r;
  *l = *l - *r;
}

// bsort sort array of int using bubble sort
// arr : array of int
// n : length of arr
void bsort(int arr[], int n){
  for (int i = 0; i < n-1; i++){
    for (int j = 0; j < n-i-1; j++){
      if (arr[j] > arr[j+1]){
        swap(&arr[j], &arr[j+1]);
      }
    }
  }
}
