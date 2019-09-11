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

	new = malloc(sizeof(listint_t));
	insert = *head;
	if (insert->next->n < new->n && (head == NULL || (*head) == NULL))
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	new->n = number;
	while (insert->next != NULL && insert->next->n < new->n)
		insert = insert->next;

	new->next = insert->next;
	insert->next = new;

	return (insert);
}
