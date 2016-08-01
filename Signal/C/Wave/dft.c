#include <stdio.h>
#include <math.h>
 
#define pi 3.1415926535         // 円周率

 // 離散フーリエ変換（読み込むファイル名, 書き込むファイル名）
int dft(char filename1[], char filename2[])
{  
	int k, n, N;
	int max = 100000;  // 読み込むデータ数の上限
	double f[max+1], re, im;

	FILE *fp1, *fp2;
    // ファイルオープン(フーリエ変換したいデータファイル, フーリエ変換後のデータ保存用ファイル)
	if((fp1=fopen(filename1,"r"))==NULL){
		printf("FILE1 not open\n");
        return -1;
	}
	if((fp2=fopen(filename2,"w"))==NULL){
		printf("FILE2 not open\n");
        return -1;
	}
	//データの読み込み
	for(N=0; N<max; N++) {
		if(fscanf(fp1,"%lf", &f[N]) == EOF) {
			N--;
			break;
		}
	}
	//実数部分と虚数部分に分けてフーリエ変換
	for(n=0; n<N; n++) {
		double re = 0.0;
		double im = 0.0;
		for(k=0; k<N; k++) {
			re += f[k]*cos(2*pi*k*n/N);
			im += -f[k]*sin(2*pi*k*n/N);
		}
		fprintf(fp2,"%d, %f, %f\n", n, re, im);
	}

	fclose(fp1);
	fclose(fp1);
	return 0;
}

int main()
{
	// 離散フーリエ変換
	dft("data.csv", "fourier.csv");
}
