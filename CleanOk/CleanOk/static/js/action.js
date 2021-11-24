const
loginTel = document.querySelector(".sphone"),
errorTel = document.querySelector(".error_tel"),
sendBtn = document.querySelector(".action__btn"),
clientName = document.querySelector(".sname"),
errorName = document.querySelector(".error_name");


function submitForm(evt) {
    const loginTelRegEx =  /(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}/g;
    const isTelValid = loginTelRegEx.test(loginTel.value);
    const isNameValid = clientName.value.length > 1 && clientName.value.trim() !== "";
    // loginTel.mask("+79999999999");
    // evt.preventDefault();
            if (isTelValid) {
            loginTel.classList.remove("invalid");
            errorTel.classList.add("hidden");
            } else {
                evt.preventDefault();  
                loginTel.classList.add("invalid");
                errorTel.classList.remove("hidden");
                
            }
            if (isNameValid) {
            clientName.classList.remove("invalid");
            errorName.classList.add("hidden");
            } else {
                evt.preventDefault();  
                clientName.classList.add("invalid");
                errorName.classList.remove("hidden");
                
            };
            // clientName.value = "";
            // loginTel.value = "";
        };

sendBtn.addEventListener("click", submitForm);