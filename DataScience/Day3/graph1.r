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
y1 = NA
c = 1
while (c<=20) { 
y1[c]=poly1d(x[c],m=-0.221,c=0.3);
c = c + 1 ; 
}
lines(x,y1,col='green')
points(x,y1,col='pink')