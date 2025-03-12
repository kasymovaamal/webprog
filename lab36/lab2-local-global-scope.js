let message = "Hello from global";

function printMessage() {
    console.log(message);
}

function printLocalMessage() {
    let message = "Hello from local";
    console.log(message);
}

printMessage();
printLocalMessage();