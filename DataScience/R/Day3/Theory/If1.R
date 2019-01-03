num1<-as.integer(readline("Enter a number: "))
num2<-as.integer(readline("Enter a number: "))
if(num1==num2){
msg1<-sprintf("First Number is %d \n", num1)
msg2<-sprintf("Second Number is %d \n", num2)
cat(msg1)
cat(msg2)
print("The entered numbers are equal")
}
