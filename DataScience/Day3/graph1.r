poly1d <- function(x,m=1,c=1){
return(m*x+c);
}
x = sample(1:50,20)
y = NA
index = 1
y = NA
while ( index <= length(x) ) {
y[index] = poly1d(x[index],m=-0.134,c=0.3);
index = index + 1 ;
}
plot(x,y,col='red',type='l')
points(x,y,col='blue')
y1 = 