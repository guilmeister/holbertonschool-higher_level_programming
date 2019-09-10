#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - check if linked list is a loop
 *
 * @list: value passed main
 *
 * Return: 1 if a loop | 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL)
		return (0);

	while (first != NULL && second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
