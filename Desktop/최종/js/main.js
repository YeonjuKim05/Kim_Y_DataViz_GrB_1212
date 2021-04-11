const toggleBtn = document.querySelector(".navbar_toogleBtn");
const menu = document.querySelector(".navbar_menu");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
});

const main_title = document.querySelectorAll("#main_title");

const ad_container_bg = document.querySelector(".ad_container_bg");

ad_container_bg.classList.toggle("active");

// image change

var num = 1;
function changePic(idx) {
  if (idx) {
    if (num == 5) return;
    num++;
  } else {
    if (num == 1) return;
    num--;
  }
  var imgTag = document.getElementById("photo");
  imgTag.setAttribute("src", "images/img0" + num + ".png");
}
