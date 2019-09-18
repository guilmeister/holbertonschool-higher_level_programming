#include "lists.h"

int is_palindrome(listint_t **head)
{
	return checkpalindrome(&(*head), (*head));
}

int checkpalindrome(listint_t **left, listint_t *right)
{
	int res;

	if (right == NULL)
		return (1);

	res = checkpalindrome(left, right->next) && ((*left)->n == right->n);
	(*left) = (*left)->next;

	return res;
}
