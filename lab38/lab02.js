let numbers = [1, 2, 3, 4, 5, 6];
let sum = 0;

for (let num of numbers) {
    console.log("Current number:", num);
    if (num % 2 === 0) {
        sum += num;
    }
}

console.log("Sum of even numbers:", sum);