// const handleLikeClick = (buttonId) => {
//   console.log(buttonId);

//   const likeButton = document.getElementById(buttonId);
//   const likeIcon = likeButton.querySelector("i");

//   const csrftoken = getCookie('csrftoken');
//   // like-button-{{ post.id }}
//   const postId = buttonId.split("-").pop();
//   const url = "/post/like/" + postId + "/"
  
//   // 서버로 좋아요 api를 호출
//   fetch(url, {
//       method: "POST",
//       mode: "same-origin",
//       headers: {
//           'X-CSRFToken': csrftoken
//       }
//   })
//   .then(response => response.json())
//   .then(data => {
//       // 결과를 받고 html(좋아요 하트) 모습을 변경
//       if (data.result === "like") {
//           // 좋아요 세팅
//           likeIcon.classList.replace("fa-heart-o", "fa-heart");

//       } else {
//           // 선택 x, 세팅
//           likeIcon.classList.replace("fa-heart", "fa-heart-o")
//       }
//   });
// }


const selectElem = document.getElementById('selectbox')
selectElem.addEventListener('change', () => {
  const index = selectElem.selectedIndex;
})
$(document).ready(function(){
  var sort = getUrlParameter('sort');
  if(sort == 'title'){
      $('.sort-title').prop('selected', 'selected')
  }else if(sort == 'star'){
      $('.sort-star').prop('selected', 'selected')
  }else if(sort == 'time'){
      $('.sort-time').prop('selected', 'selected')
  }else{
      $('.sort-date').prop('selected', 'selected')
  }
  });


function increment() {
  document.getElementById('input-{{post.pk}}').stepUp();
}
function decrement() {
  document.getElementById('input-{{post.pk}}').stepDown();
}
