#include <stdio.h>

int main()
{
	int num, n, a;

	scanf("%d", num);
	scanf("%d", n);

	int sum = 0;

	while (n > 0) {
		sum += n % 10;
		n /= 10;
	}

	printf("%d", sum);
}