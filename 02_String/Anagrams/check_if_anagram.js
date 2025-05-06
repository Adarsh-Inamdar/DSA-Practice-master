// Function to check if two strings are anagrams
let string1 = "carrrr";
let string2 = "arcccc";

let anag1 = string1.split("");
let anag2 = string2.split("");

let obj = {};

if (anag1.length === anag2.length) {
    for (let i = 0; i < anag1.length; i++) {
        obj[anag1[i]] = (obj[anag1[i]] || 0) + 1;
        obj[anag2[i]] = (obj[anag2[i]] || 0) - 1;
    }
}

console.log(obj);