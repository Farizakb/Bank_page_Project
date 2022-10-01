
var search = document.getElementById("search")
search.addEventListener("click",function(){
  document.getElementById("opening_table").classList.remove("d-none");
  document.getElementById("opening_table").classList.add("d-block")
})
var close = document.getElementById("close")
close.addEventListener("click", function(){
  document.getElementById("opening_table").classList.remove("d-block")
  document.getElementById("opening_table").classList.add("d-none")

})

var ferdi = document.getElementById('ferdi')
var biznes = document.getElementById('biznes')

ferdi.addEventListener("click" ,function(){
  document.getElementById('individual').classList.remove('d-none')
  document.getElementById('business').classList.add('d-none')
  ferdi.classList.remove('border-0')
  ferdi.classList.add('border-bottom')
  biznes.classList.remove('border-bottom')
  biznes.classList.add('border-0')
  




} )

biznes.addEventListener("click" ,function(){
  document.getElementById('business').classList.remove('d-none')
  document.getElementById('individual').classList.add('d-none')
  biznes.classList.remove('border-0')
  biznes.classList.add('border-bottom')
  ferdi.classList.add('border-0')
  ferdi.classList.remove('border-bottom')
  

} )








var filters = {};

$('#isotope').on( 'click', 'button', function() {
  var $this = $(this);
  $this
  // get group key
  var $buttonGroup = $this.parents('.button-group');
  var filterGroup = $buttonGroup.attr('data-filter-group');
  // set filter for group
  filters[ filterGroup ] = $this.attr('data-filter');
  // combine filters
  var filterValue = concatValues( filters );
  $("#product_list").isotope({ filter: filterValue });
});



// flatten object by concatting values
function concatValues( obj ) {
  var value = '';
  for ( var prop in obj ) {
    value += obj[ prop ];
  }
  return value;
}






$(document).ready(function () {
    

  var $element = $('.inputSlider');
  var $inputx = $("#monthValue")
  var totalResultValue = 0;
  var monthlyResultValue = 0;
  var loanResultValue = 0;
  $element
      .rangeslider({
          polyfill: false
      })
  for (let slider of document.querySelectorAll(".rangeslider__handle")) {
      slider.addEventListener("mouseenter", () => {
          $element.rangeslider({})
              .on('input', function () {
                  if (slider.parentElement.id === "js-rangeslider-0") {
                      if (this.id === "inputSlider-1") {
                          var month = parseInt(this.value)
                          document.querySelector("#monthValue").value = month
                      }
                  }
                  if (slider.parentElement.id === "js-rangeslider-1") {
                      if (this.id === "inputSlider-2") {
                          var loan = parseInt(this.value)
                          document.querySelector("#loanValue").value = loan
                      }
                  }
                  calculateResults()

                  function calculateResults(monthInput = document.querySelector("#monthValue").value, loanInput = document.querySelector("#loanValue").value, percentInput = document.querySelector("#percentValue").value) {
                      monthInput = parseInt(monthInput)
                      loanInput = parseInt(loanInput)
                      loanResultValue = 1.01;
                      totalResultValue = Math.floor(loanInput / monthInput) * loanResultValue;
                      totalResultValue= totalResultValue.toFixed(2)
                      updateUI()
                  }

                  function updateUI() {
                      document.querySelector("#percentValue").innerText = `${totalResultValue}`
                  }
              });
      })
  }

});