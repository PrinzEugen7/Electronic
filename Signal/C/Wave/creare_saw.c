#include <stdio.h>
#include <math.h>
 
 // ノコギリ波の生成（ファイル名, データ数, 最大値, 最小値, データの間隔）
createSaw(char filename[], int max, double xmax, double xmin, double dx)
{  
	int i = 0;
	int m = 0;	     
	int n=0;
	double x,y[max];

     
	FILE *fp;
    // ファイルオープン
	if((fp=fopen(filename,"w"))==NULL){
		printf("FILE not open\n");
        return -1;
    }
    // 1周期分のノコギリ波を生成
	for(x = xmin; x <= xmax; x += dx) {
		y[n]=x;
		n++;
	}
		 
	// データ数分だけノコギリ波を生成
	for(i = 0; i < 100; i++) {
		for(m=0; m<n; m++) {
			fprintf(fp,"%f\n",y[m]);
			printf("%f\n",y[m]);
		}
	}
     
	fclose(fp);    
	return 0;
}

int main()
{
	// ノコギリ波の作成
	createSaw("data.txt", 100, 1.0, -1.0, 0.1);
}
