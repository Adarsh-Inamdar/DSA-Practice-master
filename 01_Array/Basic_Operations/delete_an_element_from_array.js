// Delete an element from array 

// JavaScript program to delete the first occurrence of an
// element in the array using custom method

let arr = [ 10, 20, 20, 20, 30 ];
let ele = 20;
let n = arr.length;

console.log("Array before deletion");
for(let i = 0; i < n; i++)
	console.log(arr[i]);

let found = false;
for (let i = 0; i < n; i++) {

    // If the element has been found previously,
    // shift the current element to the left
    if (found) {
        arr[i - 1] = arr[i];
    }

    // check if the current element is equal to
    // the element to be removed
    else if (arr[i] === ele) {
        found = true;
    }
}

// If element was found, reduce the size of array
if (found === true) {
    n--;
}

console.log("\nArray after deletion");
for (let i = 0; i < n; i++) {
   console.log(arr[i] + " ");
}