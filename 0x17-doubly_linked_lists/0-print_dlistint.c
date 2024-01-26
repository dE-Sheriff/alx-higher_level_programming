#include "lists.h"

/**
 * print_dlistint - a function that prints
 * all the elements of a dlistint_t list
 * @h: The head of the list
 * Return: int
*/

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *new_h = h;

	if (new_h == NULL)
		return (0);

	while (new_h != NULL)
	{
		printf("%d\n", new_h->n);
		new_h = new_h->next;
		count++;
	}
	return (count);
}
