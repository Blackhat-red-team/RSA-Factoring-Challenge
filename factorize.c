#include "factor.h"

/**
 * factorisze - The fun factorisze a numbers
 * @buffer: pointer is the addres of numbers
 *
 * Author: ibrahim said
 * Return: int
 */
int factorisze(char *buffer)
{
u_int32_t nums;
u_int32_t k;

nums = atoi(buffer);

for (k = 2; k < nums; k++)
{
if (nums % k == 0)
{
printf("%d=%d*%d\n",nums,nums/k,k);
break;
}
}
return (0);
}
