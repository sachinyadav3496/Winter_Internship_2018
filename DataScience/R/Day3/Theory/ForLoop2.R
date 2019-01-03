mydf <- iris
myve <- NULL # Creates empty storage container
for(i in seq(along=mydf[,1])) {
    myve <- c(myve, mean(as.numeric(mydf[i, 1:3])))
}
print(myve)