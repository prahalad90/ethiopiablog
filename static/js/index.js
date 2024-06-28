// toggle
const menubtn  = document.getElementById('menu');
const closebtn = document.getElementById('close');
menubtn.addEventListener('click',()=>{
    menubtn.style.display = "none";
    closebtn.style.display = "block";
    document.querySelector('nav ul').style.right= '0';
})
closebtn.addEventListener('click',()=>{
    closebtn.style.display = "none";
    menubtn.style.display = "block";
    document.querySelector('nav ul').style.right= '-100%';
})


