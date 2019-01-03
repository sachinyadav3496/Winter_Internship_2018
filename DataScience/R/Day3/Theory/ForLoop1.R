## For loop for printing 2 table
## Taking input from user
num<-as.integer(readline(prompt="Enter a number= "))
for (i in 1:10){
print(paste(num,'x',i,'=',num*i))
}