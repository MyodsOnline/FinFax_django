const docs_toggle = document.querySelector('#docs');
const docs_content = document.getElementById('docs_active');
const orders_toggle = document.querySelector('#orders');
const orders_content = document.getElementById('orders_active');
const message_text = document.getElementById('id_text');
const list = document.getElementsByClassName('list')


function docs_active() {
    if (docs_content.classList.contains('hidden')){
        docs_content.classList.toggle('active')
        if (orders_content.classList.contains('active')) {
            orders_content.classList.toggle('active')
        }
    }
}
docs_toggle.addEventListener('click', docs_active)

function orders_active() {
    if (orders_content.classList.contains('hidden')){
        orders_content.classList.toggle('active')
        if (docs_content.classList.contains('active')) {
            docs_content.classList.toggle('active')
        }
    }
}
orders_toggle.addEventListener('click', orders_active)

orders_content.addEventListener('click', function (e) {
    if (e.target.classList.contains('title')){
        e.target.nextElementSibling.classList.toggle('hidden')
    }
    if (e.target.classList.contains('fin')){
        message_text.value += e.target.innerText + ' '
    }
})