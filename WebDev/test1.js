function formatString(string) {
  {
    let prefix, rest;
    prefix = string.slice(0, 3);
    rest = string.slice(3);
    string = prefix.toUpperCase() + rest;
  }
  if (/^FOO:/.test(string)) {
    return string;
  }
  return string.slice(4);
}

console.log(formatString("foo:functioncall"));
