var obj = {
  a: 1,
  b: 2,
  c: 3,
  *[Symbol.iterator]() {
    for (let key of Object.keys(this)) {
      yield [Object.values(key), this[key]];
    }
  },
};
for (let test of obj) {
  if (test[0] == "a") {
    console.log(test[1]);
  }
}

const allKeyValue = [...obj].flat(Infinity);
const keys = [];
const values = [];

for (let i = 0; i < allKeyValue.length; i++) {
  if (i % 2 !== 0) {
    values.push(allKeyValue[i]);
  } else {
    keys.push(allKeyValue[i]);
  }
}
const paired = [];
for (let i = 0; i < keys.length; i++) {
  paired.push({ key: keys[i], value: values[i] });
}
for (let pairs of paired) {
  if (pairs.key == "b") {
    console.log(pairs.value);
  }
}
