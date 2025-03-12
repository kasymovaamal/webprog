function parseJSON(jsonStr) {
    try {
        let parsedObj = JSON.parse(jsonStr);
        console.log(parsedObj);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseJSON('{"name": "Alice", "age": 25}');
parseJSON('{"name": "Alice", "age": 25');