const answerUpdateForm = document.getElementById('answer-update-by-user');
answerUpdateForm.style.display = "none";
const showForm = function(){
   console.log(answerUpdateForm.style)
   if(answerUpdateForm.style.display === "none"){
        answerUpdateForm.style.display = ""
   } else{
    answerUpdateForm.style.display = "none"
   }
}


document.querySelector('#update-answer').addEventListener('click', showForm);