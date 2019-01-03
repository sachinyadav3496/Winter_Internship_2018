SquareFunction<-function(Int_vect,is.vector(Int_vect))
{
  while(is.vector(Int_vect)==FALSE){
    print("Input is not a vector")
    break;
    }
  squaredVector<-Int_vect*2
  return(squaredVector)
}
