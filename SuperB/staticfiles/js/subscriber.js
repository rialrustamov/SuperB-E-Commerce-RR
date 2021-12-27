const SubscribeLogic = {
    url: `${location.origin}/api/subscribe/`,

    addSubscriber(email) {
        console.log(localStorage.getItem('token'));
        fetch(`${this.url}`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'email': email,
            })
        }).then(response => response.json()).then(data => {
        });
    }
}


subscribesend = document.getElementById('subscribesend');
subscribesend.addEventListener('click', () => {
    console.log('salam');
    email = document.getElementById('id_email').value
    SubscribeLogic.addSubscriber(email);
    location.reload()
})