// test.js
const { increment, decrement } = require("./inc_dec");

// Test increment function
let result = increment(5);
console.log("Increment of 5:", result);
if (result === 6) {
  console.log("Increment test passed");
} else {
  console.error("Increment test failed");
}

// Test decrement function
result = decrement(8);
console.log("Decrement of 8:", result);
if (result === 7) {
  console.log("Decrement test passed");
} else {
  console.error("Decrement test failed");
}
