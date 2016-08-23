function main()
{
	data = new Array(0, 2, 3, 3, 2, 0, 2, 3, 3, 2, 0); 
	alert( "計算結果　:　" + dft(data).Re ); // フーリエ変換後のデータ（実部）を表示
	//alert( "計算結果　:　" + dft(data).Re ); // フーリエ変換後のデータ（虚部）を表示
}

function dft(a)
{
	var Re = [];// 実部
	var Im = [];// 虚部
	var N = a.length; // サンプル数
	// DFTの計算
	for( var j=0; j<N; ++j ){
		var re = 0.0;
		var im = 0.0;
		for( var i=0; i<N; ++i ){
			var th = 2*Math.PI/N * j * i;
			re += a[i] * Math.cos(th);
			im += a[i] * Math.sin(th);
		}
		Re.push(re);
		Im.push(im);
	}
	return {'Re':Re, 'Im':Im};
}
