class solution
{
public:
    int select(int arr[], int i)
    {
         
    }
     
    void selectionSort(int arr[], int i){
    int temp;
    for(int j=0;j<i;j++){
        for(int k=0;k<i-1;k++){
              if (arr[k]>arr[k+1]) 
              {
                  temp=arr[k];
                   arr[k]=arr[k+1];
                   arr[k+1]=temp;
              }
                                  
        }
       
    }
    }
};
