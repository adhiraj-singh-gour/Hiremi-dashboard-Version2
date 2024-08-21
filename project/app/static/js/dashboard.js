// for side nav bar
const doctToRight = document.querySelector("#dock-to-left")
const sideNav = document.querySelector(".side-navbar-container")
const sideNavOption = document.querySelectorAll(".side-navbar-container li a span")
const sideNavh1 = document.querySelectorAll(".side-navbar-container h1")
const sideNavIcon = document.querySelectorAll(".side-navbar-container li a i")


// console.log(doctToRight);
// console.log(sideNav);
// console.log(sideNavOption);
// console.log(sideNavh1);
// console.log(sideNavIcon);


function displayNone() {
    sideNavOption.forEach((span) => {
        span.style.display = "none"
    });
    sideNavh1.forEach((h1) => {
        h1.style.display = "none"
    })
}
function displayBlock() {
    sideNavOption.forEach((span) => {
        span.style.display = "block"
    });
    sideNavh1.forEach((h1) => {
        h1.style.display = "block"
    })
}

doctToRight.addEventListener("click", () => {
    if (sideNav.style.width === "60px") {
        sideNav.style.width = "100%"
        displayBlock()
        sideNavIcon.forEach((icon) => {
            icon.classList.remove("active")
        })
    }
    else {
        sideNav.style.width = "60px"
        displayNone()
        sideNavIcon.forEach((icon) => {
            icon.classList.add("active")
            icon.style.marginLeft = "10px"
        })

    }
})


// to go-to top of the dashboard
function scrollTotop(){
    // console.log("clicked");
    document.querySelector(".dashboard-container").scrollTo({
        top:0,
        behavior:"smooth"
    });
}

