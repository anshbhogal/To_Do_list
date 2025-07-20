document.addEventListener("DOMContentLoaded", () => {
  const signUpBtn = document.getElementById("signUp");
  const signInBtn = document.getElementById("signIn");
  const container = document.getElementById("container");

  if (signUpBtn && signInBtn && container) {
    signUpBtn.addEventListener("click", () =>
      container.classList.add("right-panel-active")
    );
    signInBtn.addEventListener("click", () =>
      container.classList.remove("right-panel-active")
    );
  }
});
