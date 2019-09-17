#include "lists.h"

/**
 * is_palindrome - entry point
 * Description: checks list is palindrome
 * @head: ** head of list
 * Return: 1 or 0 or empty
 */
int is_palindrome(listint_t **head)
{
	listint_t *actual;
	int s[2500], pos = 0, l = 0, r = 0;

	if ((head == NULL) || (*head == NULL))
		return (1);
	actual = *head;
	while (actual)
	{
		s[pos] = actual->n;
		actual = actual->next;
		pos++;
	}
	if (pos == 1)
		return (1);
	l = pos / 2 - 1;
	if ((pos % 2) == 0)
		r = pos / 2;
	else
		r = pos / 2 + 1;
	while (l != 0)
	{
		if (s[l] != s[r])
			return (0);
		l--;
		r++;
	}
	return (1);
}
