const dropdown = document.getElementById('mydropdown');
const profile = document.getElementById('profile');

profile.addEventListener('click' , function (){
    dropdown.classList.toggle('show-dropdown');
});
//
// window.onclick = function (event){
//     if (event.target == dropdown){
//         dropdown.style.display = "none";
//     }
// };