#include "lists.h"
/**
 * insert_node - entry point
 * Description: inserts a new node
 * @head: head to list
 * @number: new position
 * Return: list of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *alloc, *redux;

	if (head == NULL)
		return (NULL);
	alloc = malloc(sizeof(listint_t));
	if (!alloc)
		return (NULL);
	alloc->n = number;
	if (*head == NULL)
	{
		alloc->next = *head;
		*head = alloc;
		return (*head);
	}
	redux = *head;
	if (redux->n > alloc->n)
	{
		alloc->next = redux;
		redux = alloc;
		*head = redux;
		return (redux);
	}
	for (redux = *head; redux && redux->next; redux = redux->next)
	{
		if ((redux->next)->n > alloc->n)
		{
			alloc->next = redux->next;
			redux->next = alloc;
			return (redux->next);
		}
	}
	alloc->next = NULL;
	redux->next = alloc;
	return (redux->next);
}
