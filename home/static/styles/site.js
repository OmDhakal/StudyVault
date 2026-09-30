document.addEventListener("DOMContentLoaded", () => {
    const passwordToggles = document.querySelectorAll("[data-password-toggle]");

    passwordToggles.forEach((toggle) => {
        toggle.addEventListener("click", () => {
            const input = document.getElementById(toggle.dataset.passwordToggle);
            if (!input) {
                return;
            }

            const isPassword = input.type === "password";
            input.type = isPassword ? "text" : "password";
            toggle.textContent = isPassword ? "Hide" : "Show";
            toggle.setAttribute("aria-label", `${isPassword ? "Hide" : "Show"} password`);
        });
    });

    const password = document.getElementById("id_password1");
    const confirmation = document.getElementById("id_password2");
    const form = document.querySelector("[data-register-form]");

    if (form && password && confirmation) {
        form.addEventListener("submit", (event) => {
            if (password.value !== confirmation.value) {
                event.preventDefault();
                confirmation.setCustomValidity("Passwords do not match.");
                confirmation.reportValidity();
            } else {
                confirmation.setCustomValidity("");
            }
        });

        confirmation.addEventListener("input", () => {
            confirmation.setCustomValidity("");
        });
    }
});
