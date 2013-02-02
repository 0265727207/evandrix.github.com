#include<stdio.h>

int g[81][11];

int tile(int x)
{
	int a;
	for(a=1; a<10 && x<81 && !g[x][10]; a++)
		g[x][a] = 1;

	for(a=0; a<9 && x<81 && !g[x][10]; a++)
		g[x][g[x/9*9+a][0]] = g[x][g[x%9+9*a][0]] = g[x][g[x%9/3*3+x/27*27+a/3*9+a%3][0]] = 0;

	for(a=0; a<10 && x<81; a++)
		if(g[x][a])
		{
			g[x][0] = a?a:g[x][10];

			if(tile(x+1))
				return printf(x%9?"%d ":"%d \n",g[x][0])|1;
		}

	g[x][0] = g[x][10];
	return x>80;
}

int main()
{
	int x, row;
	char c[9];
	for(x=0, row=0; row<9 && x<81 && (x%9 || scanf("%s",c)|1); x++)
	{
		if (x%9 == 0) row++;
		g[80-x][10] = g[80-x][0] = (c[x%9]-48);
	}

	return tile(0);
}
