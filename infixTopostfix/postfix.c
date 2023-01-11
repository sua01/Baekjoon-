#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

typedef char element;
typedef struct {
	int top;
	element data[MAX_SIZE];
} StackType;

void init(StackType* s) {
	s->top = -1;
}

int is_full(StackType* s) {
	return s->top == MAX_SIZE - 1;
}

int is_empty(StackType* s) {
	return s->top == -1;
}

void push(StackType* s, char c) {
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

// ������ �켱���� Ȯ���ϱ�
int check_priority(char c) {
	switch (c) {
	case '(': case ')': return 0;
	case '+': case '-': return 1;
	case '*': case '/': return 2;
	}
}

// ����ǥ����� ����ǥ������� ��ȯ
void infix_to_postfix(char exp[]) {
	char c, top_c;
	int i, n = strlen(exp);
	StackType s;
	init(&s);	// ���� �ʱ�ȭ

	for (i = 0; i < n; i++) {
		c = exp[i];
		switch (c) {
		case '(':	// ���� ��ȣ�� ���
			push(&s, c);
			break;
		case ')':	// ������ ��ȣ�� ���
			top_c = pop(&s);
			while (top_c != '(') {
				printf("%c", top_c);
				top_c = pop(&s);
			}
			break;
		case '+': case '-': case '*': case '/':	// ��ȣ�� �ƴ� �������� ���
			while (!is_empty(&s) && check_priority(peek(&s)) >= check_priority(c)) {	// ���� �ȿ� ����ִ� �������� �켱������ �� ���� ��� pop
				printf("%c", pop(&s));
			}
			push(&s, c);
			break;
		default:	// �ǿ�����
			printf("%c", c);
			break;
		}
	}
	while (!is_empty(&s)) {
		printf("%c", pop(&s));
	}
}

int main(void) {

	char* s = "(a+b)*c";
	printf("����ǥ��� : %s\n", s);
	printf("����ǥ��� : ");
	infix_to_postfix(s);
	return 0;
}