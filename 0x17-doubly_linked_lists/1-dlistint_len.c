#include "lists.h"

/**
 * dlistint_len - a function that returns
 * the number of elements in a linked dlistint_t list
 * @h: The head of the list
 * Return: int
*/

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *new_h = h;

	if (new_h == NULL)
		return (0);

	while (new_h != NULL)
	{
		new_h = new_h->next;
		count++;
	}
	return (count);
}
