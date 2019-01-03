num<-as.integer(readline("Enter a number: "))
if(num<=0){
msg<-sprintf("The entered number is %d \n",num)
cat(msg)
print("It is negative")
}
