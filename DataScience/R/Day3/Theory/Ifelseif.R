var1<-as.integer(readline("Enter first number="))
var2<-as.integer(readline("Enter Second number="))
msg1<-sprintf("First number is %d \n", var1 )
msg2<-sprintf("Second number is %d \n", var2 )
cat(msg1)
cat(msg2)
if (var1 > var2)
{
	print("var1 is greater than var2")
}else if (var2 > var1)
{
	print("var2 is greater than var1")
}else
{
	print("var1 is equal to var2")
}