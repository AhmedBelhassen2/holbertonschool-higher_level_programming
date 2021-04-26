#include "lists.h"

/**
 * add_nodeint - Add a node
 * @head: header of the listint
 * @n: the value
 * Return: An unsigned integer
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t  *new_nodeint_begin = malloc(sizeof(listint_t));

	if (new_nodeint_begin == NULL)
		return (NULL);
	new_nodeint_begin->n = n;
	new_nodeint_begin->next = *head;
	*head = new_nodeint_begin;
	return (new_nodeint_begin);
}
