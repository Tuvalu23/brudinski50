//Team Mini-JBEE :: Ben Rudinski, Endrit Idrizi
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
function fact(n) {
    if (n == 0) return 1;
    return n * fact(n - 1);
}

//TEST CALLS
console.log(fact(1)); 
console.log(fact(2)); 
console.log(fact(3));
console.log(fact(4));
console.log(fact(5)); 

//-----------------------------------------------------------------


//fib:
function fib(n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);
}

//TEST CALLS
console.log(fib(0)); 
console.log(fib(1)); 
console.log(fib(2)); 
console.log(fib(3)); 
console.log(fib(4)); 

//=================================================================
