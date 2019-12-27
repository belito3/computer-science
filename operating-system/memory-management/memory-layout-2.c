#include<stdio.h>
#include<stdlib.h>
#pragma GCC optimize ("O0")

// uninitialized variable
int g1;
int g2;

//iniatialized variable
int g3=5;
int g4=7;

// function to test stack
void func2() {
	int var1;
	int var2;
	printf("On Stack through func2:\t\t %u %u\n",&var1,&var2);
}

void func() {
	int var1;
	int var2;
	printf("On Stack through func:\t\t %u %u\n",&var1,&var2);
	func2();
}

int main(int argc, char* argv[], char* evnp[]) {
	
	// Command line arguments
	printf("Cmd Line and Env Var:\t\t %u %u %u\n",&argc,argv,evnp);
	
	// Local variable will go to stack and stack should grow downward
	int var1;
	int var2;
	printf("On Stack through main:\t\t %u %u\n",&var1,&var2);
	func();
	
	// Dynamic Memory should go to heap and should be increasing
	void *arr1 = malloc(5);
	void *arr2 = malloc(5);
	printf("Heap Data:\t\t\t\t\t %u\n",arr2);
	printf("Heap Data:\t\t\t\t\t %u\n",arr1);
	free(arr1);
	free(arr2);
	
	// Uninitialized and iniatialized Global Variable
	printf("Global Uniniatialized:\t\t %u %u\n",&g1,&g2);
	printf("Global iniatialized:\t\t %u %u\n",&g3,&g4);
	
	//Static Code must go to Text section
	printf("Text Data:\t\t\t\t\t %u %u %u ",main,func,func2);
	return 0;
}
