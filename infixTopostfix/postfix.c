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
		printf("스택이 가득찼습니다.\n");
		return;
	}
	else {
		s->data[++(s->top)] = c;
	}
}

char pop(StackType* s) {
	if (is_empty(s)) {
		printf("스택이 비었습니다.\n");
		return;
	}
	else {
		return s->data[(s->top)--];
	}
}

char peek(StackType* s) {
	return s->data[(s->top)];
}

// 연산자 우선순위 확인하기
int check_priority(char c) {
	switch (c) {
	case '(': case ')': return 0;
	case '+': case '-': return 1;
	case '*': case '/': return 2;
	}
}

// 중위표기식을 후위표기식으로 변환
void infix_to_postfix(char exp[]) {
	char c, top_c;
	int i, n = strlen(exp);
	StackType s;
	init(&s);	// 스택 초기화

	for (i = 0; i < n; i++) {
		c = exp[i];
		switch (c) {
		case '(':	// 왼쪽 괄호인 경우
			push(&s, c);
			break;
		case ')':	// 오른쪽 괄호인 경우
			top_c = pop(&s);
			while (top_c != '(') {
				printf("%c", top_c);
				top_c = pop(&s);
			}
			break;
		case '+': case '-': case '*': case '/':	// 괄호가 아닌 연산자의 경우
			while (!is_empty(&s) && check_priority(peek(&s)) >= check_priority(c)) {	// 스택 안에 들어있는 연산자의 우선순위가 더 높은 경우 pop
				printf("%c", pop(&s));
			}
			push(&s, c);
			break;
		default:	// 피연산자
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
	printf("중위표기식 : %s\n", s);
	printf("후위표기식 : ");
	infix_to_postfix(s);
	return 0;
}