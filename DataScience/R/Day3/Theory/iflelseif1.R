a<-as.integer(readline(prompt="Enter number : "));
## check the boolean condition
if( a == 10 ) {
	## if condition is true then print the following
   	cat("Value of a is 10\n" );
	}else if( a == 20 ) {
      	## if else if condition is true
      	cat("Value of a is 20\n" );
   	} else if( a == 30 ) {
    	## if else if condition is true
      	cat("Value of a is 30\n" );
	} else {
	   	## if none of the conditions is true
    	cat("None of the values is matching\n" );
   	}
sprintf("Exact value of a is %d \n", a );