#include <stdio.h>

int main()
{
	int num, n;
	int sum = 0;

	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%1d", &n);
		sum += n;
	}

	printf("%d", sum);
}