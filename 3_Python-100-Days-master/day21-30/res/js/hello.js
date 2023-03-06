function randomColor(opacity=1) {
	let r = parseInt(Math.random() * 256)
	// Math.random() 函数返回一个浮点数，伪随机数在范围从0 到小于1
	// parseInt(string, radix) 解析一个字符串并返回指定基数的十进制整数，
	let g = parseInt(Math.random() * 256)
	let b = parseInt(Math.random() * 256)
	return `rgba(${r}, ${g}, ${b}, ${opacity})`
}
