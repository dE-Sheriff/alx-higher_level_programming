#include "lists.h"

/**
 * add_dnodeint - a function that adds a new node
 * at the beginning of a dlistint_t list
 * @head: The head of the list
 * @n: The data
 * Return: int
*/

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_h;
	dlistint_t *h = *head;

	if (head == NULL || h == NULL)
		return (NULL);

	new_h = malloc(sizeof(dlistint_t));
	if (new_h == NULL)
		return (NULL);

	new_h->prev = NULL;
	new_h->n = n;
	new_h->next = h;

	if (h != NULL)
		h->prev = new_h;

	*head = new_h;

	return (new_h);
}
