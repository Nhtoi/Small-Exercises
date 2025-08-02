window.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("button");

  function eventHandler(event) {
    console.log("Can only click once");
    console.log(event.target);
  }
  button.addEventListener("click", eventHandler, {
    once: true,
    passive: true,
  });
});
