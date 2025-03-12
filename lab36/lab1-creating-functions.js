function addNumbers(num1, num2) {
    return num1 + num2;
}

const squareNumber = (num) => num * num;

const findLargerNumber = function(num1, num2) {
    return num1 > num2 ? num1 : num2;
};

console.log("Sum of 5 and 3:", addNumbers(5, 3));
console.log("Square of 4:", squareNumber(4));
console.log("Larger number between 7 and 12:", findLargerNumber(7, 12));