const
loginTel = document.querySelector(".sphone"),
errorTel = document.querySelector(".error_tel"),
sendBtn = document.querySelector(".action__btn"),
searchBtn = document.querySelector(".search__city-btn"),
searchText = document.querySelector(".search__city-name"),
clientName = document.querySelector(".sname"),
errorName = document.querySelector(".error_name");
citiesList = document.querySelector(".cities-list");


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
searchBtn.addEventListener("click", function(){
    let city = searchText.value
    $.ajax({
        url: '/addresses/?city=' + city,
        success: function(responce){
            $('.cities-list').show();
            let cities =responce.result
            cities.forEach(function(city_element){
                $('.cities-list').append(
                    "<div class=\"cities-item\"><a href=\"" + city_element.redirect_url +
                    "\"><p class=\"cities_name\">" + city_element.name_city +
                    "</p><p=\"cities_adress\">" + city_element.address +
                    "</p><p class=\"cities_phone\">" + city_element.phone_number +
                    "</p></a></div>"
                );
            });
        }
    })
});
$('.cities-list').hide();