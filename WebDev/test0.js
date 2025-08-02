var array = [8, 5, 3, 7];
//sort 3,5,7,8
var array1 = [100, 2, 1];
//1,10,100

//get turned into string
//sorting strings
console.log(array.sort(sortAsc));
console.log(array1.sort(sortAsc));

//context / scope;
function sortAsc(arg1, arg2) {
  if (arg1 > arg2) {
    return 0;
  }
  if (arg2 > arg1) {
    return -1;
  } else {
    return 1;
  }
}

function readhello() {
  const hello = "hello";
  const logHello = function logit() {
    return console.log(hello);
  };
  return logHello();
}

const sayhello = readhello;
sayhello();

// ==, ===

// console.log(null == undefined);

//closure

function defaultConstructor({ x = 1, y = 0 } = {}) {
  return [x, y];
}
console.log(defaultConstructor({ x: 10, y: 9 }));
console.log(defaultConstructor());
