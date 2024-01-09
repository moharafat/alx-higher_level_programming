#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: double pointer to head of list
 * @number: number to be inserted
 * Return:  the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *before = *head;
	listint_t *after = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		if (number <= after->n && number >= before->n)
		{
			*after = *new->next;
			before->next = new;
		}
	}
	return (new);
}
