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
	listint_t *after;

	after = before->next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	after = before->next;
	while (after != NULL)
	{
		if (number <= after->n && number >= before->n)
		{
			new->next = after;
			before->next = new;
			return (new);
		}
			before = after;
		after = after->next;
	}
	before->next = new;
	return (new);
}
