// 22-01-26
// 백준 함수 - 1065번 : 한수

#include <stdio.h>

int main(void)
{
	int n, han = 0;
	scanf("%d", &n);
	int one, ten, hund;

	if (n < 100) han = n;
	else if (n > 1000)return 0;
	else {
		for (int i = 100; i <= n; i++) {
			one = i % 10;
			ten = (i % 100) / 10;
			hund = i / 100;

			if ((one - ten) == (ten - hund)) {
				han++;
			}
		}
		han += 99;
	}

	printf("%d", han);
}