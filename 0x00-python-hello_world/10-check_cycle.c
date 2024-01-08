#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: refers to the first node (head)
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	temp = list;
	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == temp)
		{
			return (1);
		}
		if (current == NULL)
		{
			return (0);
		}
	}
	return (0);
}
