#include "lists.h"
/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: pointer to the linked list
 * Return: 1 if true and 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *start_second, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	fast = *head;
	slow = *head;
	temp = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		if (fast != NULL)
		{
			slow = slow->next;
		}
	}
	if (fast == NULL)
	{
		start_second = slow->next;
	}
	else
		start_second = slow->next;
	reverse_listint(&start_second);
	while (start_second != NULL)
	{
		if (temp->n == start_second->n)
		{
			start_second = start_second->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	return (1);
}

#include "lists.h"
/**
 * reverse_listint - pointer to the reverse function
 * @head: pointer to head of linked list
 * Return: pointer to tge first node
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *previous, *next_node;

	previous = NULL;
	next_node = NULL;

	while (*head != NULL)
	{
		next_node = (*head)->next;
		(*head)->next = previous;
		previous = (*head);
		(*head) = next_node;
	}
	*head = previous;

	return (*head);
}
