#include "lists.h"

/**
 * insert_node - entry point
 * Description: inserts a new node
 * @head: head to list.
 * @number: new position
 * Return: list of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *create, *temp, *auxiliar;

	temp = *head;
	create = malloc(sizeof(listint_t));

	if (create == NULL)
		return (NULL);

	while (temp != NULL)
	{
		if (temp->n > number)
			break;
		auxiliar = temp;
		temp = temp->next;
	}

	create->n = number;

	if (*head == NULL)
	{
		create->next = NULL;
		*head = create;
	}
	else
	{
		create->next = temp;
		if (temp == *head)
			*head = create;
		else
			auxiliar->next = create;
	}

	return (create);
}
