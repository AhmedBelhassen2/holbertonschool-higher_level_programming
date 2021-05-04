#include "lists.h"

/**
 * is_palindrome - Add a nodeint at the end
 * @head: header of the listint
 * @n: integer
 * Return: new nodeint
 */

int is_palindrome(listint_t **head)
{
	listint_t  *new_nodeint_end = malloc(sizeof(listint_t));
	listint_t *p;

	if (new_nodeint_end == NULL)
		return (NULL);
	new_nodeint_end->n = n;
	new_nodeint_end->next = NULL;
	if (*head == NULL)

		*head = new_nodeint_end;
	else
	{
		p = *head;
		while (p->next)
			p = p->next;
		p->next = new_nodeint_end;
	}
	return (new_nodeint_end);
}
