window.addEventListener("load", function () {
  productReview()
})

url = location.href.split('/')
url = url[url.length - 2]

function productReview() {
  fetch(`${location.origin}/api/productversion/${url}`,
    {
      method: "GET",
      credentials: 'include',
      headers: {
        "Content-Type": "application/json",
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    }
  ).then(response => response.json()).then(data => {
    console.log(data);
    const review_count = document.getElementById('review_count')
    review_count.innerHTML = `${data['product']['review'].length} Review(s)`
    const overall_rating = document.getElementsByClassName('overall-rating-box')
    const overall_rating_list = document.getElementsByClassName('overall-rating-box-list')
    var total_review = 0
    var review_sum = 0
    const review_list = document.getElementById('review-list')
    review_list.innerHTML = ''
    for (let i = 0; i < data['product']['review'].length; i++) {
      review_sum += data['product']['review'][i]['value_rating'] + data['product']['review'][i]['price_rating'] + data['product']['review'][i]['quality_rating']
      review_list.innerHTML += `<div class="box-reviews2">
            <h3>Customer Reviews</h3>
            <div class="box visible">
              <ul>
                <li>
                  <table class="ratings-table">
                    <colgroup>
                      <col width="1">
                      <col>
                    </colgroup>
                    <tbody class="rating-results">
                      <tr>
                        <th>Value</th>
                        <td>
                          <div class="rating-box">
                            <div class="rating" style="width:${data['product']['review'][i]['value_rating']*20}%"></div>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <th>Quality</th>
                        <td>
                          <div class="rating-box">
                            <div class="rating" style="width:${data['product']['review'][i]['quality_rating']*20}%;"></div>
                          </div>
                        </td>
                      </tr>
                      <tr>
                        <th>Price</th>
                        <td>
                          <div class="rating-box">
                            <div class="rating" style="width:${data['product']['review'][i]['price_rating']*20}%;"></div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div class="review">
                    <h6><a href="#">${data['product']['review'][i]['summary']}</a></h6>
                    <small>Review by <span>${data['product']['review'][i]['nickname']} </span>on ${data['product']['review'][i]['created_at']} </small>
                    <div class="review-txt"> ${data['product']['review'][i]['review']} </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>`
    }
    total_review += review_sum / 3;
    for (let i = 0; i < overall_rating.length; i++) {
      overall_rating[i].innerHTML = `<div style="width:${(total_review / data['product']['review'].length).toFixed(3)*20}%" class="rating"></div>`
    }
    // console.log(overall_rating_list);
    // overall_rating_list.innerHTML = `<div style="width:${(total_review / data['product']['review'].length).toFixed(3)*20}%" class="rating"></div>`
    // console.log(overall_rating_list);


  })
}

var reviewSubmit = document.getElementById('review-submit')
var priceRating = document.getElementsByName('price_rating')
var valueRating = document.getElementsByName('value_rating')
var qualityRating = document.getElementsByName('quality_rating')

for (let i = 0; i < priceRating.length; i++) {
  priceRating[i].onclick = function () {
    reviewSubmit.setAttribute('price_rating', priceRating[i].value)
  }
}

for (let i = 0; i < valueRating.length; i++) {
  valueRating[i].onclick = function () {
    reviewSubmit.setAttribute('value_rating', valueRating[i].value)
  }
}

for (let i = 0; i < qualityRating.length; i++) {
  qualityRating[i].onclick = function () {
    reviewSubmit.setAttribute('quality_rating', qualityRating[i].value)
  }
}


if (reviewSubmit != null) {
  reviewSubmit.onclick = function () {
    const productId = this.getAttribute('data');
    const nickname = document.getElementById('nickname_field').value
    const summary = document.getElementById('nickname_field').value
    const review = document.getElementById('review_field').value
    const price_rating = this.getAttribute('price_rating')
    const value_rating = this.getAttribute('value_rating')
    const quality_rating = this.getAttribute('quality_rating')
    ReviewLogic.productPostReview(productId, nickname, summary, review, price_rating, value_rating, quality_rating);
  }
}


var ReviewLogic = {
  productPostReview(productId, nickname, summary, review, price_rating, value_rating, quality_rating) {
    fetch(`${location.origin}/api/productversion/${url}/`, {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      },
      body: JSON.stringify({
        'product_id': productId,
        'nickname': nickname,
        'summary': summary,
        'review': review,
        'price_rating': price_rating,
        'value_rating': value_rating,
        'quality_rating': quality_rating,
      })
    }).then(response => response.json()).then(data => {
      productReview()
    });
  }
}