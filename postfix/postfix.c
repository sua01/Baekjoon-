#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

typedef char element;
typedef struct {
	int top;
	element data[MAX_SIZE];
} StackType;

int is_full(StackType *s) {
	return s->top == MAX_SIZE - 1;
}

int is_empty(StackType* s) {
	return s->top == -1;
}

void push(StackType* s, element c) {
	if (is_full(s)) {
		printf("������ ����á���ϴ�.\n");
		return;
	}
	else {
		s->data[++(s->top)] = c;
	}
}

char pop(StackType* s) {
	if (is_empty(s)) {
		printf("������ ������ϴ�.\n");
		return;
	}
	else {
		return s->data[(s->top)--];
	}
}

char peek(StackType* s) {
	return s->data[(s->top)];
}

// �ı�ǥ��� ���

int main() {
	int result;
	result = eval("82/3-32*+");
	print("�ı�ǥ��� ��갪 %d\n", result);
	return 0;
}

