function dft(a)
{
	var Re = [];// 実数部
	var Im = [];// 虚数部
	var N = a.length;
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
