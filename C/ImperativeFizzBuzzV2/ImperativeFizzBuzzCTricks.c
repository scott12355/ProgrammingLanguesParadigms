#include <stdio.h>

//Fizzbuzz 2 - imperative (using C tricks)

// 4 cases below:
// !(i % 3)       !(i%5)
//  0               0       //not divisible by 3 or 5
//  1               0       //divisible by 3, not by 5
//  0               1       //divisible by 5, not by 3
//  1               1       //divisible by 3 and 5
//
// !(i % 3) + 2 * !(i % 5)
//  0       + 2 *   0        = 0   "%d\n"
//  1       + 2 *   0        = 1   "Fizz\n"
//  0       + 2 *   1        = 2   "Buzz\n"
//  1       + 2 *   1        = 3   "FizzBuzz\n"

void fizzbuzz2()
{
  const char *s[] = { "%d\n", "Fizz\n", "Buzz\n", "FizzBuzz\n" };
  for (int i = 1; i <= 100; i++)
  {
    printf(s[!(i % 3) + 2 * !(i % 5)], i);
  }
}

int main()
{
    fizzbuzz2();
    return 0;
}