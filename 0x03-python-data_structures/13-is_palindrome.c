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
	listint_t *tort, *hare, *hare_head;

	if (head == NULL || *head == NULL)
		return (1);

	tort = *head;
	hare = *head;

	while (hare != NULL || hare->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;
	}
	hare_head = malloc(sizeof(listint_t));

	if (hare == NULL)
		hare_head = tort->next;
	else if (hare->next == NULL)
		hare_head = tort->next->next;

	reverse_list(&hare_head);
	while (tort != NULL)
	{
		if ((*head)->n != tort->n)
		return (0);

		*head = (*head)->next;
		tort = tort->next;
	}
	free(hare_head);
	return (1);
}
