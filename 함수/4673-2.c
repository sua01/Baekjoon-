// 22-01-25
// 백준 함수 - 4673번 : 셀프 넘버
#include <stdio.h>

int main(){
    int arr[10001];
    int res, a;

    for(int i=1; i<10001;i++){
        res = a = i;
        
        while(a>0){
            res += a%10;
            a/=10; 
        }

        if(res<=10000)
            arr[res] = 1;
    }
    

    for(int i = 1; i<10001; i++){
        if (arr[i] != 1)
            printf("%d\n", i);
    }
    
    return 0;
}

