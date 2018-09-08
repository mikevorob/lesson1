def get_summ (one, two, delimeter='&'):
	res=str(one)+str(delimeter)+str(two)
	return(res.upper())
sum=get_summ('one', 'two')
print(sum)