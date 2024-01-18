#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - a function in C that checks
 * if a singly linked list has a cycle in it
 * @list: link to list to be checked
 * Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	listint_t *tort, *haire;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	tort = list->next;
	haire = list->next->next;
	while (tort && haire && list->next)
	{
		if (tort == haire)
			return (1);
	tort = list->next;
	haire = list->next->next;
	}
	return (0);
}
