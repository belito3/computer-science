// A C program to demonstrate working of 
// fork() and process table entries. 
// use cmd "ps -eaf | grep "defunct"" to find entry zoobie process 
#include<stdio.h> 
#include<unistd.h> 
#include<sys/wait.h> 
#include<sys/types.h> 

int main() 
{ 
	int i; 
	int pid = fork(); 

	if (pid == 0) 
	{ 
		for (i=0; i<20; i++) 
			printf("I am Child\n"); 
	} 
	else
	{ 
		printf("I am Parent\n"); 
		while(1); 
	} 
} 

