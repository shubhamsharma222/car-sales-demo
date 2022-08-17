let menus = document.querySelector('.navbar');
document.querySelector('#menu-icons').onclick = () => {
    menus.classList.toggle('active');
}

//header

let header = document.querySelector('header');

window.addEventListener('scroll',() => {
    header.classList.toggle('shadow',window.scrollY > 0 )
})

//Hide Menu on Scroll

window.onscroll =() => {
    menus.classList.remove('active');
}
