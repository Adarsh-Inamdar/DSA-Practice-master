// Find the second largest element 

let arr = [1,2,3,4,4,5]
let secondMax = 0;
let max = 0;

for (let i = 0; i< arr.length; i++){
    if(max < arr[i]){
        secondMax = max;
        max = arr[i]
    }
}
console.log(secondMax);
