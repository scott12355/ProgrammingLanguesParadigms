#include <stdio.h>



int main(void) {
    printf("FizzBuzz Imperative\n\n");

    for (int i = 1; i < 101; i++) {        
        if (i % 3 == 0 && i % 5 == 0) {
            printf("FizzBuzz\n");
        } else if (i % 3 == 0) {
            printf("Fizz\n");
        } else if (i % 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%i \n", i);
        }
    }
    return 0;
}
