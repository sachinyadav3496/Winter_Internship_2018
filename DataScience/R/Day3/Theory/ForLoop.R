## Implementing For loop
## To square the values in the given Vector
## Creating Vector of 10 values

forvector<-seq(from=2, to=22, by=2)

## Creating Empty vector to store the output
squaredVector=NULL

## Applying for loop
for (i in 1:length(forvector)){
squaredVector[i]=forvector[i]^2
print(squaredVector[i])
}