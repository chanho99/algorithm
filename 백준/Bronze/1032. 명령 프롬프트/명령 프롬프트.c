#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int n = 0;

  scanf("%d", &n);

  char (*a)[51] = malloc(n * sizeof(char[51]));

  for(int i=0; i<n; i++){
    scanf("%s", a[i]);
  }

  int len = strlen(a[0]);
  int count = 0;

  for(int j=0; j<len; j++){
    for(int k=0; k<n; k++){
      if(a[0][j] != a[k][j]){
        count++;
        break;
      }
    }
    if (count != 0){
      printf("?");
    }
    else {
      printf("%c", a[0][j]);
    }
    count = 0;
  }

  free(a);

  return 0;
}