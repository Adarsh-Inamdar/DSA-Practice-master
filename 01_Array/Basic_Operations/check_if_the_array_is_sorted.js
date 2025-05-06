// Check if the array is sorted 
let arr = [1,2,3,5,4];

const check = (arr)=>{
    for(let i = 0 ; i < arr.length-1;i++){
        if(arr[i]>arr[i+1]){
            return false
        }
    }
    return true
}

console.log(check(arr));
 