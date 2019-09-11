#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert a node in a sorted linked list
 *
 * @head: value passed main
 * @number: value of node to be inserted
 *
 * Return: insert node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *insert;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	new->n = number;
	insert = *head;
	if ((*head) == NULL)
	{
		*head = new;
		return (*head);
	}

	if (number < insert->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (insert->next != NULL && insert->next->n < new->n)
		insert = insert->next;

	new->next = insert->next;
	insert->next = new;

	return (insert);
}
