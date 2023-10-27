#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
* infinite_while - an infinite loop
* Return: 0 on success
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - main function
* Return: exit
*/

int main(void)
{
	int i;
	int x;/*Create child process*/

	for (i = 0; i < 5; i++)
	{
		x = fork();
		if (x == 0)
		{
			printf("Zombie process created, PID: %d %d\n", getpid(), i);
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
