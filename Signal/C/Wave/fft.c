#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979


// 高速フーリエ変換
int fft(double x[], double y[], n){
    double xx, xy, z, wx[n], wy[n];
    int i, ii, il ,j , jj, k, l, l2, nv2;
	int m = 4;
    nv2 = n/2;
    j=0; 
	// 位相因子の作成(実数部 wx[i]，虚数部 wy[i])
    for (i=0; i<n; i++){
        wx[i]=cos(2*PI*i/n); 
        wy[i]=-sin(2*PI*i/n); 
    }
	
    for(i=0;i<n-1;i++) {
        if(i<j) {
            z    = x[j];
			x[j] = x[i];
			x[i] = z;
            z    = y[j];
			y[j] = y[i];
			y[i] = z;
        }
        k=nv2;
        if(k<j+1) do {j=j-k;k=k/2;} while(k<j+1);
        j=j+k;
    }
	// m段階バタフライ演算の第i段階
    for (i=1; i<=m; i++){
        l=1;
        l=l<<i;                       /* テキストの LE */
        l2=l/2;                       /* テキストの LE1 */
        jj=0;
        ii=n/l;
        for (j=0; j<l2; j++)          /* ブロック内第 j 番データを起点とする*/
        {                        /* バタフライ演算を */
            for (k=j; k<n; k=k+l)     /* 第 k/l ブロックについて実行*/
            {                          /* バタフライ演算ペアは */
                il=k+l2;                /* 第 k 番，il 番データ */
                xx=x[il]*wx[jj]-y[il]*wy[jj];
                xy=y[il]*wx[jj]+x[il]*wy[jj];
                x[il]=x[k]-xx;
                y[il]=y[k]-xy;
                x[k]=x[k]+xx;
                y[k]=y[k]+xy;
            }
            jj=jj+ii;
        }
    }
	rerurn 0;
}

int main(){
	int N = 100;
	double x[N], y[N];
    for (i=0; i<N; i++){ 
		x[i]=0;
        y[i]=0;
    } 
    fft(x, y, N);
	return 0;
}
