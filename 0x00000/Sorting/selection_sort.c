#include <stdio.h> 
  
void swap(int *xp, int *yp) 
{ 
	int temp;
	temp = *xp; 
	*xp = *yp; 
	*yp = temp; 
}
void selectionSort(int arr[], int n) 
{ 
	int i, j, min_idx;
	for (i = 0; i < n - 1; i++)
	{
		min_idx = i;
		for(j + 1; j < n; j++)
		{
			if (arr[j] < arr[min_idx])
				min_idx = j;
		}
		if (min_idx != i)
			swap
	}
}