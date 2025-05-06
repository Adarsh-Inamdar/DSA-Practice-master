// Find maximum and minimum in array 

let arr = [1,2,3,4,5,5,6,-2]

const linearApproch = (arr)=>{
    let min = 0;
    let max = 0;
    for (let i = 0; i<arr.length;i++){
        if(max < arr[i]){
            max = arr[i]
        }
    
        if(min > arr[i]){
            min = arr[i]
        }
    }
    return {max:max,min:min};
}

const bySorting = (arr)=>{
    for(let i = 0;i<arr.length-1;i++){
        for(let j = i+1;j < arr.length;j++){
            if(arr[i]<arr[j]){
                let temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
    return {min:arr[arr.length-1],max:arr[0]};
}

console.table({linear:linearApproch(arr),sorting:bySorting(arr)});
