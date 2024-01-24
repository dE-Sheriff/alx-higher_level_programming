#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
*/
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list to be freed
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)

{
	listint_t *tort, *hare, *new_head;

	if (head == NULL || *head == NULL)
		return (1);

	tort = *head;
	hare = *head;

	while (*head)
	{
		hare = hare->next->next;
		if (hare != NULL && hare->next != NULL)
			break;
		tort = tort->next;
	}
	new_head = (hare == NULL) ? tort->next : tort->next->next;

	if (new_head == NULL)
        return (1);

	tort->next = NULL;
	reverse_list(&new_head);
	print_listint(new_head);
	print_listint(*head);

	while (tort != NULL)
	{
		if ((*head)->n != tort->n)
			return (0);
		*head = (*head)->next;
		tort = tort->next;
	}
	return (1);
}
