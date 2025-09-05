let number = [1, 3, 4, 5, 6, 7]
let number2 = number
number2[0] = 55
number2
number
let number5 = [...number]
number5[0] = 90
number5

//number is also changed because both number and number2 point to the same array in memory

// To create a copy of the array, use the spread operator or slice method
let number3 = number.slice()
number3[0] = 100
number3

let [first, second, third, ...rest] = number
console.log(first, second, third, rest)
