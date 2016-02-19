#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <math.h>
unsigned long long var_num;
void *func(void *num_of_threads);//this function check if the nmber is prime 
{
	root=sqrt(number);//we have to stop searching we we arrive to number bigger than sqrt the input number
	while(num<root)
	{
		
	}
}
void run_prime_test(unsigned long long input_number, int no_of_threads)
{
	int i,num;
	pthread_t threads[no_of_threads];
	var_num=input_number;
	  if(input_number%2==0)
	      printf("%llu  number is not Prime \n");
	           return;
	              
	for(i=0;i<no_of_threads;i++)
	{
		num=3+2*i;
		pthread_create(&thread[i],NULL,func,(void*)&num);
	   
	}
	   
	
	
}

int main
{
	unsigned long long input_number;
	
	printf("Enter an unsigned long long number !\n");
	scanf("%llu",input_number);
	
	
}
